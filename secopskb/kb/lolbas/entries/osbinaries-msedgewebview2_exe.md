---
title: "msedgewebview2.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/msedgewebview2.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/msedgewebview2.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "msedgewebview2.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.015"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# msedgewebview2.exe

msedgewebview2.exe is the executable file for Microsoft Edge WebView2, which is a web browser control used by applications to display web content.

## Metadata

- Category: OSBinaries
- Created: 2023-06-15
- Author: Matan Bahar
- Source Path: yml/OSBinaries/msedgewebview2.yml

## Paths

- `C:\Program Files (x86)\Microsoft\Edge\Application\114.0.1823.43\msedgewebview2.exe`
- `C:\Program Files (x86)\Microsoft\EdgeWebView\Application\131.0.2903.70\msedgewebview2.exe`

## Commands

### 1. Execute

This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified executable as its subprocess.

```cmd
msedgewebview2.exe --no-sandbox --browser-subprocess-path="{PATH_ABSOLUTE:.exe}"
```

- Use Case: Proxy execution of binary
- Privileges: Low privileges
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.015]]

### 2. Execute

This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified command as its subprocess.

```cmd
msedgewebview2.exe --utility-cmd-prefix="{CMD}"
```

- Use Case: Proxy execution of binary
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.015]]

### 3. Execute

This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified command as its subprocess.

```cmd
msedgewebview2.exe --disable-gpu-sandbox --gpu-launcher="{CMD}"
```

- Use Case: Proxy execution of binary
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.015]]

### 4. Execute

This command launches the Microsoft Edge WebView2 browser control without sandboxing and will spawn the specified command as its subprocess.

```cmd
msedgewebview2.exe --no-sandbox --renderer-cmd-prefix="{CMD}"
```

- Use Case: Proxy execution of binary
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.015]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml
- IOC: msedgewebview2.exe spawned with any of the following: --gpu-launcher, --utility-cmd-prefix, --renderer-cmd-prefix, --browser-subprocess-path

## Resources

- {'Link': 'https://medium.com/@MalFuzzer/one-electron-to-rule-them-all-dc2e9b263daf'}

## Acknowledgements

- {'Person': 'Uriel Kosayev', 'Handle': '@MalFuzzer'}
- {'Person': 'Hai Vaknin', 'Handle': '@VakninHai'}
- {'Person': 'Tamir Yehuda', 'Handle': '@Tamirye94'}
- {'Person': 'Matan Bahar', 'Handle': '@Bl4ckShad3'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/msedgewebview2.yml)
