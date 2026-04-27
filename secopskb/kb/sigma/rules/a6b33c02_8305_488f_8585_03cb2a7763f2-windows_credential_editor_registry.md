---
sigma_id: "a6b33c02-8305-488f-8585-03cb2a7763f2"
title: "Windows Credential Editor Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_hack_wce_reg.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_hack_wce_reg.yml"
build_date: "2026-04-27 19:13:59"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of Windows Credential Editor (WCE)

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

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
