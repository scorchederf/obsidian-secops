---
title: "Sqldumper.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Sqldumper.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Sqldumper.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Sqldumper.exe"
functions:
  - "Dump"
attack_technique_ids:
  - "T1003"
  - "T1003.001"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Debugging utility included with Microsoft SQL.

## Paths

- `C:\Program Files\Microsoft SQL Server\90\Shared\SQLDumper.exe`
- `C:\Program Files (x86)\Microsoft Office\root\vfs\ProgramFilesX86\Microsoft Analysis\AS OLEDB\140\SQLDumper.exe`
- `C:\Program Files\Microsoft Power BI Desktop\bin\SqlDumper.exe`

## Commands

### 1. Dump

Dump process by PID and create a dump file (Appears to create a dump file called SQLDmprXXXX.mdmp).

```cmd
sqldumper.exe 464 0 0x0110
```

- Use Case: Dump process using PID.
- Privileges: Administrator
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]

### 2. Dump

0x01100:40 flag will create a Mimikatz compatible dump file.

```cmd
sqldumper.exe 540 0 0x01100:40
```

- Use Case: Dump LSASS.exe to Mimikatz compatible dump using PID.
- Privileges: Administrator
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_susp_sqldumper_activity.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f6421d8c534f295518a2c945f530e8afc4c8ad1b/rules/windows/credential_access_lsass_memdump_file_created.toml
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml

## Resources

- {'Link': 'https://twitter.com/countuponsec/status/910969424215232518'}
- {'Link': 'https://twitter.com/countuponsec/status/910977826853068800'}
- {'Link': 'https://support.microsoft.com/en-us/help/917825/how-to-use-the-sqldumper-exe-utility-to-generate-a-dump-file-in-sql-se'}

## Acknowledgements

- {'Person': 'Luis Rocha', 'Handle': '@countuponsec'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Sqldumper.yml)
