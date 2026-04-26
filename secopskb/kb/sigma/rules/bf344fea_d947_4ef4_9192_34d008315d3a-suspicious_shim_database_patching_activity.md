---
sigma_id: "bf344fea-d947-4ef4-9192-34d008315d3a"
title: "Suspicious Shim Database Patching Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_shim_database_susp_application.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_shim_database_susp_application.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "bf344fea-d947-4ef4-9192-34d008315d3a"
  - "Suspicious Shim Database Patching Activity"
attack_technique_ids:
  - "T1546.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Shim Database Patching Activity

Detects installation of new shim databases that try to patch sections of known processes for potential process injection or persistence.

## Metadata

- Rule ID: bf344fea-d947-4ef4-9192-34d008315d3a
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-01
- Modified: 2023-12-06
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_shim_database_susp_application.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.011]]

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Custom\
  TargetObject|endswith:
  - \csrss.exe
  - \dllhost.exe
  - \explorer.exe
  - \RuntimeBroker.exe
  - \services.exe
  - \sihost.exe
  - \svchost.exe
  - \taskhostw.exe
  - \winlogon.exe
  - \WmiPrvSe.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/
- https://www.fireeye.com/blog/threat-research/2017/05/fin7-shim-databases-persistence.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_shim_database_susp_application.yml)
