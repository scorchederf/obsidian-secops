---
sigma_id: "514e7e3e-b3b4-4a67-af60-be20f139198b"
title: "PUA - AdFind.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_adfind_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_adfind_execution.yml"
build_date: "2026-04-26 14:14:30"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "514e7e3e-b3b4-4a67-af60-be20f139198b"
  - "PUA - AdFind.EXE Execution"
attack_technique_ids:
  - "T1087.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - AdFind.EXE Execution

Detects execution of Adfind.exe utility, which can be used for reconnaissance in an Active Directory environment

## Metadata

- Rule ID: 514e7e3e-b3b4-4a67-af60-be20f139198b
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-02-26
- Source Path: rules/windows/process_creation/proc_creation_win_pua_adfind_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Detection

```yaml
selection:
- Image|endswith: \AdFind.exe
- OriginalFileName: AdFind.exe
- Hashes|contains:
  - IMPHASH=d144de8117df2beceaba2201ad304764
  - IMPHASH=12ce1c0f3f5837ecc18a3782408fa975
  - IMPHASH=bca5675746d13a1f246e2da3c2217492
  - IMPHASH=4fbf3f084fbbb2470b80b2013134df35
  - IMPHASH=49b639b4acbecc49d72a01f357aa4930
  - IMPHASH=53e117a96057eaf19c41380d0e87f1c2
  - IMPHASH=680dad9e300346e05a85023965867201
  - IMPHASH=21aa085d54992511b9f115355e468782
condition: selection
```

## False Positives

- Unknown

## References

- https://www.joeware.net/freetools/tools/adfind/
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1087.002/T1087.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_adfind_execution.yml)
