---
sigma_id: "cafeeba3-01da-4ab4-b6c4-a31b1d9730c7"
title: "PrintBrm ZIP Creation of Extraction"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_printbrm.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_printbrm.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cafeeba3-01da-4ab4-b6c4-a31b1d9730c7"
  - "PrintBrm ZIP Creation of Extraction"
attack_technique_ids:
  - "T1105"
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of the LOLBIN PrintBrm.exe, which can be used to create or extract ZIP files. PrintBrm.exe should not be run on a normal workstation.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

## Detection

```yaml
selection:
  Image|endswith: \PrintBrm.exe
  CommandLine|contains|all:
  - ' -f'
  - .zip
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/PrintBrm/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_printbrm.yml)
