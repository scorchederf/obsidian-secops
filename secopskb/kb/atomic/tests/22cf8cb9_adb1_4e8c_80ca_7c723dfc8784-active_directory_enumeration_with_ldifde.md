---
atomic_guid: "22cf8cb9-adb1-4e8c-80ca-7c723dfc8784"
title: "Active Directory Enumeration with LDIFDE"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.002"
attack_technique_name: "Permission Groups Discovery: Domain Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "22cf8cb9-adb1-4e8c-80ca-7c723dfc8784"
  - "Active Directory Enumeration with LDIFDE"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Output information from Active Directory to a specified file. [Ldifde](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc731033(v=ws.11)) is a CLI tool for creating, modifying and deleting directory objects.
The test is derived from the CISA Report on Voly Typhoon. Reference: https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]

## Input Arguments

### output_file

- description: The filename to be created by ldifde
- type: string
- default: atomic_ldifde.txt

### output_path

- description: Path to the file that ldifde will output
- type: path
- default: C:\Windows\temp

## Dependencies

PowerShell ActiveDirectory Module must be installed

### Prerequisite Check

```powershell
Try {
    Import-Module ActiveDirectory -ErrorAction Stop | Out-Null
    exit 0
}
Catch {
    exit 1
}
```

### Get Prerequisite

```powershell
if((Get-CimInstance -ClassName Win32_OperatingSystem).ProductType -eq 1) {
  Add-WindowsCapability -Name (Get-WindowsCapability -Name RSAT.ActiveDirectory.DS* -Online).Name -Online
} else {
  Install-WindowsFeature RSAT-AD-PowerShell
}
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
ldifde.exe -f #{output_path}\#{output_file} -p subtree
```

### Cleanup

```cmd
del #{output_path}\#{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml)
