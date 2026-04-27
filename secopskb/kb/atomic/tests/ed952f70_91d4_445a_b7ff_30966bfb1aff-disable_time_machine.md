---
atomic_guid: "ed952f70-91d4-445a-b7ff-30966bfb1aff"
title: "Disable Time Machine"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "ed952f70-91d4-445a-b7ff-30966bfb1aff"
  - "Disable Time Machine"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable Time Machine

Disables Time Machine which is Apple's automated backup utility software. Attackers can use this to prevent backups from occurring and hinder the victim's ability to recover from any damage.

## Metadata

- Atomic GUID: ed952f70-91d4-445a-b7ff-30966bfb1aff
- Technique: T1490: Inhibit System Recovery
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1490/T1490.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo tmutil disable
```

### Cleanup

```bash
sudo tmutil enable
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
