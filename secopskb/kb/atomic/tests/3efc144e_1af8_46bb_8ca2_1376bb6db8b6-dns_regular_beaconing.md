---
atomic_guid: "3efc144e-1af8-46bb-8ca2-1376bb6db8b6"
title: "DNS Regular Beaconing"
framework: "atomic"
generated: "true"
attack_technique_id: "T1071.004"
attack_technique_name: "Application Layer Protocol: DNS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.004/T1071.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "3efc144e-1af8-46bb-8ca2-1376bb6db8b6"
  - "DNS Regular Beaconing"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# DNS Regular Beaconing

This test simulates an infected host beaconing via DNS queries to a command and control server at regular intervals over time.
This behaviour is typical of implants either in an idle state waiting for instructions or configured to use a low query volume over time to evade threshold based detection.
A custom domain and sub-domain will need to be passed as input parameters for this test to work. Upon execution, DNS information about the domain will be displayed for each callout.

## Metadata

- Atomic GUID: 3efc144e-1af8-46bb-8ca2-1376bb6db8b6
- Technique: T1071.004: Application Layer Protocol: DNS
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1071.004/T1071.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.004]]

## Input Arguments

### c2_interval

- description: Seconds between C2 requests to the command and control server
- type: integer
- default: 30

### c2_jitter

- description: Percentage of jitter to add to the C2 interval to create variance in the times between C2 requests
- type: integer
- default: 20

### domain

- description: Default domain to simulate against
- type: string
- default: 127.0.0.1.nip.io

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
.\T1071.004\src\T1071-dns-beacon.ps1 -Domain #{domain} -Subdomain #{subdomain} -QueryType #{query_type} -C2Interval #{c2_interval} -C2Jitter #{c2_jitter} -RunTime #{runtime}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.004/T1071.004.yaml)
