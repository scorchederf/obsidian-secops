---
sigma_id: "a54f842a-3713-4b45-8c84-5f136fdebd3c"
title: "New PortProxy Registry Entry Added"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_portproxy_registry_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_portproxy_registry_key.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / registry_event"
aliases:
  - "a54f842a-3713-4b45-8c84-5f136fdebd3c"
  - "New PortProxy Registry Entry Added"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New PortProxy Registry Entry Added

Detects the modification of the PortProxy registry key which is used for port forwarding.

## Metadata

- Rule ID: a54f842a-3713-4b45-8c84-5f136fdebd3c
- Status: test
- Level: medium
- Author: Andreas Hunkeler (@Karneades)
- Date: 2021-06-22
- Modified: 2024-03-25
- Source Path: rules/windows/registry/registry_event/registry_event_portproxy_registry_key.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090]]

## Detection

```yaml
selection:
  TargetObject|contains: \Services\PortProxy\v4tov4\tcp\
condition: selection
```

## False Positives

- WSL2 network bridge PowerShell script used for WSL/Kubernetes/Docker (e.g. https://github.com/microsoft/WSL/issues/4150#issuecomment-504209723)
- Synergy Software KVM (https://symless.com/synergy)

## References

- https://www.fireeye.com/blog/threat-research/2019/01/bypassing-network-restrictions-through-rdp-tunneling.html
- https://adepts.of0x.cc/netsh-portproxy-code/
- https://www.dfirnotes.net/portproxy_detection/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_portproxy_registry_key.yml)
