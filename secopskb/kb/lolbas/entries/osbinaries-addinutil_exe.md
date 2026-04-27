---
title: "AddinUtil.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Addinutil.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Addinutil.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "AddinUtil.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AddinUtil.exe

.NET Tool used for updating cache files for Microsoft Office Add-Ins.

## Metadata

- Category: OSBinaries
- Created: 2023-10-05
- Author: Michael McKinley @MckinleyMike
- Source Path: yml/OSBinaries/Addinutil.yml

## Paths

- `C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe`
- `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\AddinUtil.exe`
- `C:\Windows\Microsoft.NET\Framework\v3.5\AddInUtil.exe`
- `C:\Windows\Microsoft.NET\Framework64\v3.5\AddInUtil.exe`

## Commands

### 1. Execute

AddinUtil is executed from the directory where the 'Addins.Store' payload exists, AddinUtil will execute the 'Addins.Store' payload.

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe -AddinRoot:.
```

- Use Case: Proxy execution of malicious serialized payload
- Privileges: User
- Operating System: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_suspicious_cmdline.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_child_process.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_cmdline.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_dir_exec.yml

## Resources

- {'Link': 'https://www.blue-prints.blog/content/blog/posts/lolbin/addinutil-lolbas.html'}

## Acknowledgements

- {'Person': 'Michael McKinley', 'Handle': '@MckinleyMike'}
- {'Person': 'Tony Latteri', 'Handle': '@TheLatteri'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Addinutil.yml)
