---
atomic_guid: "107706a5-6f9f-451a-adae-bab8c667829f"
title: "Stage data from Discovery.bat"
framework: "atomic"
generated: "true"
attack_technique_id: "T1074.001"
attack_technique_name: "Data Staged: Local Data Staging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1074.001/T1074.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "107706a5-6f9f-451a-adae-bab8c667829f"
  - "Stage data from Discovery.bat"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilize powershell to download discovery.bat and save to a local file. This emulates an attacker downloading data collection tools onto the host. Upon execution,
verify that the file is saved in the temp directory.

## ATT&CK Mapping

- [[kb/attack/techniques/T1074-data_staged#^t1074001-local-data-staging|T1074.001: Local Data Staging]]

## Input Arguments

### output_file

- description: Location to save downloaded discovery.bat file
- type: path
- default: $env:TEMP\discovery.bat

## Executor

- name: powershell

### Command

```powershell
Invoke-WebRequest "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1074.001/src/Discovery.bat" -OutFile #{output_file}
```

### Cleanup

```powershell
Remove-Item -Force #{output_file} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1074.001/T1074.001.yaml)
