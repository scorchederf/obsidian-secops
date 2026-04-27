---
atomic_guid: "c510d25b-1667-467d-8331-a56d3e9bc4ff"
title: "Application uninstall using WMIC"
framework: "atomic"
generated: "true"
attack_technique_id: "T1047"
attack_technique_name: "Windows Management Instrumentation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "c510d25b-1667-467d-8331-a56d3e9bc4ff"
  - "Application uninstall using WMIC"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Emulates uninstalling  applications using WMIC.  This method only works if the product was installed with an msi file.  APTs have been seen using this to uninstall security products.

## ATT&CK Mapping

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]

## Input Arguments

### node

- description: Computer the action is being executed against but defaults to the localhost.
- type: string
- default: 127.0.0.1

### product

- description: Enter the product name being uninstalled.  This will default to TightVNC.
- type: string
- default: Tightvnc

## Dependencies

TightVNC must be installed.

### Prerequisite Check

```powershell
if ((Test-Path "C:\Program Files\TightVNC\tvnviewer.exe")-Or (Test-Path "C:\Program Files (x86)\TightVNC\tvnviewer.exe")) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest 'https://www.tightvnc.com/download/2.8.63/tightvnc-2.8.63-gpl-setup-64bit.msi' -OutFile "PathToAtomicsFolder\..\ExternalPayloads\tightvncinstaller.msi"
start-sleep -s 10
msiexec /i "PathToAtomicsFolder\..\ExternalPayloads\tightvncinstaller.msi" /qn /norestart
start-sleep -s 15
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
wmic /node:"#{node}" product where "name like '#{product}%%'" call uninstall
```

### Cleanup

```cmd
msiexec /i "PathToAtomicsFolder\..\ExternalPayloads\tightvncinstaller.msi" /qn /norestart
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml)
