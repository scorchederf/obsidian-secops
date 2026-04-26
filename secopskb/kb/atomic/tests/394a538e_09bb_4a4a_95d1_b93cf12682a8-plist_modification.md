---
atomic_guid: "394a538e-09bb-4a4a-95d1-b93cf12682a8"
title: "Plist Modification"
framework: "atomic"
generated: "true"
attack_technique_id: "T1647"
attack_technique_name: "Plist File Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1647/T1647.yaml"
build_date: "2026-04-26 14:38:40"
executor: "manual"
aliases:
  - "394a538e-09bb-4a4a-95d1-b93cf12682a8"
  - "Plist Modification"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Plist Modification

Modify MacOS plist file in one of two directories

## Metadata

- Atomic GUID: 394a538e-09bb-4a4a-95d1-b93cf12682a8
- Technique: T1647: Plist File Modification
- Platforms: macos
- Executor: manual
- Source Path: atomics/T1647/T1647.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1647-plist_file_modification|T1647]]

## Executor

- name: manual
- steps: 1. Modify a .plist in

    /Library/Preferences

    OR

    ~/Library/Preferences

2. Subsequently, follow the steps for adding and running via [Launch Agent](Persistence/Launch_Agent.md)


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1647/T1647.yaml)
