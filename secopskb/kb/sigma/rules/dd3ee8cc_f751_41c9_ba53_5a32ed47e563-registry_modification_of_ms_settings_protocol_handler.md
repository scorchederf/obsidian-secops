---
sigma_id: "dd3ee8cc-f751-41c9-ba53-5a32ed47e563"
title: "Registry Modification of MS-settings Protocol Handler"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_registry_modification_of_ms_setting_protocol_handler.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_registry_modification_of_ms_setting_protocol_handler.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "dd3ee8cc-f751-41c9-ba53-5a32ed47e563"
  - "Registry Modification of MS-settings Protocol Handler"
attack_technique_ids:
  - "T1548.002"
  - "T1546.001"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Registry Modification of MS-settings Protocol Handler

Detects registry modifications to the 'ms-settings' protocol handler, which is frequently targeted for UAC bypass or persistence.
Attackers can modify this registry to execute malicious code with elevated privileges by hijacking the command execution path.

## Metadata

- Rule ID: dd3ee8cc-f751-41c9-ba53-5a32ed47e563
- Status: test
- Level: medium
- Author: frack113, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2021-12-20
- Modified: 2026-01-24
- Source Path: rules/windows/process_creation/proc_creation_win_susp_registry_modification_of_ms_setting_protocol_handler.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.001]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_reg_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_pwsh_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - powershell.exe
  - pwsh.dll
selection_reg_cli:
  CommandLine|contains: add
selection_pwsh_cli:
  CommandLine|contains:
  - New-ItemProperty
  - Set-ItemProperty
  - 'ni '
  - 'sp '
selection_cli_key:
  CommandLine|contains: \ms-settings\shell\open\command
condition: (all of selection_reg_* or all of selection_pwsh_*) and selection_cli_key
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2021/12/13/diavol-ransomware/
- https://www.trendmicro.com/en_us/research/25/f/water-curse.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_registry_modification_of_ms_setting_protocol_handler.yml)
