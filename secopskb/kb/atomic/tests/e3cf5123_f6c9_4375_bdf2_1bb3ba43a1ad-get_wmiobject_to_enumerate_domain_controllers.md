---
atomic_guid: "e3cf5123-f6c9-4375-bdf2-1bb3ba43a1ad"
title: "Get-WmiObject to Enumerate Domain Controllers"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "e3cf5123-f6c9-4375-bdf2-1bb3ba43a1ad"
  - "Get-WmiObject to Enumerate Domain Controllers"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The following Atomic test will utilize get-wmiobject to enumerate Active Directory for Domain Controllers.
Upon successful execution a listing of Systems from AD will output with their paths.
Reference: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018: Remote System Discovery]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
try { get-wmiobject -class ds_computer -namespace root\directory\ldap -ErrorAction Stop }
catch { $_; exit $_.Exception.HResult }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
