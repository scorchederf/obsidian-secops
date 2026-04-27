---
title: "Procdump.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Procdump.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Procdump.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Procdump.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Procdump.exe

SysInternals Memory Dump Tool

## Metadata

- Category: OtherMSBinaries
- Created: 2020-10-14
- Author: Alfie Champion (@ajpc500)
- Source Path: yml/OtherMSBinaries/Procdump.yml

## Paths

- `no default`

## Commands

### 1. Execute

Loads the specified DLL where DLL is configured with a 'MiniDumpCallbackRoutine' exported function. Valid process must be provided as dump still created.

```cmd
procdump.exe -md {PATH:.dll} explorer.exe
```

- Use Case: Performs execution of unsigned DLL.
- Privileges: User
- Operating System: Windows 8.1 and higher, Windows Server 2012 and higher
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

### 2. Execute

Loads the specified DLL where configured with DLL_PROCESS_ATTACH execution, process argument can be arbitrary.

```cmd
procdump.exe -md {PATH:.dll} foobar
```

- Use Case: Performs execution of unsigned DLL.
- Privileges: User
- Operating System: Windows 8.1 and higher, Windows Server 2012 and higher
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_renamed_sysinternals_procdump.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_sysinternals_procdump.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/dump_lsass_via_procdump.yml
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- IOC: Process creation with given '-md' parameter
- IOC: Anomalous child processes of procdump
- IOC: Unsigned DLL load via procdump.exe or procdump64.exe

## Resources

- {'Link': 'https://twitter.com/ajpc500/status/1448588362382778372?s=20'}

## Acknowledgements

- {'Person': 'Alfie Champion', 'Handle': '@ajpc500'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Procdump.yml)
