---
sigma_id: "36803969-5421-41ec-b92f-8500f79c23b0"
title: "Potential Persistence Via GlobalFlags"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_globalflags.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_globalflags.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "36803969-5421-41ec-b92f-8500f79c23b0"
  - "Potential Persistence Via GlobalFlags"
attack_technique_ids:
  - "T1546.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Persistence Via GlobalFlags

Detects registry persistence technique using the GlobalFlags and SilentProcessExit keys

## Metadata

- Rule ID: 36803969-5421-41ec-b92f-8500f79c23b0
- Status: test
- Level: high
- Author: Karneades, Jonhnathan Ribeiro, Florian Roth
- Date: 2018-04-11
- Modified: 2023-06-05
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_globalflags.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.012]]

## Detection

```yaml
selection_global_flag:
  TargetObject|contains|all:
  - \Microsoft\Windows NT\CurrentVersion\
  - \Image File Execution Options\
  - \GlobalFlag
selection_silent_process:
  TargetObject|contains|all:
  - \Microsoft\Windows NT\CurrentVersion\
  - \SilentProcessExit\
  TargetObject|contains:
  - \ReportingMode
  - \MonitorProcess
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://oddvar.moe/2018/04/10/persistence-using-globalflags-in-image-file-execution-options-hidden-from-autoruns-exe/
- https://www.deepinstinct.com/2021/02/16/lsass-memory-dumps-are-stealthier-than-ever-before-part-2/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_globalflags.yml)
