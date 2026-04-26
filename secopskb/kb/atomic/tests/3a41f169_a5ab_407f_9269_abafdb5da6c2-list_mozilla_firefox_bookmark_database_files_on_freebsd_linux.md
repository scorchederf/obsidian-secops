---
atomic_guid: "3a41f169-a5ab-407f-9269-abafdb5da6c2"
title: "List Mozilla Firefox Bookmark Database Files on FreeBSD/Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1217"
attack_technique_name: "Browser Bookmark Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "3a41f169-a5ab-407f-9269-abafdb5da6c2"
  - "List Mozilla Firefox Bookmark Database Files on FreeBSD/Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# List Mozilla Firefox Bookmark Database Files on FreeBSD/Linux

Searches for Mozilla Firefox's places.sqlite file (on FreeBSD or Linux distributions) that contains bookmarks and lists any found instances to a text file.

## Metadata

- Atomic GUID: 3a41f169-a5ab-407f-9269-abafdb5da6c2
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
- default: /tmp/T1217-Firefox.txt

## Executor

- name: sh

### Command

```bash
find / -path "*.mozilla/firefox/*/places.sqlite" 2>/dev/null -exec echo {} >> #{output_file} \;
cat #{output_file} 2>/dev/null
```

### Cleanup

```bash
rm -f #{output_file} 2>/dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml)
