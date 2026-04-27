---
sigma_id: "455b9d50-15a1-4b99-853f-8d37655a4c1b"
title: "PUA - Suspicious ActiveDirectory Enumeration Via AdFind.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_adfind_enumeration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_adfind_enumeration.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "455b9d50-15a1-4b99-853f-8d37655a4c1b"
  - "PUA - Suspicious ActiveDirectory Enumeration Via AdFind.EXE"
attack_technique_ids:
  - "T1087.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects active directory enumeration activity using known AdFind CLI flags

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]

## Detection

```yaml
selection_password:
  CommandLine|contains:
  - lockoutduration
  - lockoutthreshold
  - lockoutobservationwindow
  - maxpwdage
  - minpwdage
  - minpwdlength
  - pwdhistorylength
  - pwdproperties
selection_enum_ad:
  CommandLine|contains: -sc admincountdmp
selection_enum_exchange:
  CommandLine|contains: -sc exchaddresses
condition: 1 of selection_*
```

## False Positives

- Authorized administrative activity

## References

- https://www.joeware.net/freetools/tools/adfind/
- https://social.technet.microsoft.com/wiki/contents/articles/7535.adfind-command-examples.aspx
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1087.002/T1087.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_adfind_enumeration.yml)
