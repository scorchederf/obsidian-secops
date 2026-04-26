---
atomic_guid: "189f7d6e-9442-4160-9bc3-5e4104d93ece"
title: "ESXi - Avoslocker enumerates VMs and forcefully kills VMs"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "189f7d6e-9442-4160-9bc3-5e4104d93ece"
  - "ESXi - Avoslocker enumerates VMs and forcefully kills VMs"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ESXi - Avoslocker enumerates VMs and forcefully kills VMs

Avoslocker malware has inbuilt functionality to enumerate the VM instances and uses the esxcli command to forcefully power off them.
[Reference](https://blogs.vmware.com/security/2022/02/avoslocker-modern-linux-ransomware-threats.html)

## Metadata

- Atomic GUID: 189f7d6e-9442-4160-9bc3-5e4104d93ece
- Technique: T1529: System Shutdown/Reboot
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1529/T1529.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Input Arguments

### cli_script

- description: Path to text with commands
- type: path
- default: PathToAtomicsFolder\T1529\src\esx_avoslocker_kill_vm.txt

### plink_file

- description: Path to plink
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\plink.exe

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

Check if plink is available.

### Prerequisite Check

```powershell
if (Test-Path "#{plink_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe" -OutFile "#{plink_file}"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
echo "" | "#{plink_file}" "#{vm_host}" -ssh  -l "#{vm_user}" -pw "#{vm_pass}" -m "#{cli_script}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
