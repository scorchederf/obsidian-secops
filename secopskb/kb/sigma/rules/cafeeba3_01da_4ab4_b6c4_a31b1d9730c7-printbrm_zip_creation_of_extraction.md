---
sigma_id: "cafeeba3-01da-4ab4-b6c4-a31b1d9730c7"
title: "PrintBrm ZIP Creation of Extraction"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_printbrm.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_printbrm.yml"
build_date: "2026-04-26 17:03:21"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PrintBrm ZIP Creation of Extraction

Detects the execution of the LOLBIN PrintBrm.exe, which can be used to create or extract ZIP files. PrintBrm.exe should not be run on a normal workstation.

## Metadata

- Rule ID: cafeeba3-01da-4ab4-b6c4-a31b1d9730c7
- Status: test
- Level: high
- Author: frack113
- Date: 2022-05-02
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_printbrm.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]
- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

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
