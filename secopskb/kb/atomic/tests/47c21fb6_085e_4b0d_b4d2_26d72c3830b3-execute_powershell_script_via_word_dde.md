---
atomic_guid: "47c21fb6-085e-4b0d-b4d2-26d72c3830b3"
title: "Execute PowerShell script via Word DDE"
framework: "atomic"
generated: "true"
attack_technique_id: "T1559.002"
attack_technique_name: "Inter-Process Communication: Dynamic Data Exchange"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1559.002/T1559.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "47c21fb6-085e-4b0d-b4d2-26d72c3830b3"
  - "Execute PowerShell script via Word DDE"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

When the word document opens it will prompt the user to click ok on a dialogue box, then attempt to run PowerShell with DDEAUTO to download and execute a powershell script

## ATT&CK Mapping

- [[kb/attack/techniques/T1559-inter-process_communication#^t1559002-dynamic-data-exchange|T1559.002: Dynamic Data Exchange]]

## Executor

- name: command_prompt

### Command

```cmd
start "$PathToAtomicsFolder\T1559.002\bin\DDE_Document.docx"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1559.002/T1559.002.yaml)
