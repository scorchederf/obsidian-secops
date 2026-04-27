---
atomic_guid: "fb8d4d7e-f5a4-481c-8867-febf13f8b6d3"
title: "Create and start Hyper-V virtual machine"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.006"
attack_technique_name: "Run Virtual Instance"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.006/T1564.006.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "fb8d4d7e-f5a4-481c-8867-febf13f8b6d3"
  - "Create and start Hyper-V virtual machine"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Create a simple Hyper-V VM (Windows native hypervisor) and start up the machine
Cleanup command stops and deletes the newly created VM
https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
https://embracethered.com/blog/posts/2020/shadowbunny-virtual-machine-red-teaming-technique/
https://attack.mitre.org/techniques/T1564/006/

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564006-run-virtual-instance|T1564.006: Run Virtual Instance]]

## Input Arguments

### vm_name

- description: Name of the new virtual machine
- type: string
- default: Atomic VM

## Dependencies

Hyper-V must be enabled on the system
Checks whether Hyper-V is enabled. If not, enables Hyper-V and forces a required restart

### Prerequisite Check

```untitled
if ((Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V).State = "Enabled") {exit 0} else {exit 1}
```

### Get Prerequisite

```untitled
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All -Force
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$VM = "#{vm_name}"
New-VM -Name $VM -Generation 2
Set-VMFirmware $VM -EnableSecureBoot Off
Start-VM $VM
```

### Cleanup

```powershell
Stop-VM $VM -Force
Remove-VM $VM -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.006/T1564.006.yaml)
