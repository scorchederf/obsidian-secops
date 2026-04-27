---
title: "Runonce.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Runonce.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Runonce.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Runonce.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Runonce.exe

Executes a Run Once Task that has been configured in the registry

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Runonce.yml

## Paths

- `C:\Windows\System32\runonce.exe`
- `C:\Windows\SysWOW64\runonce.exe`

## Commands

### 1. Execute

Executes a Run Once Task that has been configured in the registry.

```cmd
Runonce.exe /AlternateShellStartup
```

- Use Case: Persistence, bypassing defensive counter measures
- Privileges: Administrator
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/registry/registry_event/registry_event_runonce_persistence.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_runonce_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/2926e98c5d998706ef7e248a63fb0367c841f685/rules/windows/persistence_run_key_and_startup_broad.toml
- IOC: Registy key add - HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\YOURKEY

## Resources

- {'Link': 'https://twitter.com/pabraeken/status/990717080805789697'}
- {'Link': 'https://cmatskas.com/configure-a-runonce-task-on-windows/'}

## Acknowledgements

- {'Person': 'Pierre-Alexandre Braeken', 'Handle': '@pabraeken'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Runonce.yml)
