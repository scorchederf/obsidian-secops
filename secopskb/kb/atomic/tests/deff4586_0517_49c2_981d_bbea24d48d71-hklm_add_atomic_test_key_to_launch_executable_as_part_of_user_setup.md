---
atomic_guid: "deff4586-0517-49c2-981d-bbea24d48d71"
title: "HKLM - Add atomic_test key to launch executable as part of user setup"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.014"
attack_technique_name: "Active Setup"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.014/T1547.014.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "deff4586-0517-49c2-981d-bbea24d48d71"
  - "HKLM - Add atomic_test key to launch executable as part of user setup"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HKLM - Add atomic_test key to launch executable as part of user setup

This test will create an "atomic_test" key under 'HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components' to launch calc by configuring an active setup executable and 
forcing to run active setup using the "runonce.exe /AlternateShellStartup" command. 
Without the "runonce.exe /AlternateShellStartup" command it would run during the next logon for each user.

Note: If you logout before running the cleanup command, you will be required to go through the OOBE (out-of-box experience) setup sequence to log back in. 
The payload will only run once unless the cleanup command is run in between tests.

[Active Setup Explained](https://helgeklein.com/blog/active-setup-explained/)

## Metadata

- Atomic GUID: deff4586-0517-49c2-981d-bbea24d48d71
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
New-Item "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components" -Name "atomic_test" -Force
Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\atomic_test" "(Default)" "ART TEST" -Force
Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\atomic_test" "StubPath" "#{payload}" -Force 
& $env:SYSTEMROOT\system32\runonce.exe /AlternateShellStartup
```

### Cleanup

```powershell
Remove-Item "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\atomic_test" -Force -ErrorAction Ignore
Remove-Item "HKCU:\SOFTWARE\Microsoft\Active Setup\Installed Components\atomic_test" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.014/T1547.014.yaml)
