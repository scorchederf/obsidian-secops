---
atomic_guid: "553b39f9-1e8c-47b1-abf5-8daf7b0391e9"
title: "Clear Docker Container Logs"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "553b39f9-1e8c-47b1-abf5-8daf7b0391e9"
  - "Clear Docker Container Logs"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Clear Docker Container Logs

Clears Docker container logs using the Docker CLI and the truncate command, removing all log entries.

## Metadata

- Atomic GUID: 553b39f9-1e8c-47b1-abf5-8daf7b0391e9
- Technique: T1070.003: Indicator Removal on Host: Clear Command History
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1070.003/T1070.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
docker container prune -f && sudo truncate -s 0 /var/lib/docker/containers/*/*-json.log
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
