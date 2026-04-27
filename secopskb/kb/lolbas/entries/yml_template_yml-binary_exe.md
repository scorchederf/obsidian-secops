---
title: "Binary.exe"
framework: "lolbas"
generated: "true"
source_path: "YML-Template.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/YML-Template.yml"
build_date: "2026-04-27 18:39:01"
category: "YML-Template.yml"
aliases:
  - "Binary.exe"
functions:
  - "Execute"
  - "AWL Bypass"
attack_technique_ids:
  - "T1055"
  - "T1033"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Binary.exe

Something general about the binary

## Metadata

- Category: YML-Template.yml
- Created: 1970-01-01
- Author: The name of the person that created this file
- Source Path: YML-Template.yml

## Paths

- `c:\windows\system32\bin.exe`
- `c:\windows\syswow64\bin.exe`

## Commands

### 1. Execute

Description of the command

```cmd
The command
```

- Use Case: A description of the usecase
- Privileges: Required privs
- Operating System: Windows 10 1803, Windows 10 1703
- ATT&CK: [[kb/attack/techniques/T1055-process_injection|T1055]]

### 2. AWL Bypass

Description of the second command

```cmd
The second command
```

- Use Case: A description of the usecase
- Privileges: Required privs
- Operating System: Windows 10 All
- ATT&CK: [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detections

- IOC: Event ID 10
- IOC: binary.exe spawned
- Analysis: https://example.com/to/blog/gist/writeup/if/applicable
- Sigma: https://example.com/to/sigma/rule/if/applicable
- Elastic: https://example.com/to/elastic/rule/if/applicable
- Splunk: https://example.com/to/splunk/rule/if/applicable
- BlockRule: https://example.com/to/microsoft/block/rules/if/applicable

## Resources

- {'Link': 'http://blogpost.com'}
- {'Link': 'http://twitter.com/something'}
- {'Link': 'http://example.com/Threatintelreport'}

## Acknowledgements

- {'Person': 'John Doe', 'Handle': '@johndoe'}
- {'Person': 'Ola Norman', 'Handle': '@olaNor'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/YML-Template.yml)
