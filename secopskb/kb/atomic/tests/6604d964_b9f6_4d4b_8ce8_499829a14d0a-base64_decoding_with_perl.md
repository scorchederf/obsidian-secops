---
atomic_guid: "6604d964-b9f6-4d4b-8ce8-499829a14d0a"
title: "Base64 decoding with Perl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1140"
attack_technique_name: "Deobfuscate/Decode Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "6604d964-b9f6-4d4b-8ce8-499829a14d0a"
  - "Base64 decoding with Perl"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Base64 decoding with Perl

Use Perl to decode a base64-encoded text string and echo it to the console

## Metadata

- Atomic GUID: 6604d964-b9f6-4d4b-8ce8-499829a14d0a
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

Perl must be present

### Prerequisite Check

```untitled
which perl
```

### Get Prerequisite

```untitled
echo "Please install Perl"
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
ENCODED=$(perl -e "use MIME::Base64;print(encode_base64('#{message}'));")
perl -le "use MIME::Base64;print(decode_base64('$ENCODED'));"
echo $ENCODED | perl -le 'use MIME::Base64;print(decode_base64(<STDIN>));'
echo $ENCODED > #{encoded_file} && perl -le 'use MIME::Base64;open($f,"<","#{encoded_file}");print(decode_base64(<$f>));'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml)
