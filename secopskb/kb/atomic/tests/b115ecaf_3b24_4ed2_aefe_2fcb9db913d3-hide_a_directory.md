---
atomic_guid: "b115ecaf-3b24-4ed2-aefe-2fcb9db913d3"
title: "Hide a Directory"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.001"
attack_technique_name: "Hide Artifacts: Hidden Files and Directories"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "b115ecaf-3b24-4ed2-aefe-2fcb9db913d3"
  - "Hide a Directory"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Hide a Directory

Hide a directory on MacOS

## Metadata

- Atomic GUID: b115ecaf-3b24-4ed2-aefe-2fcb9db913d3
- Technique: T1564.001: Hide Artifacts: Hidden Files and Directories
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1564.001/T1564.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.001]]

## Executor

- name: sh

### Command

```sh
touch /var/tmp/T1564.001_mac.txt
chflags hidden /var/tmp/T1564.001_mac.txt
```

### Cleanup

```sh
rm /var/tmp/T1564.001_mac.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml)
