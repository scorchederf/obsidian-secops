---
sigma_id: "092af964-4233-4373-b4ba-d86ea2890288"
title: "Add Debugger Entry To AeDebug For Persistence"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_aedebug_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_aedebug_persistence.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "092af964-4233-4373-b4ba-d86ea2890288"
  - "Add Debugger Entry To AeDebug For Persistence"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Add Debugger Entry To AeDebug For Persistence

Detects when an attacker adds a new "Debugger" value to the "AeDebug" key in order to achieve persistence which will get invoked when an application crashes

## Metadata

- Rule ID: 092af964-4233-4373-b4ba-d86ea2890288
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-21
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_aedebug_persistence.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug\Debugger
  Details|endswith: .dll
filter:
  Details: '"C:\WINDOWS\system32\vsjitdebugger.exe" -p %ld -e %ld -j 0x%p'
condition: selection and not filter
```

## False Positives

- Legitimate use of the key to setup a debugger. Which is often the case on developers machines

## References

- https://persistence-info.github.io/Data/aedebug.html
- https://learn.microsoft.com/en-us/windows/win32/debug/configuring-automatic-debugging

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_aedebug_persistence.yml)
