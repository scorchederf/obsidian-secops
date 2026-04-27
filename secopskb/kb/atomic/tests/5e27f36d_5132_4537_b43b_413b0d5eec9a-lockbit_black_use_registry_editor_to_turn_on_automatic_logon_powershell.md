---
atomic_guid: "5e27f36d-5132-4537-b43b-413b0d5eec9a"
title: "Lockbit Black - Use Registry Editor to turn on automatic logon -Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "5e27f36d-5132-4537-b43b-413b0d5eec9a"
  - "Lockbit Black - Use Registry Editor to turn on automatic logon -Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Lockbit Black - Use Registry Editor to turn on automatic logon -Powershell

Lockbit Black - Use Registry Editor to turn on automatic logon

## Metadata

- Atomic GUID: 5e27f36d-5132-4537-b43b-413b0d5eec9a
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name AutoAdminLogon -PropertyType DWord -Value 1 -Force
New-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name DefaultUserName -Value Administrator -Force
New-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name DefaultDomainName -Value contoso.com -Force
New-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name DefaultPassword  -Value password1 -Force
```

### Cleanup

```powershell
Remove-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name AutoAdminLogon -Force -ErrorAction Ignore
Remove-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name DefaultUserName -Force -ErrorAction Ignore
Remove-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name DefaultDomainName -Force -ErrorAction Ignore
Remove-ItemProperty "HKLM:\Software\Policies\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name DefaultPassword -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
