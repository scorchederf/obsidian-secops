---
sigma_id: "9ace0707-b560-49b8-b6ca-5148b42f39fb"
title: "Potential Persistence Via Logon Scripts - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_logon_scripts_userinitmprlogonscript.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_logon_scripts_userinitmprlogonscript.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "9ace0707-b560-49b8-b6ca-5148b42f39fb"
  - "Potential Persistence Via Logon Scripts - Registry"
attack_technique_ids:
  - "T1037.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Logon Scripts - Registry

Detects creation of "UserInitMprLogonScript" registry value which can be used as a persistence method by malicious actors

## Metadata

- Rule ID: 9ace0707-b560-49b8-b6ca-5148b42f39fb
- Status: test
- Level: medium
- Author: Tom Ueltschi (@c_APT_ure)
- Date: 2019-01-12
- Modified: 2025-10-26
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_logon_scripts_userinitmprlogonscript.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037.001]]

## Detection

```yaml
selection:
  TargetObject|contains: UserInitMprLogonScript
condition: selection
```

## False Positives

- Investigate the contents of the "UserInitMprLogonScript" value to determine of the added script is legitimate

## Simulation

### Logon Scripts

- atomic_guid: d6042746-07d4-4c92-9ad8-e644c114a231
- name: Logon Scripts
- technique: T1037.001
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1037.001/T1037.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_logon_scripts_userinitmprlogonscript.yml)
