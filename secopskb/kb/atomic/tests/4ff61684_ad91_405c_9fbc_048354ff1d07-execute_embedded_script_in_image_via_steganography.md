---
atomic_guid: "4ff61684-ad91-405c-9fbc-048354ff1d07"
title: "Execute Embedded Script in Image via Steganography"
framework: "atomic"
generated: "true"
attack_technique_id: "T1001.002"
attack_technique_name: "Data Obfuscation via Steganography"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1001.002/T1001.002.yaml"
build_date: "2026-04-27 19:12:25"
executor: "sh"
aliases:
  - "4ff61684-ad91-405c-9fbc-048354ff1d07"
  - "Execute Embedded Script in Image via Steganography"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This atomic test demonstrates the execution of an embedded script in an image file using steganography techniques. The script is first encoded in base64 and then embedded within the pixels of the image. The modified image is created, and the script is extracted and executed on the target system.

## ATT&CK Mapping

- [[kb/attack/techniques/T1001-data_obfuscation#^t1001002-steganography|T1001.002: Steganography]]

## Input Arguments

### evil_image

- description: The modified image with embedded script
- type: String
- default: PathToAtomicsFolder/evil_image.jpg

### image

- description: Image file to be embedded
- type: String
- default: PathToAtomicsFolder/image.jpg

### script

- description: Shell Script file to be embedded and executed
- type: String
- default: PathToAtomicsFolder/script.sh

## Executor

- elevation_required: False
- name: sh

### Command

```bash
cat "#{script}" | base64 | xxd -p | sed 's/../& /g' | xargs -n1 | xxd -r -p | cat "#{image}" - > "#{evil_image}"; strings "#{evil_image}" | tail -n 1 | base64 -d | sh
```

### Cleanup

```bash
rm "#{evil_image}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1001.002/T1001.002.yaml)
