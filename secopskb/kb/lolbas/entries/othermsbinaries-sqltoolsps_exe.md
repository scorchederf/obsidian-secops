---
title: "SQLToolsPS.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Sqltoolsps.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Sqltoolsps.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "SQLToolsPS.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# SQLToolsPS.exe

Tool included with Microsoft SQL that loads SQL Server cmdlts. A replacement for sqlps.exe. Successor to sqlps.exe in SQL Server 2016+.

## Metadata

- Category: OtherMSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OtherMSBinaries/Sqltoolsps.yml

## Paths

- `C:\Program files (x86)\Microsoft SQL Server\130\Tools\Binn\sqlps.exe`

## Commands

### 1. Execute

Run a SQL Server PowerShell mini-console without Module and ScriptBlock Logging.

```cmd
SQLToolsPS.exe -noprofile -command Start-Process {PATH:.exe}
```

- Use Case: Execute PowerShell command.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_mssql_sqltoolsps_susp_execution.yml
- Splunk: https://github.com/splunk/security_content/blob/aa9f7e0d13a61626c69367290ed1b7b71d1281fd/docs/_posts/2021-10-05-suspicious_copy_on_system32.md

## Resources

- {'Link': 'https://twitter.com/pabraeken/status/993298228840992768'}
- {'Link': 'https://docs.microsoft.com/en-us/sql/powershell/sql-server-powershell?view=sql-server-2017'}

## Acknowledgements

- {'Person': 'Pierre-Alexandre Braeken', 'Handle': '@pabraeken'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Sqltoolsps.yml)
