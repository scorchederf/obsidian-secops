---
atomic_guid: "280812c8-4dae-43e9-a74e-1d08ab997c0e"
title: "ESXi - Enable SSH via VIM-CMD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.004"
attack_technique_name: "Remote Services: SSH"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.004/T1021.004.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "280812c8-4dae-43e9-a74e-1d08ab997c0e"
  - "ESXi - Enable SSH via VIM-CMD"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ESXi - Enable SSH via VIM-CMD

An adversary enables SSH on an ESXi host to maintain persistence and creeate another command execution interface.
[Reference](https://lolesxi-project.github.io/LOLESXi/lolesxi/Binaries/vim-cmd/#enable%20service)

## Metadata

- Atomic GUID: 280812c8-4dae-43e9-a74e-1d08ab997c0e
- Technique: T1021.004: Remote Services: SSH
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1021.004/T1021.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.004]]

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

```text
if (Test-Path "#{plink_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe" -OutFile "#{plink_file}"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```commandprompt
echo "" | "#{plink_file}" -batch "#{vm_host}" -ssh -l #{vm_user} -pw "#{vm_pass}" "vim-cmd hostsvc/enable_ssh"
```

### Cleanup

```commandprompt
echo "" | "#{plink_file}" -batch "#{vm_host}" -ssh -l #{vm_user} -pw "#{vm_pass}" "vim-cmd hostsvc/disable_ssh"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.004/T1021.004.yaml)
