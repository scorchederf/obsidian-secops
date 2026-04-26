---
sigma_id: "1e8a9b4d-3c2a-4f9b-8d1e-7c6a5b4f3d2e"
title: "PowerShell Defender Threat Severity Default Action Set to 'Allow' or 'NoAction'"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_defender_default_action_modified.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_defender_default_action_modified.yml"
build_date: "2026-04-26 17:03:21"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1e8a9b4d-3c2a-4f9b-8d1e-7c6a5b4f3d2e"
  - "PowerShell Defender Threat Severity Default Action Set to 'Allow' or 'NoAction'"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerShell Defender Threat Severity Default Action Set to 'Allow' or 'NoAction'

Detects the use of PowerShell to execute the 'Set-MpPreference' cmdlet to configure Windows Defender's threat severity default action to 'Allow' (value '6') or 'NoAction' (value '9').
This is a highly suspicious configuration change that effectively disables Defender's ability to automatically mitigate threats of a certain severity level.
An attacker might use this technique via the command line to bypass defenses before executing payloads.

## Metadata

- Rule ID: 1e8a9b4d-3c2a-4f9b-8d1e-7c6a5b4f3d2e
- Status: experimental
- Level: high
- Author: Matt Anderson (Huntress)
- Date: 2025-07-11
- Source Path: rules/windows/process_creation/proc_creation_win_defender_default_action_modified.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_cmdlet:
  CommandLine|contains: Set-MpPreference
selection_action:
  CommandLine|contains:
  - -LowThreatDefaultAction
  - -ModerateThreatDefaultAction
  - -HighThreatDefaultAction
  - -SevereThreatDefaultAction
  - '-ltdefac '
  - '-mtdefac '
  - '-htdefac '
  - '-stdefac '
selection_value:
  CommandLine|contains:
  - Allow
  - '6'
  - NoAction
  - '9'
condition: all of selection_*
```

## False Positives

- Highly unlikely

## References

- https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference
- https://learn.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/security-malware-windows-defender-threatseveritydefaultaction
- https://research.splunk.com/endpoint/7215831c-8252-4ae3-8d43-db588e82f952
- https://gist.github.com/Dump-GUY/8daef859f382b895ac6fd0cf094555d2
- https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_defender_default_action_modified.yml)
