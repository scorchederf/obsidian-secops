---
title: "Psr.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Psr.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Psr.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Psr.exe"
functions:
  - "Reconnaissance"
attack_technique_ids:
  - "T1113"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Psr.exe

Windows Problem Steps Recorder, used to record screen and clicks.

## Metadata

- Category: OSBinaries
- Created: 2020-06-27
- Author: Leon Rodenko
- Source Path: yml/OSBinaries/Psr.yml

## Paths

- `c:\windows\system32\psr.exe`
- `c:\windows\syswow64\psr.exe`

## Commands

### 1. Reconnaissance

Record a user screen without creating a GUI. You should use "psr.exe /stop" to stop recording and create output file.

```cmd
psr.exe /start /output {PATH_ABSOLUTE:.zip} /sc 1 /gui 0
```

- Use Case: Can be used to take screenshots of the user environment
- Privileges: User
- Operating System: since Windows 7 (client) / Windows 2008 R2
- ATT&CK: [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_psr_capture_screenshots.yml
- IOC: psr.exe spawned
- IOC: suspicious activity when running with "/gui 0" flag

## Resources

- {'Link': 'https://social.technet.microsoft.com/wiki/contents/articles/51722.windows-problem-steps-recorder-psr-quick-and-easy-documenting-of-your-steps-and-procedures.aspx'}

## Acknowledgements

- {'Person': 'Leon Rodenko', 'Handle': '@L3m0nada'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Psr.yml)
