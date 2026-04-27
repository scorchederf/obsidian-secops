---
title: "iediagcmd.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Iediagcmd.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Iediagcmd.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "iediagcmd.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Diagnostics Utility for Internet Explorer

## Paths

- `C:\Program Files\Internet Explorer\iediagcmd.exe`

## Commands

### 1. Execute

Executes binary that is pre-planted at C:\test\system32\netsh.exe.

```cmd
set windir=c:\test& cd "C:\Program Files\Internet Explorer\" & iediagcmd.exe /out:{PATH_ABSOLUTE:.cab}
```

- Use Case: Spawn a pre-planted executable from iediagcmd.exe.
- Privileges: User
- Operating System: Windows 10 1803, Windows 10 1703, Windows 10 22H1, Windows 10 22H2, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/manasmbellani/mycode_public/blob/master/sigma/rules/win_proc_creation_lolbin_iediagcmd.yml
- IOC: Sysmon Event ID 1
- IOC: Execution of process iediagcmd.exe with /out could be suspicious

## Resources

- {'Link': 'https://twitter.com/Hexacorn/status/1507516393859731456'}

## Acknowledgements

- {'Person': 'Adam', 'Handle': '@hexacorn'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Iediagcmd.yml)
