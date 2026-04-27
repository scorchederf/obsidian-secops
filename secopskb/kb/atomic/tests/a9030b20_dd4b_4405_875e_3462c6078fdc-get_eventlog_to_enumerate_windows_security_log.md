---
atomic_guid: "a9030b20-dd4b-4405-875e-3462c6078fdc"
title: "Get-EventLog To Enumerate Windows Security Log"
framework: "atomic"
generated: "true"
attack_technique_id: "T1654"
attack_technique_name: "Log Enumeration"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1654/T1654.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "a9030b20-dd4b-4405-875e-3462c6078fdc"
  - "Get-EventLog To Enumerate Windows Security Log"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Get-EventLog To Enumerate Windows Security Log

Uses the built-in PowerShell commandlet Get-EventLog to search for 'SYSTEM' keyword and saves results to a text file.

This technique was observed in a [TheDFIRReport case](https://thedfirreport.com/2023/04/03/malicious-iso-file-leads-to-domain-wide-ransomware/) 
where the threat actor enumerated the Windows Security audit log to determine user accounts and associated IPv4 addresses.

Successful execution will save matching log events to the users temp folder.

## Metadata

- Atomic GUID: a9030b20-dd4b-4405-875e-3462c6078fdc
- Technique: T1654: Log Enumeration
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1654/T1654.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1654-log_enumeration|T1654]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
powershell -c {get-eventlog 'Security' | where {$_.Message -like '*SYSTEM*'} | export-csv $env:temp\T1654_events.txt}
```

### Cleanup

```powershell
powershell -c "remove-item $env:temp\T1654_events.txt -ErrorAction Ignore"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1654/T1654.yaml)
