---
sigma_id: "17769c90-230e-488b-a463-e05c08e9d48f"
title: "Powershell Defender Exclusion"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_defender_exclusion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_defender_exclusion.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "17769c90-230e-488b-a463-e05c08e9d48f"
  - "Powershell Defender Exclusion"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Defender Exclusion

Detects requests to exclude files, folders or processes from Antivirus scanning using PowerShell cmdlets

## Metadata

- Rule ID: 17769c90-230e-488b-a463-e05c08e9d48f
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2021-04-29
- Modified: 2022-05-12
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_defender_exclusion.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection1:
  CommandLine|contains:
  - 'Add-MpPreference '
  - 'Set-MpPreference '
selection2:
  CommandLine|contains:
  - ' -ExclusionPath '
  - ' -ExclusionExtension '
  - ' -ExclusionProcess '
  - ' -ExclusionIpAddress '
condition: all of selection*
```

## False Positives

- Possible Admin Activity
- Other Cmdlets that may use the same parameters

## References

- https://learn.microsoft.com/en-us/defender-endpoint/configure-process-opened-file-exclusions-microsoft-defender-antivirus
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://twitter.com/AdamTheAnalyst/status/1483497517119590403

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_defender_exclusion.yml)
