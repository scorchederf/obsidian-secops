---
sigma_id: "b6f91281-20aa-446a-b986-38a92813a18f"
title: "DLL Search Order Hijackig Via Additional Space in Path"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_dll_sideloading_space_path.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_dll_sideloading_space_path.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "b6f91281-20aa-446a-b986-38a92813a18f"
  - "DLL Search Order Hijackig Via Additional Space in Path"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when an attacker create a similar folder structure to windows system folders such as (Windows, Program Files...)
but with a space in order to trick DLL load search order and perform a "DLL Search Order Hijacking" attack

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

## Detection

```yaml
selection:
  TargetFilename|startswith:
  - C:\Windows \
  - C:\Program Files \
  - C:\Program Files (x86) \
  TargetFilename|endswith: .dll
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/cyb3rops/status/1552932770464292864
- https://www.wietzebeukema.nl/blog/hijacking-dlls-in-windows

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_dll_sideloading_space_path.yml)
