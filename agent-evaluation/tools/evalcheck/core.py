"""Check registry and findings.

A finding carries a level, and the level depends on who wrote the artifact.
This workspace checks two different kinds of artifact:

  authored   the rationale, the confidence note, the ratings file. Ours. A
             finding here is a defect, and it is an ERROR.
  evidence   the harness output documents. Not ours, and not editable. A
             finding here is an observation to weigh when rating Format &
             Presentation, never something to fix, so it is a NOTE.

Collapsing the two would either turn every tell in a model's output into a
defect we are asked to repair, or soften the standard on our own prose. The
levels are kept apart instead, and only NOTE may attach to evidence.
"""
import re

ERROR = "ERROR"
REC = "REC"
NOTE = "NOTE"
LEVELS = (ERROR, REC, NOTE)

REGISTRY = []
_BY_CODE = {}


class Finding(object):
    __slots__ = ("level", "code", "artifact", "message")

    def __init__(self, level, code, artifact, message):
        self.level = level
        self.code = code
        self.artifact = artifact
        self.message = message

    def as_dict(self):
        return {"level": self.level, "code": self.code,
                "artifact": self.artifact, "message": self.message}

    def line(self):
        where = " %s:" % self.artifact if self.artifact else ""
        return "  %-5s [%s]%s %s" % (self.level, self.code, where, self.message)


class Check(object):
    def __init__(self, fn, codes, rules, scope):
        self.fn = fn
        self.name = fn.__name__
        self.codes = tuple(codes)
        self.rules = tuple(rules)
        self.scope = scope          # "authored", "evidence" or "both"
        self.doc = (fn.__doc__ or "").strip().split("\n")[0]


def check(codes=(), rules=(), scope="both"):
    """Register a check. Refuses a duplicate name or a code another check owns."""
    def deco(fn):
        c = Check(fn, codes, rules, scope)
        if any(x.name == c.name for x in REGISTRY):
            raise ValueError("duplicate check name %s" % c.name)
        for code in c.codes:
            owner = _BY_CODE.get(code)
            if owner is not None and owner is not c:
                raise ValueError("check id %s is emitted by both %s and %s"
                                 % (code, owner.name, c.name))
            _BY_CODE[code] = c
        REGISTRY.append(c)
        return fn
    return deco


class Report(object):
    def __init__(self):
        self.findings = []
        self.facts = {}

    def emit(self, level, code, artifact, message):
        if level not in LEVELS:
            raise ValueError("unknown level %r" % level)
        self.findings.append(Finding(level, code, artifact, message))

    def error(self, code, artifact, message):
        self.emit(ERROR, code, artifact, message)

    def rec(self, code, artifact, message):
        self.emit(REC, code, artifact, message)

    def note(self, code, artifact, message):
        self.emit(NOTE, code, artifact, message)

    def fact(self, key, value):
        self.facts[key] = value

    def of(self, level):
        return [f for f in self.findings if f.level == level]

    @property
    def errors(self):
        return len(self.of(ERROR))

    def as_dict(self, task=None, codes=None):
        return {
            "check": "evalcheck",
            "task": task,
            "codes": sorted(codes) if codes else sorted(_BY_CODE),
            "findings": [f.as_dict() for f in self.findings],
            "error_count": self.errors,
            "facts": self.facts,
        }


def run(ctx, codes=None):
    """Run every registered check, or only those owning one of `codes`."""
    report = Report()
    wanted = set(codes) if codes else None
    for c in REGISTRY:
        if wanted and not (set(c.codes) & wanted):
            continue
        c.fn(ctx, report)
    report.findings.sort(key=lambda f: (LEVELS.index(f.level), f.code, f.artifact or ""))
    return report


_CODE_RE = re.compile(r"^([A-Z])(\d+)")


def catalog():
    """The registered checks, grouped by code, for docs/reference/check-rules.md."""
    rows = []
    for c in REGISTRY:
        for code in c.codes:
            m = _CODE_RE.match(code)
            family = m.group(1) if m else "?"
            order = int(m.group(2)) if m else 0
            rows.append((family, order, code, c.name, c.scope, ", ".join(c.rules), c.doc))
    rows.sort()
    return rows
