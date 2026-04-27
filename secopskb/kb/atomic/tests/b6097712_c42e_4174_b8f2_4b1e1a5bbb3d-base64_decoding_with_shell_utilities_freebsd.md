---
atomic_guid: "b6097712-c42e-4174-b8f2-4b1e1a5bbb3d"
title: "Base64 decoding with shell utilities (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1140"
attack_technique_name: "Deobfuscate/Decode Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "b6097712-c42e-4174-b8f2-4b1e1a5bbb3d"
  - "Base64 decoding with shell utilities (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Base64 decoding with shell utilities (freebsd)

Use common shell utilities to decode a base64-encoded text string and echo it to the console

## Metadata

- Atomic GUID: b6097712-c42e-4174-b8f2-4b1e1a5bbb3d
- Technique: T1140: Deobfuscate/Decode Files or Information
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1140/T1140.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]

## Input Arguments

### encoded_file

- description: File to temporarily save encoded text
- type: path
- default: /tmp/T1140.encoded

### message

- description: Message to print to the screen
- type: string
- default: Hello from Atomic Red Team test T1140!

## Executor

- elevation_required: False
- name: sh

### Command

```bash
ENCODED=$(echo '#{message}' | b64encode -r -)
printf $ENCODED | b64decode -r
echo $ENCODED | b64decode -r
echo $(echo $ENCODED) | b64decode -r
echo $ENCODED > #{encoded_file} && b64encode -r #{encoded_file}
echo $ENCODED > #{encoded_file} && b64decode -r < #{encoded_file}
echo $ENCODED > #{encoded_file} && cat #{encoded_file} | b64decode -r
echo $ENCODED > #{encoded_file} && cat < #{encoded_file} | b64decode -r
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml)
