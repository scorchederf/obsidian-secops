---
atomic_guid: "ed952f70-91d4-445a-b7ff-30966bfb1aff"
title: "Disable Time Machine"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-27 19:12:27"
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

Disables Time Machine which is Apple's automated backup utility software. Attackers can use this to prevent backups from occurring and hinder the victim's ability to recover from any damage.

## ATT&CK Mapping

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]

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
