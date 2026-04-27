---
atomic_guid: "7a714703-9f6b-461c-b06d-e6aeac650f27"
title: "Google Chrome Load Unpacked Extension With Command Line"
framework: "atomic"
generated: "true"
attack_technique_id: "T1176"
attack_technique_name: "Browser Extensions"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1176/T1176.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "7a714703-9f6b-461c-b06d-e6aeac650f27"
  - "Google Chrome Load Unpacked Extension With Command Line"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Google Chrome Load Unpacked Extension With Command Line

This test loads an unpacked extension in Google Chrome with the `--load-extension` parameter. This technique was previously used by the Grandoreiro malware to load a malicious extension that would capture the browsing history, steal cookies and other user information. Other malwares also leverage this technique to hijack searches, steal passwords, inject ads, and more.

References:
https://attack.mitre.org/techniques/T1176/
https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/

## Metadata

- Atomic GUID: 7a714703-9f6b-461c-b06d-e6aeac650f27
- Technique: T1176: Browser Extensions
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1176/T1176.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1176-software_extensions|T1176]]

## Input Arguments

### working_dir

- description: Working directory where the files will be downloaded and extracted
- type: string
- default: $env:TEMP

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell

# Chromium
$chromium =  "https://commondatastorage.googleapis.com/chromium-browser-snapshots/Win_x64/1153778/chrome-win.zip"

# uBlock Origin Lite to test side-loading
$extension = "https://github.com/uBlockOrigin/uBOL-home/releases/download/uBOLite_2024.11.25.1376/uBOLite_2024.11.25.1376.chromium.mv3.zip"

Set-Location "#{working_dir}"

Set-Variable ProgressPreference SilentlyContinue
Invoke-WebRequest -URI $chromium -OutFile "#{working_dir}\chrome.zip"
Invoke-WebRequest -URI $extension -OutFile "#{working_dir}\extension.zip"


Expand-Archive chrome.zip -DestinationPath "#{working_dir}" -Force
Expand-Archive extension.zip -Force

Start-Process .\chrome-win\chrome.exe --load-extension="#{working_dir}\extension\" -PassThru
```

### Cleanup

```powershell
Set-Location "#{working_dir}"
Stop-Process -Name chrome -Force
Remove-Item .\chrome.zip, .\chrome-win, .\extension, .\extension.zip -Recurse -Force
Set-Variable ProgressPreference Continue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1176/T1176.yaml)
