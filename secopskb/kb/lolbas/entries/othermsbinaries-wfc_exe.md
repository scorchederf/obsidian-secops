---
title: "Wfc.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Wfc.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Wfc.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Wfc.exe"
functions:
  - "AWL Bypass"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The Workflow Command-line Compiler tool is included with the Windows Software Development Kit (SDK).

## Paths

- `C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8 Tools\wfc.exe`

## Commands

### 1. AWL Bypass

Execute arbitrary C# code embedded in a XOML file.

```cmd
wfc.exe {PATH_ABSOLUTE:.xoml}
```

- Use Case: Execute proxied payload with Microsoft signed binary to bypass WDAC policies
- Privileges: User
- Operating System: Windows 10 2004 (likely previous and newer versions as well)
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_wfc.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious

## Resources

- {'Link': 'https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/'}

## Acknowledgements

- {'Person': 'Matt Graeber', 'Handle': '@mattifestation'}
- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Wfc.yml)
