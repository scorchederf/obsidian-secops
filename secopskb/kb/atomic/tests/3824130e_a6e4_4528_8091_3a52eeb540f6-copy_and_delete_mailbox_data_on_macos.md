---
atomic_guid: "3824130e-a6e4-4528-8091-3a52eeb540f6"
title: "Copy and Delete Mailbox Data on macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.008"
attack_technique_name: "Email Collection: Mailbox Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.008/T1070.008.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "3824130e-a6e4-4528-8091-3a52eeb540f6"
  - "Copy and Delete Mailbox Data on macOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Copy and Delete Mailbox Data on macOS

Copies and deletes mail data on macOS

## Metadata

- Atomic GUID: 3824130e-a6e4-4528-8091-3a52eeb540f6
- Technique: T1070.008: Email Collection: Mailbox Manipulation
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1070.008/T1070.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.008]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
mkdir ~/Library/Mail/copy
cp -R ~/Library/Mail/* ~/Library/Mail/copy
rm -rf ~/Library/Mail/copy/*
```

### Cleanup

```bash
rm -rf ~/Library/Mail/copy
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.008/T1070.008.yaml)
