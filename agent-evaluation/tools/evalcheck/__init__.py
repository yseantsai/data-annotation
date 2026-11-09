"""evalcheck: pre-submission checks for an agent-evaluation task.

prose.py carries the A-code prose checks, with their patterns in catalogs.py;
rationale.py carries the E-codes, which encode the platform's own Stage 5
rules. Import order registers the checks.
"""
from . import prose, rationale   # noqa: F401  (registration side effect)
from .core import run, catalog, REGISTRY, ERROR, REC, NOTE   # noqa: F401
from .task import TaskContext, find_tasks                    # noqa: F401

__all__ = ["run", "catalog", "REGISTRY", "TaskContext", "find_tasks",
           "ERROR", "REC", "NOTE"]
