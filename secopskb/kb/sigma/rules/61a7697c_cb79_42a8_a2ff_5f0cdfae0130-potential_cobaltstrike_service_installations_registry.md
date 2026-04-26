---
sigma_id: "61a7697c-cb79-42a8-a2ff-5f0cdfae0130"
title: "Potential CobaltStrike Service Installations - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_cobaltstrike_service_installs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_cobaltstrike_service_installs.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "61a7697c-cb79-42a8-a2ff-5f0cdfae0130"
  - "Potential CobaltStrike Service Installations - Registry"
attack_technique_ids:
  - "T1021.002"
  - "T1543.003"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential CobaltStrike Service Installations - Registry

Detects known malicious service installs that appear in cases in which a Cobalt Strike beacon elevates privileges or lateral movement.

## Metadata

- Rule ID: 61a7697c-cb79-42a8-a2ff-5f0cdfae0130
- Status: test
- Level: high
- Author: Wojciech Lesicki
- Date: 2021-06-29
- Modified: 2024-03-25
- Source Path: rules/windows/registry/registry_set/registry_set_cobaltstrike_service_installs.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection_key:
- TargetObject|contains: \System\CurrentControlSet\Services
- TargetObject|contains|all:
  - \System\ControlSet
  - \Services
selection_details:
- Details|contains|all:
  - ADMIN$
  - .exe
- Details|contains|all:
  - '%COMSPEC%'
  - start
  - powershell
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://www.sans.org/webcasts/tech-tuesday-workshop-cobalt-strike-detection-log-analysis-119395

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_cobaltstrike_service_installs.yml)
