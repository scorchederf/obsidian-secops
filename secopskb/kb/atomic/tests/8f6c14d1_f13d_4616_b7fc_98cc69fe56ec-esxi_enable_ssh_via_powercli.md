---
atomic_guid: "8f6c14d1-f13d-4616-b7fc-98cc69fe56ec"
title: "ESXi - Enable SSH via PowerCLI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.004"
attack_technique_name: "Remote Services: SSH"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.004/T1021.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "8f6c14d1-f13d-4616-b7fc-98cc69fe56ec"
  - "ESXi - Enable SSH via PowerCLI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ESXi - Enable SSH via PowerCLI

An adversary enables the SSH service on a ESXi host to maintain persistent access to the host and to carryout subsequent operations.

## Metadata

- Atomic GUID: 8f6c14d1-f13d-4616-b7fc-98cc69fe56ec
- Technique: T1021.004: Remote Services: SSH
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1021.004/T1021.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.004]]

## Input Arguments

### vm_host

- description: Specify the host name of the ESXi Server
- type: string
- default: atomic.local

### vm_pass

- description: Specify the privilege user password on ESXi Server
- type: string
- default: pass

### vm_user

- description: Specify the privilege user account on ESXi Server
- type: string
- default: root

## Dependencies

Check if VMWARE PowerCLI PowerShell Module is installed.

### Prerequisite Check

```powershell
$RequiredModule = Get-Module -Name VMware.PowerCLI -ListAvailable
if (-not $RequiredModule) {exit 1}
```

### Get Prerequisite

```powershell
Install-Module -Name VMware.PowerCLI
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -ParticipateInCEIP:$false -Confirm:$false 
Connect-VIServer -Server #{vm_host} -User #{vm_user} -Password #{vm_pass}
Get-VMHostService -VMHost #{vm_host} | Where-Object {$_.Key -eq "TSM-SSH" } | Start-VMHostService -Confirm:$false
```

### Cleanup

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -ParticipateInCEIP:$false -Confirm:$false 
Connect-VIServer -Server #{vm_host} -User #{vm_user} -Password #{vm_pass}
Get-VMHostService -VMHost #{vm_host} | Where-Object {$_.Key -eq "TSM-SSH" } | Stop-VMHostService -Confirm:$false
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.004/T1021.004.yaml)
