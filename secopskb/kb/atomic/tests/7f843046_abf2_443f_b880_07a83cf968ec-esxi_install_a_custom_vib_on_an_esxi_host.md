---
atomic_guid: "7f843046-abf2-443f-b880-07a83cf968ec"
title: "ESXi - Install a custom VIB on an ESXi host"
framework: "atomic"
generated: "true"
attack_technique_id: "T1129"
attack_technique_name: "Server Software Component"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1129/T1129.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "7f843046-abf2-443f-b880-07a83cf968ec"
  - "ESXi - Install a custom VIB on an ESXi host"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ESXi - Install a custom VIB on an ESXi host

An adversary can maintain persistence within an ESXi host by installing malicious vSphere Installation Bundles (VIBs).
[Reference](https://www.mandiant.com/resources/blog/esxi-hypervisors-malware-persistence)

## Metadata

- Atomic GUID: 7f843046-abf2-443f-b880-07a83cf968ec
- Technique: T1129: Server Software Component
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1129/T1129.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1129-shared_modules|T1129]]

## Input Arguments

### plink_file

- description: Path to plink
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\plink.exe

### pscp_file

- description: Path to Pscp
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\pscp.exe

### vib_file

- description: Path to the dummy vib
- type: path
- default: PathToAtomicsFolder\..\atomics\T1129\src\atomicvibes.vib

### vib_install

- description: Path to script with commands to install the vib
- type: path
- default: PathToAtomicsFolder\..\atomics\T1129\src\esxi_vibinstall.txt

### vib_remove

- description: Path to script with commands to remove the vib
- type: path
- default: PathToAtomicsFolder\..\atomics\T1129\src\esxi_vibremove.txt

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

Check if plink and pscp are available.

### Prerequisite Check

```powershell
if (Test-Path "#{plink_file}") {exit 0} else {exit 1}
if (Test-Path "#{pscp_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\plink.exe"
Invoke-WebRequest "https://the.earth.li/~sgtatham/putty/latest/w64/pscp.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\pscp.exe"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
#{pscp_file} -pw #{vm_pass} #{vib_file} #{vm_user}@#{vm_host}:/tmp
echo "" | "#{plink_file}" "#{vm_host}" -ssh  -l "#{vm_user}" -pw "#{vm_pass}" -m "#{vib_install}"
```

### Cleanup

```cmd
echo "" | "#{plink_file}" "#{vm_host}" -ssh  -l "#{vm_user}" -pw "#{vm_pass}" -m "#{vib_remove}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1129/T1129.yaml)
