---
atomic_guid: "0e56bf29-ff49-4ea5-9af4-3b81283fd513"
title: "Extracting passwords with findstr"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "0e56bf29-ff49-4ea5-9af4-3b81283fd513"
  - "Extracting passwords with findstr"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Extracting Credentials from Files. Upon execution, the contents of files that contain the word "password" will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]

## Executor

- name: powershell

### Command

```powershell
findstr /si pass *.xml *.doc *.txt *.xls
ls -R | select-string -ErrorAction SilentlyContinue -Pattern password
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
