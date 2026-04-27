---
sigma_id: "6b6976a3-b0e6-4723-ac24-ae38a737af41"
title: "Potential Persistence Via Shim Database In Uncommon Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_shim_database_uncommon_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_shim_database_uncommon_location.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "6b6976a3-b0e6-4723-ac24-ae38a737af41"
  - "Potential Persistence Via Shim Database In Uncommon Location"
attack_technique_ids:
  - "T1546.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential Persistence Via Shim Database In Uncommon Location

Detects the installation of a new shim database where the file is located in a non-default location

## Metadata

- Rule ID: 6b6976a3-b0e6-4723-ac24-ae38a737af41
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-01
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_shim_database_uncommon_location.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.011]]

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB\
  - \DatabasePath
filter_main_known_locations:
  Details|contains: :\Windows\AppPatch\Custom
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.fireeye.com/blog/threat-research/2017/05/fin7-shim-databases-persistence.html
- https://andreafortuna.org/2018/11/12/process-injection-and-persistence-using-application-shimming/
- https://www.blackhat.com/docs/asia-14/materials/Erickson/Asia-14-Erickson-Persist-It-Using-And-Abusing-Microsofts-Fix-It-Patches.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_shim_database_uncommon_location.yml)
