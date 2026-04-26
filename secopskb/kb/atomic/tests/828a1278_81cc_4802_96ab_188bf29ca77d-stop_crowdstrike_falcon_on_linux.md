---
atomic_guid: "828a1278-81cc-4802-96ab-188bf29ca77d"
title: "Stop Crowdstrike Falcon on Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "828a1278-81cc-4802-96ab-188bf29ca77d"
  - "Stop Crowdstrike Falcon on Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Stop Crowdstrike Falcon on Linux

Stop and disable Crowdstrike Falcon on Linux

## Metadata

- Atomic GUID: 828a1278-81cc-4802-96ab-188bf29ca77d
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: sh

### Command

```sh
sudo systemctl stop falcon-sensor.service
sudo systemctl disable falcon-sensor.service
```

### Cleanup

```sh
sudo systemctl enable falcon-sensor.service
sudo systemctl start falcon-sensor.service
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
