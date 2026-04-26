---
sigma_id: "f44800ac-38ec-471f-936e-3fa7d9c53100"
title: "PUA - CleanWipe Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_cleanwipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_cleanwipe.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f44800ac-38ec-471f-936e-3fa7d9c53100"
  - "PUA - CleanWipe Execution"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - CleanWipe Execution

Detects the use of CleanWipe a tool usually used to delete Symantec antivirus.

## Metadata

- Rule ID: f44800ac-38ec-471f-936e-3fa7d9c53100
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-12-18
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_pua_cleanwipe.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection1:
  Image|endswith: \SepRemovalToolNative_x64.exe
selection2:
  Image|endswith: \CATClean.exe
  CommandLine|contains: --uninstall
selection3:
  Image|endswith: \NetInstaller.exe
  CommandLine|contains: -r
selection4:
  Image|endswith: \WFPUnins.exe
  CommandLine|contains|all:
  - /uninstall
  - /enterprise
condition: 1 of selection*
```

## False Positives

- Legitimate administrative use (Should be investigated either way)

## References

- https://github.com/3CORESec/MAL-CL/tree/master/Descriptors/Other/CleanWipe

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_cleanwipe.yml)
