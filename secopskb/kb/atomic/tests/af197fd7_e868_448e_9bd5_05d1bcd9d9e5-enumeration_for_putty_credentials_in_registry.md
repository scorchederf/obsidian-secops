---
atomic_guid: "af197fd7-e868-448e-9bd5-05d1bcd9d9e5"
title: "Enumeration for PuTTY Credentials in Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.002"
attack_technique_name: "Unsecured Credentials: Credentials in Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.002/T1552.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "af197fd7-e868-448e-9bd5-05d1bcd9d9e5"
  - "Enumeration for PuTTY Credentials in Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Queries to enumerate for PuTTY credentials in the Registry. PuTTY must be installed for this test to work. If any registry
entries are found, they will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]

## Executor

- name: command_prompt

### Command

```cmd
reg query HKCU\Software\SimonTatham\PuTTY\Sessions /t REG_SZ /s
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.002/T1552.002.yaml)
