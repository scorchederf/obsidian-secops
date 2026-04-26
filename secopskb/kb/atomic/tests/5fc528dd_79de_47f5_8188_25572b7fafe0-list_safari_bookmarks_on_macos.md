---
atomic_guid: "5fc528dd-79de-47f5-8188-25572b7fafe0"
title: "List Safari Bookmarks on MacOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1217"
attack_technique_name: "Browser Bookmark Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "5fc528dd-79de-47f5-8188-25572b7fafe0"
  - "List Safari Bookmarks on MacOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# List Safari Bookmarks on MacOS

This test searches for Safari's Bookmarks file (on macOS) and lists any found instances to a text file.

## Metadata

- Atomic GUID: 5fc528dd-79de-47f5-8188-25572b7fafe0
- Technique: T1217: Browser Bookmark Discovery
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1217/T1217.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1217-browser_information_discovery|T1217]]

## Input Arguments

### output_file

- description: Path where captured results will be placed.
- type: path
- default: /tmp/T1217-Safari.txt

## Executor

- name: sh

### Command

```sh
find / -path "*/Safari/Bookmarks.plist" 2>/dev/null >> #{output_file} 
cat #{output_file}
```

### Cleanup

```sh
rm -f #{output_file} 2>/dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml)
