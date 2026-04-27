---
title: "wuauclt.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Wuauclt.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Wuauclt.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "wuauclt.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# wuauclt.exe

Windows Update Client

## Metadata

- Category: OSBinaries
- Created: 2020-09-23
- Author: David Middlehurst
- Source Path: yml/OSBinaries/Wuauclt.yml

## Paths

- `C:\Windows\System32\wuauclt.exe`
- `C:\Windows\UUS\amd64\wuauclt.exe`

## Commands

### 1. Execute

Loads and executes DLL code on attach.

```cmd
wuauclt.exe /UpdateDeploymentProvider {PATH_ABSOLUTE:.dll} /RunHandlerComServer
```

- Use Case: Execute dll via attach/detach methods
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/network_connection/net_connection_win_wuauclt_network_connection.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_wuauclt.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wuauclt_execution.yml
- IOC: wuauclt run with a parameter of a DLL path
- IOC: Suspicious wuauclt Internet/network connections

## Resources

- {'Link': 'https://dtm.uk/wuauclt/'}

## Acknowledgements

- {'Person': 'David Middlehurst', 'Handle': '@dtmsecurity'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Wuauclt.yml)
