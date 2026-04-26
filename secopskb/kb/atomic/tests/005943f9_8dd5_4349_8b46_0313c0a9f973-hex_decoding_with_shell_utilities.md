---
atomic_guid: "005943f9-8dd5-4349-8b46-0313c0a9f973"
title: "Hex decoding with shell utilities"
framework: "atomic"
generated: "true"
attack_technique_id: "T1140"
attack_technique_name: "Deobfuscate/Decode Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "005943f9-8dd5-4349-8b46-0313c0a9f973"
  - "Hex decoding with shell utilities"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Hex decoding with shell utilities

Use common shell utilities to decode a hex-encoded text string and echo it to the console

## Metadata

- Atomic GUID: 005943f9-8dd5-4349-8b46-0313c0a9f973
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

## Dependencies

xxd must be present

### Prerequisite Check

```untitled
which xxd
```

### Get Prerequisite

```untitled
echo "Please install xxd"
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
ENCODED=$(echo '#{message}' | xxd -ps -c 256)
printf $ENCODED | xxd -r -p
echo $ENCODED | xxd -r -p
echo $(echo $ENCODED) | xxd -r -p
echo $ENCODED > #{encoded_file} && xxd -r -p #{encoded_file}
echo $ENCODED > #{encoded_file} && xxd -r -p < #{encoded_file}
echo $ENCODED > #{encoded_file} && cat #{encoded_file} | xxd -r -p
echo $ENCODED > #{encoded_file} && cat < #{encoded_file} | xxd -r -p
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml)
