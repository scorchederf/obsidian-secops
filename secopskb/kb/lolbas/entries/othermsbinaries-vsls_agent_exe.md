---
title: "vsls-agent.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/vsls-agent.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/vsls-agent.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "vsls-agent.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Agent for Visual Studio Live Share (Code Collaboration)

## Paths

- `c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\Extensions\Microsoft\LiveShare\Agent\vsls-agent.exe`

## Commands

### 1. Execute

Load a library payload using the --agentExtensionPath parameter (32-bit)

```cmd
vsls-agent.exe --agentExtensionPath {PATH_ABSOLUTE:.dll}
```

- Use Case: Execute proxied payload with Microsoft signed binary
- Privileges: User
- Operating System: Windows 10 21H2 (likely previous and newer versions with modern versions of Visual Studio installed)
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_vslsagent_agentextensionpath_load.yml

## Resources

- {'Link': 'https://twitter.com/bohops/status/1583916360404729857'}

## Acknowledgements

- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/vsls-agent.yml)
