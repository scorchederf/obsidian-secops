---
sigma_id: "29e1c216-6408-489d-8a06-ee9d151ef819"
title: "Suspicious Mount-DiskImage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_mount_diskimage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_mount_diskimage.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "29e1c216-6408-489d-8a06-ee9d151ef819"
  - "Suspicious Mount-DiskImage"
attack_technique_ids:
  - "T1553.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Mount-DiskImage

Adversaries may abuse container files such as disk image (.iso, .vhd) file formats to deliver malicious payloads that may not be tagged with MOTW.

## Metadata

- Rule ID: 29e1c216-6408-489d-8a06-ee9d151ef819
- Status: test
- Level: low
- Author: frack113
- Date: 2022-02-01
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_mount_diskimage.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.005]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - 'Mount-DiskImage '
  - '-ImagePath '
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.005/T1553.005.md#atomic-test-1---mount-iso-image
- https://learn.microsoft.com/en-us/powershell/module/storage/mount-diskimage?view=windowsserver2022-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_mount_diskimage.yml)
