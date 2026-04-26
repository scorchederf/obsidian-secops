---
sigma_id: "9e8894c0-0ae0-11ef-9d85-1f2942bec57c"
title: "Suspicious Shell Open Command Registry Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_susp_shell_open_keys_modification_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_shell_open_keys_modification_patterns.yml"
build_date: "2026-04-26 14:14:37"
status: "experimental"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "9e8894c0-0ae0-11ef-9d85-1f2942bec57c"
  - "Suspicious Shell Open Command Registry Modification"
attack_technique_ids:
  - "T1548.002"
  - "T1546.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Shell Open Command Registry Modification

Detects modifications to shell open registry keys that point to suspicious locations typically used by malware for persistence.
Generally, modifications to the `*\shell\open\command` registry key can indicate an attempt to change the default action for opening files,
and various UAC bypass or persistence techniques involve modifying these keys to execute malicious scripts or binaries.

## Metadata

- Rule ID: 9e8894c0-0ae0-11ef-9d85-1f2942bec57c
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2026-01-24
- Source Path: rules/windows/registry/registry_set/registry_set_susp_shell_open_keys_modification_patterns.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.001]]

## Detection

```yaml
selection:
  TargetObject|contains: \shell\open\command\
  Details|contains:
  - \$Recycle.Bin\
  - \AppData\Local\Temp\
  - \Contacts\
  - \Music\
  - \PerfLogs\
  - \Photos\
  - \Pictures\
  - \Users\Public\
  - \Videos\
  - \Windows\Temp\
  - '%AppData%'
  - '%LocalAppData%'
  - '%Temp%'
  - '%tmp%'
condition: selection
```

## False Positives

- Legitimate software installations or updates that modify the shell open command registry keys to these locations.

## References

- https://www.trendmicro.com/en_us/research/25/f/water-curse.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_shell_open_keys_modification_patterns.yml)
