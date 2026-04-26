---
atomic_guid: "653d39cd-bae7-499a-898c-9fb96b8b5cd1"
title: "Delete log files using built-in log utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "653d39cd-bae7-499a-898c-9fb96b8b5cd1"
  - "Delete log files using built-in log utility"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete log files using built-in log utility

This test deletes main log datastore, inflight log data, time-to-live data(TTL), fault and error content

## Metadata

- Atomic GUID: 653d39cd-bae7-499a-898c-9fb96b8b5cd1
- Technique: T1070.002: Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1070.002/T1070.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.002]]

## Executor

- elevation_required: True
- name: sh

### Command

```sh
sudo log erase --all
sudo log erase --ttl #Deletes only time-to-live log content
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
