---
sigma_id: "902cedee-0398-4e3a-8183-6f3a89773a96"
title: "Suspicious Invoke-Item From Mount-DiskImage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_run_from_mount_diskimage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_run_from_mount_diskimage.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "902cedee-0398-4e3a-8183-6f3a89773a96"
  - "Suspicious Invoke-Item From Mount-DiskImage"
attack_technique_ids:
  - "T1553.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Invoke-Item From Mount-DiskImage

Adversaries may abuse container files such as disk image (.iso, .vhd) file formats to deliver malicious payloads that may not be tagged with MOTW.

## Metadata

- Rule ID: 902cedee-0398-4e3a-8183-6f3a89773a96
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-01
- Source Path: rules/windows/powershell/powershell_script/posh_ps_run_from_mount_diskimage.yml

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
  - Get-Volume
  - .DriveLetter
  - 'invoke-item '
  - ):\
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.005/T1553.005.md#atomic-test-2---mount-an-iso-image-and-run-executable-from-the-iso
- https://learn.microsoft.com/en-us/powershell/module/storage/mount-diskimage?view=windowsserver2022-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_run_from_mount_diskimage.yml)
