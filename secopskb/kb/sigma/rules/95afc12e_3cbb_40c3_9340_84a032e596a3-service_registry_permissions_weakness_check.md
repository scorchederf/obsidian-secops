---
sigma_id: "95afc12e-3cbb-40c3-9340-84a032e596a3"
title: "Service Registry Permissions Weakness Check"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_get_acl_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_acl_service.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "95afc12e-3cbb-40c3-9340-84a032e596a3"
  - "Service Registry Permissions Weakness Check"
attack_technique_ids:
  - "T1574.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service Registry Permissions Weakness Check

Adversaries may execute their own malicious payloads by hijacking the Registry entries used by services.
Adversaries may use flaws in the permissions for registry to redirect from the originally specified executable to one that they control, in order to launch their own code at Service start.
Windows stores local service configuration information in the Registry under HKLM\SYSTEM\CurrentControlSet\Services

## Metadata

- Rule ID: 95afc12e-3cbb-40c3-9340-84a032e596a3
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-30
- Source Path: rules/windows/powershell/powershell_script/posh_ps_get_acl_service.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - get-acl
  - REGISTRY::HKLM\SYSTEM\CurrentControlSet\Services\
condition: selection
```

## False Positives

- Legitimate administrative script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1574.011/T1574.011.md#atomic-test-1---service-registry-permissions-weakness
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-acl?view=powershell-7.4

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_acl_service.yml)
