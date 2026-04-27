---
title: "ntdsutil.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Ntdsutil.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Ntdsutil.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "ntdsutil.exe"
functions:
  - "Dump"
attack_technique_ids:
  - "T1003.003"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Command line utility used to export Active Directory.

## Paths

- `C:\Windows\System32\ntdsutil.exe`

## Commands

### 1. Dump

Dump NTDS.dit into folder

```cmd
ntdsutil.exe "ac i ntds" "ifm" "create full c:\" q q
```

- Use Case: Dumping of Active Directory NTDS.dit database
- Privileges: Administrator
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_ntdsutil_usage.yml
- Splunk: https://github.com/splunk/security_content/blob/2b87b26bdc2a84b65b1355ffbd5174bdbdb1879c/detections/endpoint/ntdsutil_export_ntds.yml
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- IOC: ntdsutil.exe with command line including "ifm"

## Resources

- {'Link': 'https://adsecurity.org/?p=2398#CreateIFM'}

## Acknowledgements

- {'Person': 'Sean Metcalf', 'Handle': '@PyroTek3'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Ntdsutil.yml)
