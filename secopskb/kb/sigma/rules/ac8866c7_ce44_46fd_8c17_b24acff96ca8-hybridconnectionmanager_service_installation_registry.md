---
sigma_id: "ac8866c7-ce44-46fd-8c17-b24acff96ca8"
title: "HybridConnectionManager Service Installation - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_hybridconnectionmgr_svc_installation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_hybridconnectionmgr_svc_installation.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "ac8866c7-ce44-46fd-8c17-b24acff96ca8"
  - "HybridConnectionManager Service Installation - Registry"
attack_technique_ids:
  - "T1608"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the installation of the Azure Hybrid Connection Manager service to allow remote code execution from Azure function.

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1608-stage_capabilities|T1608: Stage Capabilities]]

## Detection

```yaml
selection1:
  TargetObject|contains: \Services\HybridConnectionManager
selection2:
  EventType: SetValue
  Details|contains: Microsoft.HybridConnectionManager.Listener.exe
condition: selection1 or selection2
```

## False Positives

- Unknown

## References

- https://twitter.com/Cyb3rWard0g/status/1381642789369286662

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_hybridconnectionmgr_svc_installation.yml)
