---
atomic_guid: "bc071188-459f-44d5-901a-f8f2625b2d2e"
title: "Enumerate credentials from Windows Credential Manager using vaultcmd.exe [Web Credentials]"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555"
attack_technique_name: "Credentials from Password Stores"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "bc071188-459f-44d5-901a-f8f2625b2d2e"
  - "Enumerate credentials from Windows Credential Manager using vaultcmd.exe [Web Credentials]"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This module will enumerate credentials stored in Web Credentials vault of Windows Credential Manager using builtin utility vaultcmd.exe

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
vaultcmd /listcreds:"Web Credentials" /all
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml)
