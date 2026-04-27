---
title: "DefaultPack.EXE"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/DefaultPack.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/DefaultPack.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "DefaultPack.EXE"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# DefaultPack.EXE

This binary can be downloaded along side multiple software downloads on the Microsoft website. It gets downloaded when the user forgets to uncheck the option to set Bing as the default search provider.

## Metadata

- Category: OtherMSBinaries
- Created: 2020-10-01
- Author: @checkymander
- Source Path: yml/OtherMSBinaries/DefaultPack.yml

## Paths

- `C:\Program Files (x86)\Microsoft\DefaultPack\DefaultPack.exe`

## Commands

### 1. Execute

Use DefaultPack.EXE to execute arbitrary binaries, with added argument support.

```cmd
DefaultPack.EXE /C:"{CMD}"
```

- Use Case: Can be used to execute stagers, binaries, and other malicious commands.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_lolbin_defaultpack.yml
- IOC: DefaultPack.EXE spawned an unknown process

## Resources

- {'Link': 'https://twitter.com/checkymander/status/1311509470275604480.'}

## Acknowledgements

- {'Person': 'checkymander', 'Handle': '@checkymander'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/DefaultPack.yml)
