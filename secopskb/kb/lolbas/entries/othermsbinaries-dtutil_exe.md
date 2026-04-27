---
title: "dtutil.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Dtutil.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Dtutil.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "dtutil.exe"
functions:
  - "Copy"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Microsoft command line utility used to manage SQL Server Integration Services packages.

## Paths

- `C:\Program Files\Microsoft SQL Server\<version>\DTS\Binn\dtutil.exe`
- `C:\Program Files (x86)\Microsoft SQL Server\<version>\DTS\Binn\dtutil.exe`

## Commands

### 1. Copy

Copy file from source to destination

```cmd
dtutil.exe /FILE {PATH_ABSOLUTE:.source.ext} /COPY FILE;{PATH_ABSOLUTE:.dest.ext}
```

- Use Case: Use to copies the source file to the destination file
- Privileges: Administrator
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/sql/integration-services/dtutil-utility?view=sql-server-ver16'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Dtutil.yml)
