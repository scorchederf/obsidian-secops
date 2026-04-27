---
title: "rcsi.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Rcsi.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Rcsi.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "rcsi.exe"
functions:
  - "Execute"
  - "AWL Bypass"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# rcsi.exe

Non-Interactive command line inerface included with Visual Studio.

## Metadata

- Category: OtherMSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OtherMSBinaries/Rcsi.yml

## Paths

- `no default`

## Commands

### 1. Execute

Use embedded C# within the csx script to execute the code.

```cmd
rcsi.exe {PATH:.csx}
```

- Use Case: Local execution of arbitrary C# code stored in local CSX file.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

### 2. AWL Bypass

Use embedded C# within the csx script to execute the code.

```cmd
rcsi.exe {PATH:.csx}
```

- Use Case: Local execution of arbitrary C# code stored in local CSX file.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- BlockRule: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml

## Resources

- {'Link': 'https://enigma0x3.net/2016/11/21/bypassing-application-whitelisting-by-using-rcsi-exe/'}

## Acknowledgements

- {'Person': 'Matt Nelson', 'Handle': '@enigma0x3'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Rcsi.yml)
