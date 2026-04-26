---
atomic_guid: "b4f6a567-a27a-41e5-b8ef-ac4b4008bb7e"
title: "Base64 decoding with shell utilities"
framework: "atomic"
generated: "true"
attack_technique_id: "T1140"
attack_technique_name: "Deobfuscate/Decode Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "b4f6a567-a27a-41e5-b8ef-ac4b4008bb7e"
  - "Base64 decoding with shell utilities"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Base64 decoding with shell utilities

Use common shell utilities to decode a base64-encoded text string and echo it to the console

## Metadata

- Atomic GUID: b4f6a567-a27a-41e5-b8ef-ac4b4008bb7e
- Technique: T1140: Deobfuscate/Decode Files or Information
- Platforms: linux, macos
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

```sh
ENCODED=$(echo '#{message}' | base64)
printf $ENCODED | base64 -d
echo $ENCODED | base64 -d
echo $(echo $ENCODED) | base64 -d
echo $ENCODED > #{encoded_file} && base64 -d #{encoded_file}
echo $ENCODED > #{encoded_file} && base64 -d < #{encoded_file}
echo $ENCODED > #{encoded_file} && cat #{encoded_file} | base64 -d
echo $ENCODED > #{encoded_file} && cat < #{encoded_file} | base64 -d
bash -c "{echo,\"$(echo $ENCODED)\"}|{base64,-d}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml)
