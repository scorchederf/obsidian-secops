---
sigma_id: "dfb5b4e8-91d0-4291-b40a-e3b0d3942c45"
title: "Potential Persistence Via Shim Database Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_shim_database.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_shim_database.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "dfb5b4e8-91d0-4291-b40a-e3b0d3942c45"
  - "Potential Persistence Via Shim Database Modification"
attack_technique_ids:
  - "T1546.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Shim Database Modification

Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by application shims.
The Microsoft Windows Application Compatibility Infrastructure/Framework (Application Shim) was created to allow for backward compatibility of software as the operating system codebase changes over time

## Metadata

- Rule ID: dfb5b4e8-91d0-4291-b40a-e3b0d3942c45
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-30
- Modified: 2025-10-22
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_shim_database.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.011]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB\
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Custom\
filter_main_empty_string:
  Details: ''
filter_main_empty_value:
  Details: (Empty)
filter_main_null:
  Details: null
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate custom SHIM installations will also trigger this rule

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.011/T1546.011.md#atomic-test-3---registry-key-creation-andor-modification-events-for-sdb
- https://www.fireeye.com/blog/threat-research/2017/05/fin7-shim-databases-persistence.html
- https://andreafortuna.org/2018/11/12/process-injection-and-persistence-using-application-shimming/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_shim_database.yml)
