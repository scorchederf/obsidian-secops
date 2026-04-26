---
atomic_guid: "04d55cef-f283-40ba-ae2a-316bc3b5e78c"
title: "HKLM - re-execute 'Internet Explorer Core Fonts' StubPath payload by decreasing version number"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.014"
attack_technique_name: "Active Setup"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.014/T1547.014.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "04d55cef-f283-40ba-ae2a-316bc3b5e78c"
  - "HKLM - re-execute 'Internet Explorer Core Fonts' StubPath payload by decreasing version number"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HKLM - re-execute 'Internet Explorer Core Fonts' StubPath payload by decreasing version number

This test will decrease the version number of the 'Internet Explorer Core Fonts' (UUID {C9E9A340-D1F1-11D0-821E-444553540600}) registry key for the current user, 
which will force the StubPath payload (if set) to execute.

## Metadata

- Atomic GUID: 04d55cef-f283-40ba-ae2a-316bc3b5e78c
- Technique: T1547.014: Active Setup
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1547.014/T1547.014.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.014]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Active Setup\Installed Components\{C9E9A340-D1F1-11D0-821E-444553540600}" -Name "Version" -Value "0,0,0,0"
& $env:SYSTEMROOT\system32\runonce.exe /AlternateShellStartup
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.014/T1547.014.yaml)
