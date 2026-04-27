---
atomic_guid: "4c8db261-a58b-42a6-a866-0a294deedde4"
title: "Running Chrome VPN Extensions via the Registry 2 vpn extension"
framework: "atomic"
generated: "true"
attack_technique_id: "T1133"
attack_technique_name: "External Remote Services"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1133/T1133.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "4c8db261-a58b-42a6-a866-0a294deedde4"
  - "Running Chrome VPN Extensions via the Registry 2 vpn extension"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Running Chrome VPN Extensions via the Registry 2 vpn extension

Running Chrome VPN Extensions via the Registry install 2 vpn extension, please see "T1133\src\list of vpn extension.txt" to view complete list

## Metadata

- Atomic GUID: 4c8db261-a58b-42a6-a866-0a294deedde4
- Technique: T1133: External Remote Services
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1133/T1133.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]

## Input Arguments

### chrome_url

- description: chrome installer download URL
- type: url
- default: https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BFD62DDBC-14C6-20BD-706F-C7744738E422%7D%26lang%3Den%26browser%3D3%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/chrome/install/ChromeStandaloneSetup64.exe

### extension_id

- description: chrome extension id
- type: string
- default: "fcfhplploccackoneaefokcmbjfbkenj", "fdcgdnkidjaadafnichfpabhfomcebme"


## Dependencies

Chrome must be installed

### Prerequisite Check

```powershell
if ((Test-Path "C:\Program Files\Google\Chrome\Application\chrome.exe") -Or (Test-Path "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest -OutFile "PathToAtomicsFolder\..\ExternalPayloads\ChromeStandaloneSetup64.exe" #{chrome_url}
Start-Process "PathToAtomicsFolder\..\ExternalPayloads\ChromeStandaloneSetup64.exe" /S
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$extList = #{extension_id}
foreach ($extension in $extList) {
  New-Item -Path HKLM:\Software\Wow6432Node\Google\Chrome\Extensions\$extension -Force
  New-ItemProperty -Path "HKLM:\Software\Wow6432Node\Google\Chrome\Extensions\$extension" -Name "update_url" -Value "https://clients2.google.com/service/update2/crx" -PropertyType "String" -Force}
Start chrome
Start-Sleep -Seconds 30
Stop-Process -Name "chrome"
```

### Cleanup

```powershell
$extList = #{extension_id}
foreach ($extension in $extList) {
Remove-Item -Path "HKLM:\Software\Wow6432Node\Google\Chrome\Extensions\$extension" -ErrorAction Ignore}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1133/T1133.yaml)
