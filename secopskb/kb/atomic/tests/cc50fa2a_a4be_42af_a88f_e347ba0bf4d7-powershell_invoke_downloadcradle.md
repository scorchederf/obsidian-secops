---
atomic_guid: "cc50fa2a-a4be-42af-a88f-e347ba0bf4d7"
title: "Powershell Invoke-DownloadCradle"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "manual"
aliases:
  - "cc50fa2a-a4be-42af-a88f-e347ba0bf4d7"
  - "Powershell Invoke-DownloadCradle"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Provided by https://github.com/mgreen27/mgreen27.github.io
Invoke-DownloadCradle is used to generate Network and Endpoint artifacts.

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Executor

- name: manual
- steps: 1. Open Powershell_ise as a Privileged Account
2. Invoke-DownloadCradle.ps1


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
