---
title: "Eventvwr.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Eventvwr.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Eventvwr.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Eventvwr.exe"
functions:
  - "UAC Bypass"
attack_technique_ids:
  - "T1548.002"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Eventvwr.exe

Displays Windows Event Logs in a GUI window.

## Metadata

- Category: OSBinaries
- Created: 2018-11-01
- Author: Jacob Gajek
- Source Path: yml/OSBinaries/Eventvwr.yml

## Paths

- `C:\Windows\System32\eventvwr.exe`
- `C:\Windows\SysWOW64\eventvwr.exe`

## Commands

### 1. UAC Bypass

During startup, eventvwr.exe checks the registry value `HKCU\Software\Classes\mscfile\shell\open\command` for the location of mmc.exe, which is used to open the eventvwr.msc saved console file. If the location of another binary or script is added to this registry value, it will be executed as a high-integrity process without a UAC prompt being displayed to the user.

```cmd
eventvwr.exe
```

- Use Case: Execute a binary or script as a high-integrity process without a UAC prompt.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

### 2. UAC Bypass

During startup, eventvwr.exe uses .NET deserialization with `%LOCALAPPDATA%\Microsoft\EventV~1\RecentViews` file. This file can be created using https://github.com/pwntester/ysoserial.net

```cmd
ysoserial.exe -o raw -f BinaryFormatter - g DataSet -c "{CMD}" > RecentViews & copy RecentViews %LOCALAPPDATA%\Microsoft\EventV~1\RecentViews & eventvwr.exe
```

- Use Case: Execute a command to bypass security restrictions that limit the use of command-line interpreters.
- Privileges: Administrator
- Operating System: Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_uac_bypass_eventvwr.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/registry/registry_set/registry_set_uac_bypass_eventvwr.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/file/file_event/file_event_win_uac_bypass_eventvwr.yml
- Elastic: https://github.com/elastic/detection-rules/blob/d31ea6253ea40789b1fc49ade79b7ec92154d12a/rules/windows/privilege_escalation_uac_bypass_event_viewer.toml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/eventvwr_uac_bypass.yml
- IOC: eventvwr.exe launching child process other than mmc.exe
- IOC: Creation or modification of the registry value HKCU\Software\Classes\mscfile\shell\open\command

## Resources

- {'Link': 'https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/'}
- {'Link': 'https://github.com/enigma0x3/Misc-PowerShell-Stuff/blob/master/Invoke-EventVwrBypass.ps1'}
- {'Link': 'https://twitter.com/orange_8361/status/1518970259868626944'}

## Acknowledgements

- {'Person': 'Matt Nelson', 'Handle': '@enigma0x3'}
- {'Person': 'Matt Graeber', 'Handle': '@mattifestation'}
- {'Person': 'Orange Tsai', 'Handle': '@orange_8361'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Eventvwr.yml)
