---
atomic_guid: "cfdc954d-4bb0-4027-875b-a1893ce406f2"
title: "Create shortcut to cmd in startup folders"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.009"
attack_technique_name: "Boot or Logon Autostart Execution: Shortcut Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.009/T1547.009.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "cfdc954d-4bb0-4027-875b-a1893ce406f2"
  - "Create shortcut to cmd in startup folders"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create shortcut to cmd in startup folders

LNK file to launch CMD placed in startup folder. Upon execution, open File Explorer and browse to "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\"
to view the new shortcut.

## Metadata

- Atomic GUID: cfdc954d-4bb0-4027-875b-a1893ce406f2
- Technique: T1547.009: Boot or Logon Autostart Execution: Shortcut Modification
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1547.009/T1547.009.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.009]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$Shell = New-Object -ComObject ("WScript.Shell")
$ShortCut = $Shell.CreateShortcut("$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\T1547.009.lnk")
$ShortCut.TargetPath="cmd.exe"
$ShortCut.WorkingDirectory = "C:\Windows\System32";
$ShortCut.WindowStyle = 1;
$ShortCut.Description = "T1547.009.";
$ShortCut.Save()

$Shell = New-Object -ComObject ("WScript.Shell")
$ShortCut = $Shell.CreateShortcut("$env:ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\T1547.009.lnk")
$ShortCut.TargetPath="cmd.exe"
$ShortCut.WorkingDirectory = "C:\Windows\System32";
$ShortCut.WindowStyle = 1;
$ShortCut.Description = "T1547.009.";
$ShortCut.Save()
```

### Cleanup

```powershell
Remove-Item "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\T1547.009.lnk" -ErrorAction Ignore
Remove-Item "$env:ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\T1547.009.lnk" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.009/T1547.009.yaml)
