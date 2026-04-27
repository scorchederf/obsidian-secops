---
sigma_id: "add64136-62e5-48ea-807e-88638d02df1e"
title: "Fsutil Suspicious Invocation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_fsutil_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fsutil_usage.yml"
build_date: "2026-04-27 19:13:51"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "add64136-62e5-48ea-807e-88638d02df1e"
  - "Fsutil Suspicious Invocation"
attack_technique_ids:
  - "T1070"
  - "T1485"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious parameters of fsutil (deleting USN journal, configuring it with small size, etc).
Might be used by ransomwares during the attack (seen by NotPetya and others).

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070: Indicator Removal]]
- [[kb/attack/techniques/T1485-data_destruction|T1485: Data Destruction]]

## Detection

```yaml
selection_img:
- Image|endswith: \fsutil.exe
- OriginalFileName: fsutil.exe
selection_cli:
  CommandLine|contains:
  - deletejournal
  - createjournal
  - setZeroData
condition: all of selection_*
```

## False Positives

- Admin activity
- Scripts and administrative tools used in the monitored environment

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-usn
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070/T1070.md
- https://eqllib.readthedocs.io/en/latest/analytics/c91f422a-5214-4b17-8664-c5fcf115c0a2.html
- https://github.com/albertzsigovits/malware-notes/blob/558898932c1579ff589290092a2c8febefc3a4c9/Ransomware/Lockbit.md
- https://blog.cluster25.duskrise.com/2023/05/22/back-in-black-blackbyte-nt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fsutil_usage.yml)
