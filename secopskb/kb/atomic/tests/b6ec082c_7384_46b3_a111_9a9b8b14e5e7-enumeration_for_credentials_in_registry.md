---
atomic_guid: "b6ec082c-7384-46b3-a111-9a9b8b14e5e7"
title: "Enumeration for Credentials in Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.002"
attack_technique_name: "Unsecured Credentials: Credentials in Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.002/T1552.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "b6ec082c-7384-46b3-a111-9a9b8b14e5e7"
  - "Enumeration for Credentials in Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Queries to enumerate for credentials in the Registry. Upon execution, any registry key containing the word "password" will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]

## Executor

- name: command_prompt

### Command

```cmd
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.002/T1552.002.yaml)
