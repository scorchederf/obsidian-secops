---
title: "Verclsid.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Verclsid.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Verclsid.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Verclsid.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.012"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Verclsid.exe

Used to verify a COM object before it is instantiated by Windows Explorer

## Metadata

- Category: OSBinaries
- Created: 2018-12-04
- Author: @bohops
- Source Path: yml/OSBinaries/Verclsid.yml

## Paths

- `C:\Windows\System32\verclsid.exe`
- `C:\Windows\SysWOW64\verclsid.exe`

## Commands

### 1. Execute

Used to verify a COM object before it is instantiated by Windows Explorer

```cmd
verclsid.exe /S /C {CLSID}
```

- Use Case: Run a COM object created in registry to evade defensive counter measures
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.012]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_verclsid_runs_com.yml
- Splunk: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/verclsid_clsid_execution.yml

## Resources

- {'Link': 'https://gist.github.com/NickTyrer/0598b60112eaafe6d07789f7964290d5'}
- {'Link': 'https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/'}

## Acknowledgements

- {'Person': 'Nick Tyrer', 'Handle': '@NickTyrer'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Verclsid.yml)
