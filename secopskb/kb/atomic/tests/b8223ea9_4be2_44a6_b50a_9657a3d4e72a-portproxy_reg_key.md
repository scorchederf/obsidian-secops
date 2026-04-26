---
atomic_guid: "b8223ea9-4be2-44a6-b50a-9657a3d4e72a"
title: "portproxy reg key"
framework: "atomic"
generated: "true"
attack_technique_id: "T1090.001"
attack_technique_name: "Proxy: Internal Proxy"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1090.001/T1090.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "b8223ea9-4be2-44a6-b50a-9657a3d4e72a"
  - "portproxy reg key"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# portproxy reg key

Adds a registry key to set up a proxy on the endpoint at HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PortProxy\v4tov4
Upon execution there will be a new proxy entry in netsh
netsh interface portproxy show all

## Metadata

- Atomic GUID: b8223ea9-4be2-44a6-b50a-9657a3d4e72a
- Technique: T1090.001: Proxy: Internal Proxy
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1090.001/T1090.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1090-proxy|T1090.001]]

## Input Arguments

### connectaddress

- description: Specifies the IPv4 address to which to connect. Acceptable values are IP address, computer NetBIOS name, or computer DNS name. If an address is not specified, the default is the local computer.
- type: string
- default: 127.0.0.1

### connectport

- description: Specifies the IPv4 port, by port number or service name, to which to connect. If connectport is not specified, the default is the value of listenport on the local computer.
- type: string
- default: 1337

### listenport

- description: Specifies the IPv4 port, by port number or service name, on which to listen.
- type: string
- default: 1337

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
netsh interface portproxy add v4tov4 listenport=#{listenport} connectport=#{connectport} connectaddress=#{connectaddress}
```

### Cleanup

```powershell
netsh interface portproxy delete v4tov4 listenport=#{listenport} -ErrorAction Ignore | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1090.001/T1090.001.yaml)
