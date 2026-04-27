---
title: "Bcp.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Bcp.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Bcp.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Bcp.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Bcp.exe

Microsoft SQL Server Bulk Copy Program utility for importing and exporting data between SQL Server instances and data files.

## Metadata

- Category: OtherMSBinaries
- Created: 2025-11-13
- Author: Mahir Ali Khan
- Source Path: yml/OtherMSBinaries/Bcp.yml

## Paths

- `C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\bcp.exe`
- `C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\bcp.exe`
- `C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn\bcp.exe`
- `C:\Program Files (x86)\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\bcp.exe`
- `C:\Program Files (x86)\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\bcp.exe`
- `C:\Program Files (x86)\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn\bcp.exe`
- `C:\Program Files (x86)\Microsoft SQL Server\120\Tools\Binn\bcp.exe`

## Commands

### 1. Download

Export binary payload stored in SQL Server database to file system.

```cmd
bcp "SELECT payload_data FROM database.dbo.payloads WHERE id=1" queryout "C:\Windows\Temp\payload.exe" -S localhost -T -c
```

- Use Case: Extract malicious executable from database storage to local file system for execution.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- IOC: Process creation of bcp.exe with queryout or Out parameter
- IOC: bcp.exe writing executable files to temp or users directories
- IOC: Network connections from bcp.exe to SQL Server followed by file creation
- IOC: Event ID 4688 - Process creation for bcp.exe
- IOC: Event ID 4663 - File system access by bcp.exe
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bcp_export_data.yml

## Resources

- {'Link': 'https://docs.microsoft.com/en-us/sql/tools/bcp-utility'}
- {'Link': 'https://asec.ahnlab.com/en/61000/'}
- {'Link': 'https://asec.ahnlab.com/en/78944/'}
- {'Link': 'https://www.huntress.com/blog/attacking-mssql-servers'}
- {'Link': 'https://www.huntress.com/blog/attacking-mssql-servers-pt-ii'}
- {'Link': 'https://news.sophos.com/en-us/2024/08/07/sophos-mdr-hunt-tracks-mimic-ransomware-campaign-against-organizations-in-india/'}
- {'Link': 'https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/'}

## Acknowledgements

- {'Person': 'Mahir Ali Khan', 'Handle': '@mahiralikhan07'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Bcp.yml)
