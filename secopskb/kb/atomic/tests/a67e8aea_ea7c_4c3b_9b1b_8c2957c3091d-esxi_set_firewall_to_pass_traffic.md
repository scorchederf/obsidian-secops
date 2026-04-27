---
atomic_guid: "a67e8aea-ea7c-4c3b-9b1b-8c2957c3091d"
title: "ESXi - Set Firewall to PASS Traffic"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "a67e8aea-ea7c-4c3b-9b1b-8c2957c3091d"
  - "ESXi - Set Firewall to PASS Traffic"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ESXi - Set Firewall to PASS Traffic

This test sets the default ESXi firewall action to PASS instead of DROP. This allows all incoming and outgoing traffic.

## Metadata

- Atomic GUID: a67e8aea-ea7c-4c3b-9b1b-8c2957c3091d
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

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

The plink executable must be found in the ExternalPayloads folder.

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
echo "" | "#{plink_file}" -batch "#{vm_host}" -ssh -l #{vm_user} -pw "#{vm_pass}" "esxcli network firewall set --default-action true"
```

### Cleanup

```cmd
echo "" | "#{plink_file}" -batch "#{vm_host}" -ssh -l #{vm_user} -pw "#{vm_pass}" "esxcli network firewall set --default-action false"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
