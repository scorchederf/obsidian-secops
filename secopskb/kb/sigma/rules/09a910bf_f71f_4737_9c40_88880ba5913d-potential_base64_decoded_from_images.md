---
sigma_id: "09a910bf-f71f-4737-9c40-88880ba5913d"
title: "Potential Base64 Decoded From Images"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_tail_base64_decode_from_image.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_tail_base64_decode_from_image.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "macos / process_creation"
aliases:
  - "09a910bf-f71f-4737-9c40-88880ba5913d"
  - "Potential Base64 Decoded From Images"
attack_technique_ids:
  - "T1140"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Base64 Decoded From Images

Detects the use of tail to extract bytes at an offset from an image and then decode the base64 value to create a new file with the decoded content. The detected execution is a bash one-liner.

## Metadata

- Rule ID: 09a910bf-f71f-4737-9c40-88880ba5913d
- Status: test
- Level: high
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-12-20
- Source Path: rules/macos/process_creation/proc_creation_macos_tail_base64_decode_from_image.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]

## Detection

```yaml
selection_image:
  Image|endswith: /bash
selection_view:
  CommandLine|contains|all:
  - tail
  - -c
selection_b64:
  CommandLine|contains|all:
  - base64
  - -d
  - '>'
selection_files:
  CommandLine|contains:
  - .avif
  - .gif
  - .jfif
  - .jpeg
  - .jpg
  - .pjp
  - .pjpeg
  - .png
  - .svg
  - .webp
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.virustotal.com/gui/file/16bafdf741e7a13137c489f3c8db1334f171c7cb13b62617d691b0a64783cc48/behavior
- https://www.virustotal.com/gui/file/483fafc64a2b84197e1ef6a3f51e443f84dc5742602e08b9e8ec6ad690b34ed0/behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_tail_base64_decode_from_image.yml)
