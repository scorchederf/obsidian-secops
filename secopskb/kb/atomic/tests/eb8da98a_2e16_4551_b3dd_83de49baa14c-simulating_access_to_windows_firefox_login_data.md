---
atomic_guid: "eb8da98a-2e16-4551-b3dd-83de49baa14c"
title: "Simulating access to Windows Firefox Login Data"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "eb8da98a-2e16-4551-b3dd-83de49baa14c"
  - "Simulating access to Windows Firefox Login Data"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Simulates an adversary accessing encrypted credentials from firefox web browser's login database.
more info in https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]

## Dependencies

Firefox must be installed

### Prerequisite Check

```powershell
if ((Test-Path "C:\Program Files\Mozilla Firefox\firefox.exe") -Or (Test-Path "C:\Program Files (x86)\Mozilla Firefox\firefox.exe")) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
if ($env:PROCESSOR_ARCHITECTURE -eq 'AMD64') {$url="https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US"}else {$url="https://download.mozilla.org/?product=firefox-latest-ssl&os=win&lang=en-US"}
$installer = "PathToAtomicsFolder\..\ExternalPayloads\firefoxsetup.exe"
(New-Object Net.WebClient).DownloadFile($url,$installer)
Start-Process $installer -ArgumentList '/S' -Wait
```

Firefox login data file must exist

### Prerequisite Check

```powershell
if (Test-Path "$env:APPDATA\Mozilla\Firefox\Profiles\") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
if ($env:PROCESSOR_ARCHITECTURE -eq 'AMD64') {$firefox="C:\Program Files\Mozilla Firefox\firefox.exe"}else {$firefox="C:\Program Files (x86)\Mozilla Firefox\firefox.exe"}
Start-Process $firefox -ArgumentList '-CreateProfile Atomic' -Wait
Start-Process $firefox -NoNewWindow
Start-Sleep -s 20
Stop-Process -Name firefox
```

## Executor

- name: powershell

### Command

```powershell
Copy-Item "$env:APPDATA\Mozilla\Firefox\Profiles\" -Destination "PathToAtomicsFolder\..\ExternalPayloads" -Force -Recurse
```

### Cleanup

```powershell
Remove-Item -Path "PathToAtomicsFolder\..\ExternalPayloads\Profiles" -Force -ErrorAction Ignore -Recurse
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
