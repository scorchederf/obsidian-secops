---
title: "AgentExecutor.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Agentexecutor.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Agentexecutor.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "AgentExecutor.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AgentExecutor.exe

Intune Management Extension included on Intune Managed Devices

## Metadata

- Category: OtherMSBinaries
- Created: 2020-07-23
- Author: Eleftherios Panos
- Source Path: yml/OtherMSBinaries/Agentexecutor.yml

## Paths

- `C:\Program Files (x86)\Microsoft Intune Management Extension\AgentExecutor.exe`

## Commands

### 1. Execute

Spawns powershell.exe and executes a provided powershell script with ExecutionPolicy Bypass argument

```cmd
AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}" "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}" 60000 "C:\Windows\SysWOW64\WindowsPowerShell\v1.0" 0 1
```

- Use Case: Execute unsigned powershell scripts
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 2. Execute

If we place a binary named powershell.exe in the specified folder path, agentexecutor.exe will execute it successfully

```cmd
AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}" "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}" 60000 "{PATH_ABSOLUTE:folder}" 0 1
```

- Use Case: Execute a provided EXE
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_agentexecutor.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_agentexecutor_susp_usage.yml

## Acknowledgements

- {'Person': 'Eleftherios Panos', 'Handle': '@lefterispan'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Agentexecutor.yml)
