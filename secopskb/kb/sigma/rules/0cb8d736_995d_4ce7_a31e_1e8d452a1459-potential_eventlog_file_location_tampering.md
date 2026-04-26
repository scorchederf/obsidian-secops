---
sigma_id: "0cb8d736-995d-4ce7-a31e-1e8d452a1459"
title: "Potential EventLog File Location Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_evtx_file_key_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_evtx_file_key_tamper.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "0cb8d736-995d-4ce7-a31e-1e8d452a1459"
  - "Potential EventLog File Location Tampering"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential EventLog File Location Tampering

Detects tampering with EventLog service "file" key. In order to change the default location of an Evtx file. This technique is used to tamper with log collection and alerting

## Metadata

- Rule ID: 0cb8d736-995d-4ce7-a31e-1e8d452a1459
- Status: test
- Level: high
- Author: D3F7A5105
- Date: 2023-01-02
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_evtx_file_key_tamper.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Detection

```yaml
selection:
  TargetObject|contains: \SYSTEM\CurrentControlSet\Services\EventLog\
  TargetObject|endswith: \File
filter:
  Details|contains: \System32\Winevt\Logs\
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows/win32/eventlog/eventlog-key

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_evtx_file_key_tamper.yml)
