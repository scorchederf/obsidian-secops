---
atomic_guid: "f8da74bb-21b8-4af9-8d84-f2c8e4a220e3"
title: "Lolbin Gpscript startup option"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "f8da74bb-21b8-4af9-8d84-f2c8e4a220e3"
  - "Lolbin Gpscript startup option"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Lolbin Gpscript startup option

Executes startup scripts configured in Group Policy
https://lolbas-project.github.io/lolbas/Binaries/Gpscript/
https://oddvar.moe/2018/04/27/gpscript-exe-another-lolbin-to-the-list/

## Metadata

- Atomic GUID: f8da74bb-21b8-4af9-8d84-f2c8e4a220e3
- Technique: T1218: Signed Binary Proxy Execution
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1218/T1218.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Executor

- name: command_prompt

### Command

```cmd
Gpscript /startup
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
