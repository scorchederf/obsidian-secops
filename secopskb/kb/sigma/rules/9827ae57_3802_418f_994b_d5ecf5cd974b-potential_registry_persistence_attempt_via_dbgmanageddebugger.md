---
sigma_id: "9827ae57-3802-418f-994b-d5ecf5cd974b"
title: "Potential Registry Persistence Attempt Via DbgManagedDebugger"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_dbgmanageddebugger_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_dbgmanageddebugger_persistence.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "9827ae57-3802-418f-994b-d5ecf5cd974b"
  - "Potential Registry Persistence Attempt Via DbgManagedDebugger"
attack_technique_ids:
  - "T1574"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Registry Persistence Attempt Via DbgManagedDebugger

Detects the addition of the "Debugger" value to the "DbgManagedDebugger" key in order to achieve persistence. Which will get invoked when an application crashes

## Metadata

- Rule ID: 9827ae57-3802-418f-994b-d5ecf5cd974b
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-07
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_dbgmanageddebugger_persistence.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Microsoft\.NETFramework\DbgManagedDebugger
filter:
  Details: '"C:\Windows\system32\vsjitdebugger.exe" PID %d APPDOM %d EXTEXT "%s" EVTHDL
    %d'
condition: selection and not filter
```

## False Positives

- Legitimate use of the key to setup a debugger. Which is often the case on developers machines

## References

- https://www.hexacorn.com/blog/2013/09/19/beyond-good-ol-run-key-part-4/
- https://github.com/last-byte/PersistenceSniper

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_dbgmanageddebugger_persistence.yml)
