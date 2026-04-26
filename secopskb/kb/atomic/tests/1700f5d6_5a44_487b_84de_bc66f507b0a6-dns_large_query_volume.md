---
atomic_guid: "1700f5d6-5a44-487b-84de-bc66f507b0a6"
title: "DNS Large Query Volume"
framework: "atomic"
generated: "true"
attack_technique_id: "T1071.004"
attack_technique_name: "Application Layer Protocol: DNS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.004/T1071.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "1700f5d6-5a44-487b-84de-bc66f507b0a6"
  - "DNS Large Query Volume"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DNS Large Query Volume

This test simulates an infected host sending a large volume of DNS queries to a command and control server.
The intent of this test is to trigger threshold based detection on the number of DNS queries either from a single source system or to a single targe domain.
A custom domain and sub-domain will need to be passed as input parameters for this test to work. Upon execution, DNS information about the domain will be displayed for each callout.

## Metadata

- Atomic GUID: 1700f5d6-5a44-487b-84de-bc66f507b0a6
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
for($i=0; $i -le #{query_volume}; $i++) { Resolve-DnsName -type "#{query_type}" "#{subdomain}-$(Get-Random -Minimum 1 -Maximum 999999).#{domain}" -QuickTimeout}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.004/T1071.004.yaml)
