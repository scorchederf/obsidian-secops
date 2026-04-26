---
sigma_id: "c90362e0-2df3-4e61-94fe-b37615814cb1"
title: "Potential Persistence Via Netsh Helper DLL - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_netsh_helper_dll_potential_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_netsh_helper_dll_potential_persistence.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "c90362e0-2df3-4e61-94fe-b37615814cb1"
  - "Potential Persistence Via Netsh Helper DLL - Registry"
attack_technique_ids:
  - "T1546.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Netsh Helper DLL - Registry

Detects changes to the Netsh registry key to add a new DLL value. This change might be an indication of a potential persistence attempt by adding a malicious Netsh helper

## Metadata

- Rule ID: c90362e0-2df3-4e61-94fe-b37615814cb1
- Status: test
- Level: medium
- Author: Anish Bogati
- Date: 2023-11-28
- Modified: 2025-10-08
- Source Path: rules/windows/registry/registry_set/registry_set_netsh_helper_dll_potential_persistence.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.007]]

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\Microsoft\NetSh
  Details|contains: .dll
filter_main_poqexec:
  Image: C:\Windows\System32\poqexec.exe
  Details:
  - ipmontr.dll
  - iasmontr.dll
  - ippromon.dll
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate helper added by different programs and the OS

## References

- https://www.ired.team/offensive-security/persistence/t1128-netsh-helper-dll
- https://pentestlab.blog/2019/10/29/persistence-netsh-helper-dll/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_netsh_helper_dll_potential_persistence.yml)
