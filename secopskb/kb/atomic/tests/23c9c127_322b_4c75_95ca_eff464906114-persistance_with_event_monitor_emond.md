---
atomic_guid: "23c9c127-322b-4c75-95ca-eff464906114"
title: "Persistance with Event Monitor - emond"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.014"
attack_technique_name: "Event Triggered Execution: Emond"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.014/T1546.014.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "23c9c127-322b-4c75-95ca-eff464906114"
  - "Persistance with Event Monitor - emond"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Persistance with Event Monitor - emond

Establish persistence via a rule run by OSX's emond (Event Monitor) daemon at startup, based on https://posts.specterops.io/leveraging-emond-on-macos-for-persistence-a040a2785124

## Metadata

- Atomic GUID: 23c9c127-322b-4c75-95ca-eff464906114
- Technique: T1546.014: Event Triggered Execution: Emond
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1546.014/T1546.014.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.014]]

## Input Arguments

### plist

- description: Path to attacker emond plist file
- type: path
- default: PathToAtomicsFolder/T1546.014/src/T1546.014_emond.plist

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo cp "#{plist}" /etc/emond.d/rules/T1546.014_emond.plist
sudo touch /private/var/db/emondClients/T1546.014
```

### Cleanup

```bash
sudo rm /etc/emond.d/rules/T1546.014_emond.plist
sudo rm /private/var/db/emondClients/T1546.014
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.014/T1546.014.yaml)
