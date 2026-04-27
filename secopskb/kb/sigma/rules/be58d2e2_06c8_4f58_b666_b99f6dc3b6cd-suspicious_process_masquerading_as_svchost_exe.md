---
sigma_id: "be58d2e2-06c8-4f58-b666-b99f6dc3b6cd"
title: "Suspicious Process Masquerading As SvcHost.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_svchost_masqueraded_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_svchost_masqueraded_execution.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "be58d2e2-06c8-4f58-b666-b99f6dc3b6cd"
  - "Suspicious Process Masquerading As SvcHost.EXE"
attack_technique_ids:
  - "T1036.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Process Masquerading As SvcHost.EXE

Detects a suspicious process that is masquerading as the legitimate "svchost.exe" by naming its binary "svchost.exe" and executing from an uncommon location.
Adversaries often disguise their malicious binaries by naming them after legitimate system processes like "svchost.exe" to evade detection.

## Metadata

- Rule ID: be58d2e2-06c8-4f58-b666-b99f6dc3b6cd
- Status: test
- Level: high
- Author: Swachchhanda Shrawan Poudel
- Date: 2024-08-07
- Source Path: rules/windows/process_creation/proc_creation_win_svchost_masqueraded_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detection

```yaml
selection:
  Image|endswith: \svchost.exe
filter_main_img_location:
  Image:
  - C:\Windows\System32\svchost.exe
  - C:\Windows\SysWOW64\svchost.exe
filter_main_ofn:
  OriginalFileName: svchost.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://tria.ge/240731-jh4crsycnb/behavioral2
- https://redcanary.com/blog/threat-detection/process-masquerading/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_svchost_masqueraded_execution.yml)
