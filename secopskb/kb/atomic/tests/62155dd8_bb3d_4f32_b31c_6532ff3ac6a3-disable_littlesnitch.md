---
atomic_guid: "62155dd8-bb3d-4f32-b31c-6532ff3ac6a3"
title: "Disable LittleSnitch"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "62155dd8-bb3d-4f32-b31c-6532ff3ac6a3"
  - "Disable LittleSnitch"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable LittleSnitch

Disables LittleSnitch

## Metadata

- Atomic GUID: 62155dd8-bb3d-4f32-b31c-6532ff3ac6a3
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo launchctl unload /Library/LaunchDaemons/at.obdev.littlesnitchd.plist
```

### Cleanup

```bash
sudo launchctl load -w /Library/LaunchDaemons/at.obdev.littlesnitchd.plist
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
