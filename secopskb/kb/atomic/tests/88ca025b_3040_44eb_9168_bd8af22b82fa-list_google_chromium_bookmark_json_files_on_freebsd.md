---
atomic_guid: "88ca025b-3040-44eb-9168-bd8af22b82fa"
title: "List Google Chromium Bookmark JSON Files on FreeBSD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1217"
attack_technique_name: "Browser Bookmark Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "88ca025b-3040-44eb-9168-bd8af22b82fa"
  - "List Google Chromium Bookmark JSON Files on FreeBSD"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# List Google Chromium Bookmark JSON Files on FreeBSD

Searches for Google Chromium's Bookmark file (on FreeBSD) that contains bookmarks in JSON format and lists any found instances to a text file.

## Metadata

- Atomic GUID: 88ca025b-3040-44eb-9168-bd8af22b82fa
- Technique: T1217: Browser Bookmark Discovery
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1217/T1217.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1217-browser_information_discovery|T1217]]

## Input Arguments

### output_file

- description: Path where captured results will be placed.
- type: path
- default: /tmp/T1217-Chrome.txt

## Executor

- name: sh

### Command

```bash
find / -path "*/.config/chromium/*/Bookmarks" -exec echo {} >> #{output_file} \;
cat #{output_file} 2>/dev/null
```

### Cleanup

```bash
rm -f #{output_file} 2>/dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml)
