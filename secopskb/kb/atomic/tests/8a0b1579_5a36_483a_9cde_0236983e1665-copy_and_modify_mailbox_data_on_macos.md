---
atomic_guid: "8a0b1579-5a36-483a-9cde-0236983e1665"
title: "Copy and Modify Mailbox Data on macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.008"
attack_technique_name: "Email Collection: Mailbox Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.008/T1070.008.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "8a0b1579-5a36-483a-9cde-0236983e1665"
  - "Copy and Modify Mailbox Data on macOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Copy and Modify Mailbox Data on macOS

Copies and modifies mail data on macOS

## Metadata

- Atomic GUID: 8a0b1579-5a36-483a-9cde-0236983e1665
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
echo "Manipulated data" > ~/Library/Mail/copy/manipulated.txt
```

### Cleanup

```bash
rm -rf ~/Library/Mail/copy
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.008/T1070.008.yaml)
