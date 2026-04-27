---
title: "Tttracer.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Tttracer.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Tttracer.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Tttracer.exe"
functions:
  - "Execute"
  - "Dump"
attack_technique_ids:
  - "T1127"
  - "T1003"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Tttracer.exe

Used by Windows 1809 and newer to Debug Time Travel

## Metadata

- Category: OSBinaries
- Created: 2019-11-05
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Tttracer.yml

## Paths

- `C:\Windows\System32\tttracer.exe`
- `C:\Windows\SysWOW64\tttracer.exe`

## Commands

### 1. Execute

Execute specified executable from tttracer.exe. Requires administrator privileges.

```cmd
tttracer.exe {PATH_ABSOLUTE:.exe}
```

- Use Case: Spawn process using other binary
- Privileges: Administrator
- Operating System: Windows 10 1809 and newer, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

### 2. Dump

Dumps process using tttracer.exe. Requires administrator privileges

```cmd
TTTracer.exe -dumpFull -attach {PID}
```

- Use Case: Dump process by PID
- Privileges: Administrator
- Operating System: Windows 10 1809 and newer, Windows 11
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_tttracer_mod_load.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/image_load/image_load_tttracer_mod_load.yml
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- IOC: Parent child relationship. Tttracer parent for executed command

## Resources

- {'Link': 'https://twitter.com/oulusoyum/status/1191329746069655553'}
- {'Link': 'https://twitter.com/mattifestation/status/1196390321783025666'}
- {'Link': 'https://lists.samba.org/archive/cifs-protocol/2016-April/002877.html'}

## Acknowledgements

- {'Person': 'Onur Ulusoy', 'Handle': '@oulusoyum'}
- {'Person': 'Matt Graeber', 'Handle': '@mattifestation'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Tttracer.yml)
