---
atomic_guid: "5bcda9cd-8e85-48fa-861d-b5a85d91d48c"
title: "Lolbin Gpscript logon option"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "5bcda9cd-8e85-48fa-861d-b5a85d91d48c"
  - "Lolbin Gpscript logon option"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes logon scripts configured in Group Policy.
https://lolbas-project.github.io/lolbas/Binaries/Gpscript/
https://oddvar.moe/2018/04/27/gpscript-exe-another-lolbin-to-the-list/

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Executor

- name: command_prompt

### Command

```cmd
Gpscript /logon
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
