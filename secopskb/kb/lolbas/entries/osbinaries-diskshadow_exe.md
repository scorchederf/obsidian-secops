---
title: "Diskshadow.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Diskshadow.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Diskshadow.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Diskshadow.exe"
functions:
  - "Dump"
  - "Execute"
attack_technique_ids:
  - "T1003.003"
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Diskshadow.exe is a tool that exposes the functionality offered by the volume shadow copy Service (VSS).

## Paths

- `C:\Windows\System32\diskshadow.exe`
- `C:\Windows\SysWOW64\diskshadow.exe`

## Commands

### 1. Dump

Execute commands using diskshadow.exe from a prepared diskshadow script.

```cmd
diskshadow.exe /s {PATH:.txt}
```

- Use Case: Use diskshadow to exfiltrate data from VSS such as NTDS.dit
- Privileges: User
- Operating System: Windows server
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

### 2. Execute

Execute commands using diskshadow.exe to spawn child process

```cmd
diskshadow> exec {PATH:.exe}
```

- Use Case: Use diskshadow to bypass defensive counter measures
- Privileges: User
- Operating System: Windows server
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diskshadow.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_shadow_copies_deletion.yml
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- IOC: Child process from diskshadow.exe

## Resources

- {'Link': 'https://bohops.com/2018/03/26/diskshadow-the-return-of-vss-evasion-persistence-and-active-directory-database-extraction/'}

## Acknowledgements

- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Diskshadow.yml)
