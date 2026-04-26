---
sigma_id: "25ffa65d-76d8-4da5-a832-3f2b0136e133"
title: "PUA - Sysinternal Tool Execution - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_pua_sysinternals_execution_via_eula.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_pua_sysinternals_execution_via_eula.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / registry_set"
aliases:
  - "25ffa65d-76d8-4da5-a832-3f2b0136e133"
  - "PUA - Sysinternal Tool Execution - Registry"
attack_technique_ids:
  - "T1588.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Sysinternal Tool Execution - Registry

Detects the execution of a Sysinternals Tool via the creation of the "accepteula" registry key

## Metadata

- Rule ID: 25ffa65d-76d8-4da5-a832-3f2b0136e133
- Status: test
- Level: low
- Author: Markus Neis
- Date: 2017-08-28
- Modified: 2025-10-26
- Source Path: rules/windows/registry/registry_set/registry_set_pua_sysinternals_execution_via_eula.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1588-obtain_capabilities|T1588.002]]

## Detection

```yaml
selection:
  TargetObject|endswith: \EulaAccepted
condition: selection
```

## False Positives

- Legitimate use of SysInternals tools
- Programs that use the same Registry Key

## References

- https://twitter.com/Moti_B/status/1008587936735035392

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_pua_sysinternals_execution_via_eula.yml)
