---
atomic_guid: "fef31710-223a-40ee-8462-a396d6b66978"
title: "DNS Long Domain Query"
framework: "atomic"
generated: "true"
attack_technique_id: "T1071.004"
attack_technique_name: "Application Layer Protocol: DNS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.004/T1071.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "fef31710-223a-40ee-8462-a396d6b66978"
  - "DNS Long Domain Query"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DNS Long Domain Query

This test simulates an infected host returning data to a command and control server using long domain names.
The simulation involves sending DNS queries that gradually increase in length until reaching the maximum length. The intent is to test the effectiveness of detection of DNS queries for long domain names over a set threshold.
 Upon execution, DNS information about the domain will be displayed for each callout.

## Metadata

- Atomic GUID: fef31710-223a-40ee-8462-a396d6b66978
- Technique: T1071.004: Application Layer Protocol: DNS
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1071.004/T1071.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.004]]

## Input Arguments

### domain

- description: Default domain to simulate against
- type: string
- default: 127.0.0.1.nip.io

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
.\T1071.004\src\T1071-dns-domain-length.ps1 -Domain #{domain} -Subdomain #{subdomain} -QueryType #{query_type}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.004/T1071.004.yaml)
