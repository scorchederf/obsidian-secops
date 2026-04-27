---
sigma_id: "589ac73f-8e12-409c-964e-31a2f5775ae2"
title: "HackTool - WSASS Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_wsass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_wsass.yml"
build_date: "2026-04-26 17:03:19"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "589ac73f-8e12-409c-964e-31a2f5775ae2"
  - "HackTool - WSASS Execution"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - WSASS Execution

Detects execution of WSASS, a tool used to dump LSASS memory on Windows systems by leveraging WER's
(Windows Error Reporting) WerFaultSecure.EXE to bypass PPL (Protected Process Light) protections.

## Metadata

- Rule ID: 589ac73f-8e12-409c-964e-31a2f5775ae2
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-23
- Modified: 2026-01-09
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_wsass.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_img:
  Image|endswith: \wsass.exe
selection_hash:
  Hashes|contains: IMPHASH=32F5095C9BBDCACF28FD4060EB4DFC42
selection_cli:
  CommandLine|re: (?i)\.exe[\"\']?\s+[^\"]{0,64}werfaultsecure\.exe[\"\']?\s+\d{2,10}
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://github.com/TwoSevenOneT/WSASS
- https://www.zerosalarium.com/2025/09/Dumping-LSASS-With-WER-On-Modern-Windows-11.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_wsass.yml)
