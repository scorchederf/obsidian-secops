---
sigma_id: "fcddca7c-b9c0-4ddf-98da-e1e2d18b0157"
title: "Disabled Windows Defender Eventlog"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disabled_microsoft_defender_eventlog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disabled_microsoft_defender_eventlog.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "fcddca7c-b9c0-4ddf-98da-e1e2d18b0157"
  - "Disabled Windows Defender Eventlog"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disabled Windows Defender Eventlog

Detects the disabling of the Windows Defender eventlog as seen in relation to Lockbit 3.0 infections

## Metadata

- Rule ID: fcddca7c-b9c0-4ddf-98da-e1e2d18b0157
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-07-04
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_disabled_microsoft_defender_eventlog.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|contains: \Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Windows
    Defender/Operational\Enabled
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Other Antivirus software installations could cause Windows to disable that eventlog (unknown)

## References

- https://twitter.com/WhichbufferArda/status/1543900539280293889/photo/2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disabled_microsoft_defender_eventlog.yml)
