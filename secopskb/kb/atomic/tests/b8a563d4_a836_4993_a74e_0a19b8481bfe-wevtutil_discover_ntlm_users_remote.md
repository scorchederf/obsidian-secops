---
atomic_guid: "b8a563d4-a836-4993-a74e-0a19b8481bfe"
title: "Wevtutil - Discover NTLM Users Remote"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b8a563d4-a836-4993-a74e-0a19b8481bfe"
  - "Wevtutil - Discover NTLM Users Remote"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Wevtutil - Discover NTLM Users Remote

This test discovers users who have authenticated against a Domain Controller via NTLM. 
This is done remotely via wmic and captures the event code 4776 from the domain controller and stores the ouput in C:\temp. [Reference](https://www.reliaquest.com/blog/socgholish-fakeupdates/)

## Metadata

- Atomic GUID: b8a563d4-a836-4993-a74e-0a19b8481bfe
- Technique: T1087.002: Account Discovery: Domain Account
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1087.002/T1087.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Executor

- name: powershell

### Command

```powershell
$target = $env:LOGONSERVER
$target = $target.Trim("\\")
$IpAddress = [System.Net.Dns]::GetHostAddresses($target) | select IPAddressToString -ExpandProperty IPAddressToString
wmic.exe /node:$IpAddress process call create 'wevtutil epl Security C:\\ntlmusers.evtx /q:\"Event[System[(EventID=4776)]]"'
```

### Cleanup

```powershell
Remove-Item -Path \\$IpAddress\c$\ntlmusers.evtx
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
