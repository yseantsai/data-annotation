# Task 002 prompt

The prompt as given to both harnesses. Category: Immigration Law (adjudication).
Task author: not stated on the task page as supplied.

Supplied by the user on 2026-11-05 and recorded before either harness ran.
Reproduced verbatim, including its original typography.

## Prompt text

> As an Immigration Services Officer at the USCIS Nebraska Service Center, you handle a variety of immigration cases. Sometimes you have mostly routine cases, and sometimes you need to adjudicate more complicated ones, such as VAWA based self-petitions.
>
> This afternoon, on Monday, October 12, 2026, you need to adjudicate the VAWA petitioner's case: Marcia Evadne Whitfield, a citizen of Jamaica, who is seeking an immigration benefit as a self-petitioning spouse. She is claiming her husband, Vernon Lloyd Lattimore, a U.S. citizen by birth, abused her with extreme cruelty and battery.
>
> You pre-reviewed the petitioner’s files yesterday. In all files, the filing requirements are met. Vernon Lloyd Lattimore’s citizenship evidence was reviewed, and his U.S. citizenship was successfully established. The pre-reviewed record contains sufficient good-faith-marriage evidence. The submitted marriage certificate raised no concerns. You also reviewed routine identity and civil-status documentation confirming neither spouse had a prior unresolved marriage. Pre-reviewed police clearance reports are sufficient to prove the petitioner’s good moral character. The joint residency element is also established.
>
> Earlier today, you interviewed the petitioner. Her testimony was consistent and coherent with the case files, but contained no new information on the case. She was clearly upset, which is typical in similar cases. You formed an impression that her testimony is credible and she would not be able to provide any significant new testimony or documents on the case.
>
> What you have not reviewed yet in close detail is attached in the input files: the completed Form I-360, the petitioner’s affidavit, her friend Desmond’s affidavit, Marcia’s first cousin Simone’s affidavit, and the petitioner’s psychological report. Review all the mentioned documents now. Treat all mentioned documents as properly signed.
>
> Additionally, attached is the USCIS Policy Manual extract to guide you: USCISPolicy_Manual_Volume_3_Part_D_VAWA.
>
> You need to make a decision about the petitioner today, meaning you can approve, request further evidence, issue a notice of intent to deny, or deny. You must issue only one decision: Approve/Request for Evidence/Notice of Intent to Deny/Deny.
>
> Decide on the record in front of you. Explain in detail your reasoning for the selected decision and the relevant eligibility findings. Use referrals and citations to a specific document while reaching the conclusion. Document-specific locators such as page number and numbered declaration paragraph are also acceptable. Use neutral language and maintain a professional tone.

## Input files given with it

Received as `inputs/input-files.zip`, unpacked beside it in `inputs/`:

- `Affidavit_Desmond_Reid.pdf`
- `Affidavit_Marcia_Whitfield.pdf`
- `Affidavit_Simone_Barrett.pdf`
- `I-360_Whitfield.pdf`
- `Psychosocial_Report_Hale.pdf`
- `USCIS_Policy_Manual_Volume_3_Part_D_VAWA.pdf`

The Policy Manual extract is supplied as an input, so it is material the models
were given, not outside reference. A citation to it is traceable; a citation to
a provision outside it is not.

## Reference solution description

In [reference-solution.md](reference-solution.md), kept out of this file on
purpose. `evalcheck` E06 fails a task where any of it reappears here.
