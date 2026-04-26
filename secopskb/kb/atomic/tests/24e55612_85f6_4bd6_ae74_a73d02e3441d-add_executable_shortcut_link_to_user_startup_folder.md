---
atomic_guid: "24e55612-85f6-4bd6-ae74-a73d02e3441d"
title: "Add Executable Shortcut Link to User Startup Folder"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "24e55612-85f6-4bd6-ae74-a73d02e3441d"
  - "Add Executable Shortcut Link to User Startup Folder"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Add Executable Shortcut Link to User Startup Folder

Adds a non-malicious executable shortcut link to the current users startup directory. Test can be verified by going to the users startup directory and checking if the shortcut link exists.

## Metadata

- Atomic GUID: 24e55612-85f6-4bd6-ae74-a73d02e3441d
- Technique: T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1547.001/T1547.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$Target = "C:\Windows\System32\calc.exe"
$ShortcutLocation = "$home\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\calc_exe.lnk"
$WScriptShell = New-Object -ComObject WScript.Shell
$Create = $WScriptShell.CreateShortcut($ShortcutLocation)
$Create.TargetPath = $Target
$Create.Save()
```

### Cleanup

```powershell
Remove-Item "$home\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\calc_exe.lnk" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
