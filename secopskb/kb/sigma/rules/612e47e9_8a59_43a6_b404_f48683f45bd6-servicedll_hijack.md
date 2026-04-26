---
sigma_id: "612e47e9-8a59-43a6-b404-f48683f45bd6"
title: "ServiceDll Hijack"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_servicedll_hijack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_servicedll_hijack.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "612e47e9-8a59-43a6-b404-f48683f45bd6"
  - "ServiceDll Hijack"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ServiceDll Hijack

Detects changes to the "ServiceDLL" value related to a service in the registry.
This is often used as a method of persistence.

## Metadata

- Rule ID: 612e47e9-8a59-43a6-b404-f48683f45bd6
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-04
- Modified: 2024-04-03
- Source Path: rules/windows/registry/registry_set/registry_set_servicedll_hijack.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - \System\
  - ControlSet
  - \Services\
  TargetObject|endswith: \Parameters\ServiceDll
filter_main_printextensionmanger:
  Details: C:\Windows\system32\spool\drivers\x64\3\PrintConfig.dll
filter_main_domain_controller:
  Image: C:\Windows\system32\lsass.exe
  TargetObject|endswith: \Services\NTDS\Parameters\ServiceDll
  Details: '%%systemroot%%\system32\ntdsa.dll'
filter_main_poqexec:
  Image: C:\Windows\System32\poqexec.exe
filter_optional_safetica:
  Image|endswith: \regsvr32.exe
  Details: C:\Windows\System32\STAgent.dll
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Administrative scripts
- Installation of a service

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1543.003/T1543.003.md#atomic-test-4---tinyturla-backdoor-service-w64time
- https://www.hexacorn.com/blog/2013/09/19/beyond-good-ol-run-key-part-4/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_servicedll_hijack.yml)
