---
atomic_guid: "ae9ef4b0-d8c1-49d4-8758-06206f19af0a"
title: "DNS over HTTPS Large Query Volume"
framework: "atomic"
generated: "true"
attack_technique_id: "T1572"
attack_technique_name: "Protocol Tunneling"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "ae9ef4b0-d8c1-49d4-8758-06206f19af0a"
  - "DNS over HTTPS Large Query Volume"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DNS over HTTPS Large Query Volume

This test simulates an infected host sending a large volume of DoH queries to a command and control server.
The intent of this test is to trigger threshold based detection on the number of DoH queries either from a single source system or to a single targe domain.
A custom domain and sub-domain will need to be passed as input parameters for this test to work. Upon execution, DNS information about the domain will be displayed for each callout in a JSON format.

## Metadata

- Atomic GUID: ae9ef4b0-d8c1-49d4-8758-06206f19af0a
- Technique: T1572: Protocol Tunneling
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1572/T1572.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Input Arguments

### doh_server

- description: Default DoH resolver
- type: string
- default: https://8.8.8.8/resolve

### domain

- description: Default domain to simulate against
- type: string
- default: 127.0.0.1.xip.io

### query_type

- description: DNS query type
- type: string
- default: TXT

### query_volume

- description: Number of DNS queries to send
- type: integer
- default: 1000

### subdomain

- description: Subdomain prepended to the domain name
- type: string
- default: atomicredteam

## Executor

- name: powershell

### Command

```powershell
for($i=0; $i -le #{query_volume}; $i++) { (Invoke-WebRequest "#{doh_server}?name=#{subdomain}.$(Get-Random -Minimum 1 -Maximum 999999).#{domain}&type=#{query_type}" -UseBasicParsing).Content }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml)
