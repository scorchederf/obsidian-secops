---
atomic_guid: "43e92449-ff60-46e9-83a3-1a38089df94d"
title: "Install MS Exchange Transport Agent Persistence"
framework: "atomic"
generated: "true"
attack_technique_id: "T1505.002"
attack_technique_name: "Server Software Component: Transport Agent"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.002/T1505.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "43e92449-ff60-46e9-83a3-1a38089df94d"
  - "Install MS Exchange Transport Agent Persistence"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Install MS Exchange Transport Agent Persistence

Install a Microsoft Exchange Transport Agent for persistence. This requires execution from an Exchange Client Access Server and the creation of a DLL with specific exports. Seen in use by Turla.
More details- https://docs.microsoft.com/en-us/exchange/transport-agents-exchange-2013-help

## Metadata

- Atomic GUID: 43e92449-ff60-46e9-83a3-1a38089df94d
- Technique: T1505.002: Server Software Component: Transport Agent
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1505.002/T1505.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1505-server_software_component|T1505.002]]

## Input Arguments

### class_factory

- description: Class factory of transport agent.
- type: string
- default: Microsoft.Exchange.Security.Interop.SecurityInteropAgentFactory

### dll_path

- description: Path of DLL to use as transport agent.
- type: path
- default: c:\program files\microsoft\Exchange Server\v15\bin\Microsoft.Exchange.Security.Interop.dll

### transport_agent_identity

- description: Friendly name of transport agent once installed.
- type: string
- default: Security Interop Agent

## Dependencies

Microsoft Exchange SnapIn must be installed

### Prerequisite Check

```untitled
Get-TransportAgent -TransportService FrontEnd
```

### Get Prerequisite

```untitled
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Install-TransportAgent -Name #{transport_agent_identity} -TransportAgentFactory #{class_factory} -AssemblyPath #{dll_path}
Enable-TransportAgent #{transport_agent_identity}
Get-TransportAgent | Format-List Name,Enabled
```

### Cleanup

```powershell
if(Get-Command "Get-TransportAgent" -ErrorAction Ignore){
  Disable-TransportAgent #{transport_agent_identity}
  Uninstall-TransportAgent #{transport_agent_identity}
  Get-TransportAgent
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.002/T1505.002.yaml)
