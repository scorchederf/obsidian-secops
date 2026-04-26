---
sigma_id: "a6b33c02-8305-488f-8585-03cb2a7763f2"
title: "Windows Credential Editor Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_hack_wce_reg.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_hack_wce_reg.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "critical"
logsource: "windows / registry_event"
aliases:
  - "a6b33c02-8305-488f-8585-03cb2a7763f2"
  - "Windows Credential Editor Registry"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Credential Editor Registry

Detects the use of Windows Credential Editor (WCE)

## Metadata

- Rule ID: a6b33c02-8305-488f-8585-03cb2a7763f2
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2019-12-31
- Modified: 2021-11-27
- Source Path: rules/windows/registry/registry_event/registry_event_hack_wce_reg.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

### Software Tags

- S0005

## Detection

```yaml
selection:
  TargetObject|contains: Services\WCESERVICE\Start
condition: selection
```

## False Positives

- Unknown

## References

- https://www.ampliasecurity.com/research/windows-credentials-editor/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_hack_wce_reg.yml)
