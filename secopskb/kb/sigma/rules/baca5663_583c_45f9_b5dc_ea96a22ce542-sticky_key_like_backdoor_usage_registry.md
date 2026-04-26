---
sigma_id: "baca5663-583c-45f9-b5dc-ea96a22ce542"
title: "Sticky Key Like Backdoor Usage - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_stickykey_like_backdoor.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_stickykey_like_backdoor.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "critical"
logsource: "windows / registry_event"
aliases:
  - "baca5663-583c-45f9-b5dc-ea96a22ce542"
  - "Sticky Key Like Backdoor Usage - Registry"
attack_technique_ids:
  - "T1546.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Sticky Key Like Backdoor Usage - Registry

Detects the usage and installation of a backdoor that uses an option to register a malicious debugger for built-in tools that are accessible in the login screen

## Metadata

- Rule ID: baca5663-583c-45f9-b5dc-ea96a22ce542
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems), @twjackomo, Jonhnathan Ribeiro, oscd.community
- Date: 2018-03-15
- Modified: 2022-11-26
- Source Path: rules/windows/registry/registry_event/registry_event_stickykey_like_backdoor.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.008]]

## Detection

```yaml
selection_registry:
  TargetObject|endswith:
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe\Debugger
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\utilman.exe\Debugger
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\osk.exe\Debugger
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Magnify.exe\Debugger
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Narrator.exe\Debugger
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\DisplaySwitch.exe\Debugger
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\atbroker.exe\Debugger
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\HelpPane.exe\Debugger
condition: selection_registry
```

## False Positives

- Unlikely

## References

- https://blogs.technet.microsoft.com/jonathantrull/2016/10/03/detecting-sticky-key-backdoors/
- https://bazaar.abuse.ch/sample/6f3aa9362d72e806490a8abce245331030d1ab5ac77e400dd475748236a6cc81/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_stickykey_like_backdoor.yml)
