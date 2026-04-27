---
atomic_guid: "9a1ec7da-b892-449f-ad68-67066d04380c"
title: "Show all hidden files"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.001"
attack_technique_name: "Hide Artifacts: Hidden Files and Directories"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "9a1ec7da-b892-449f-ad68-67066d04380c"
  - "Show all hidden files"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Show all hidden files on MacOS

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564001-hidden-files-and-directories|T1564.001: Hidden Files and Directories]]

## Executor

- name: sh

### Command

```bash
defaults write com.apple.finder AppleShowAllFiles YES
```

### Cleanup

```bash
defaults write com.apple.finder AppleShowAllFiles NO
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml)
