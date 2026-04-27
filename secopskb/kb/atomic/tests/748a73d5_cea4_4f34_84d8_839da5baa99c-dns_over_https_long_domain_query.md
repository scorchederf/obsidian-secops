---
atomic_guid: "748a73d5-cea4-4f34-84d8-839da5baa99c"
title: "DNS over HTTPS Long Domain Query"
framework: "atomic"
generated: "true"
attack_technique_id: "T1572"
attack_technique_name: "Protocol Tunneling"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "748a73d5-cea4-4f34-84d8-839da5baa99c"
  - "DNS over HTTPS Long Domain Query"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test simulates an infected host returning data to a command and control server using long domain names.
The simulation involves sending DoH queries that gradually increase in length until reaching the maximum length. The intent is to test the effectiveness of detection of DoH queries for long domain names over a set threshold.
 Upon execution, DNS information about the domain will be displayed for each callout in a JSON format.

## ATT&CK Mapping

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572: Protocol Tunneling]]

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

### subdomain

- description: Subdomain prepended to the domain name (should be 63 characters to test maximum length)
- type: string
- default: atomicredteamatomicredteamatomicredteamatomicredteamatomicredte

## Executor

- name: powershell

### Command

```powershell
Set-Location "PathToAtomicsFolder"
.\T1572\src\T1572-doh-domain-length.ps1 -DohServer #{doh_server} -Domain #{domain} -Subdomain #{subdomain} -QueryType #{query_type}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml)
