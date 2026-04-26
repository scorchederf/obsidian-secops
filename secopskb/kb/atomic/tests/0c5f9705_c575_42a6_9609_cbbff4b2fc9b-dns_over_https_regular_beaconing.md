---
atomic_guid: "0c5f9705-c575-42a6-9609-cbbff4b2fc9b"
title: "DNS over HTTPS Regular Beaconing"
framework: "atomic"
generated: "true"
attack_technique_id: "T1572"
attack_technique_name: "Protocol Tunneling"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "0c5f9705-c575-42a6-9609-cbbff4b2fc9b"
  - "DNS over HTTPS Regular Beaconing"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DNS over HTTPS Regular Beaconing

This test simulates an infected host beaconing via DoH queries to a command and control server at regular intervals over time.
This behaviour is typical of implants either in an idle state waiting for instructions or configured to use a low query volume over time to evade threshold based detection.
A custom domain and sub-domain will need to be passed as input parameters for this test to work. Upon execution, DNS information about the domain will be displayed for each callout in a JSON format.

## Metadata

- Atomic GUID: 0c5f9705-c575-42a6-9609-cbbff4b2fc9b
- Technique: T1572: Protocol Tunneling
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1572/T1572.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Input Arguments

### c2_interval

- description: Seconds between C2 requests to the command and control server
- type: integer
- default: 30

### c2_jitter

- description: Percentage of jitter to add to the C2 interval to create variance in the times between C2 requests
- type: integer
- default: 20

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

### runtime

- description: Time in minutes to run the simulation
- type: integer
- default: 30

### subdomain

- description: Subdomain prepended to the domain name
- type: string
- default: atomicredteam

## Executor

- name: powershell

### Command

```powershell
Set-Location "PathToAtomicsFolder"
.\T1572\src\T1572-doh-beacon.ps1 -DohServer #{doh_server} -Domain #{domain} -Subdomain #{subdomain} -QueryType #{query_type} -C2Interval #{c2_interval} -C2Jitter #{c2_jitter} -RunTime #{runtime}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1572/T1572.yaml)
