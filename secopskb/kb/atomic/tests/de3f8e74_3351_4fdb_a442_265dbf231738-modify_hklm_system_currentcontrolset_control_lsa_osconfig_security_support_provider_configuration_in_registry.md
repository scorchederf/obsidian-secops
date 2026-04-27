---
atomic_guid: "de3f8e74-3351-4fdb-a442-265dbf231738"
title: "Modify HKLM:\\System\\CurrentControlSet\\Control\\Lsa\\OSConfig Security Support Provider configuration in registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.005"
attack_technique_name: "Boot or Logon Autostart Execution: Security Support Provider"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.005/T1547.005.yaml"
build_date: "2026-04-27 19:12:27"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Add a value to a Windows registry SSP key, simulating an adversarial modification of those keys.

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547005-security-support-provider|T1547.005: Security Support Provider]]

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
