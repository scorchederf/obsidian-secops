---
sigma_id: "152f3630-77c1-4284-bcc0-4cc68ab2f6e7"
title: "Shell Open Registry Keys Manipulation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_shell_open_keys_manipulation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_shell_open_keys_manipulation.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "152f3630-77c1-4284-bcc0-4cc68ab2f6e7"
  - "Shell Open Registry Keys Manipulation"
attack_technique_ids:
  - "T1548.002"
  - "T1546.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Shell Open Registry Keys Manipulation

Detects the shell open key manipulation (exefile and ms-settings) used for persistence and the pattern of UAC Bypass using fodhelper.exe, computerdefaults.exe, slui.exe via registry keys (e.g. UACMe 33 or 62)

## Metadata

- Rule ID: 152f3630-77c1-4284-bcc0-4cc68ab2f6e7
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-30
- Modified: 2022-01-13
- Source Path: rules/windows/registry/registry_event/registry_event_shell_open_keys_manipulation.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.001]]

## Detection

```yaml
selection1:
  EventType: SetValue
  TargetObject|endswith: Classes\ms-settings\shell\open\command\SymbolicLinkValue
  Details|contains: \Software\Classes\{
selection2:
  TargetObject|endswith: Classes\ms-settings\shell\open\command\DelegateExecute
selection3:
  EventType: SetValue
  TargetObject|endswith:
  - Classes\ms-settings\shell\open\command\(Default)
  - Classes\exefile\shell\open\command\(Default)
filter_sel3:
  Details: (Empty)
condition: selection1 or selection2 or (selection3 and not filter_sel3)
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME
- https://winscripting.blog/2017/05/12/first-entry-welcome-and-uac-bypass/
- https://github.com/RhinoSecurityLabs/Aggressor-Scripts/tree/master/UACBypass
- https://tria.ge/211119-gs7rtshcfr/behavioral2 [Lokibot sample from Nov 2021]

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_shell_open_keys_manipulation.yml)
