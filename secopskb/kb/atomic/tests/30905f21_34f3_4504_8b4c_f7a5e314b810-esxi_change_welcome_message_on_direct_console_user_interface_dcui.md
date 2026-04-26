---
atomic_guid: "30905f21-34f3-4504-8b4c-f7a5e314b810"
title: "ESXi - Change Welcome Message on Direct Console User Interface (DCUI)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1491.001"
attack_technique_name: "Defacement: Internal Defacement"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1491.001/T1491.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "30905f21-34f3-4504-8b4c-f7a5e314b810"
  - "ESXi - Change Welcome Message on Direct Console User Interface (DCUI)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ESXi - Change Welcome Message on Direct Console User Interface (DCUI)

Changes the ESXi welcome message to potentially display ransom information.
[Reference](https://lolesxi-project.github.io/LOLESXi/lolesxi/Binaries/esxcli/#change%20display%20information)

## Metadata

- Atomic GUID: 30905f21-34f3-4504-8b4c-f7a5e314b810
- Technique: T1491.001: Defacement: Internal Defacement
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1491.001/T1491.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1491-defacement|T1491.001]]

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
echo "" | "#{plink_file}" -batch "#{vm_host}" -ssh -l #{vm_user} -pw "#{vm_pass}" "esxcli system welcomemsg set -m 'RANSOMWARE-NOTIFICATION'"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1491.001/T1491.001.yaml)
