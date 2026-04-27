---
atomic_guid: "f592ba2a-e9e8-4d62-a459-ef63abd819fd"
title: "Execute Commands"
framework: "atomic"
generated: "true"
attack_technique_id: "T1559.002"
attack_technique_name: "Inter-Process Communication: Dynamic Data Exchange"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1559.002/T1559.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "manual"
aliases:
  - "f592ba2a-e9e8-4d62-a459-ef63abd819fd"
  - "Execute Commands"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes commands via DDE using Microsfot Word

## ATT&CK Mapping

- [[kb/attack/techniques/T1559-inter-process_communication#^t1559002-dynamic-data-exchange|T1559.002: Dynamic Data Exchange]]

## Executor

- name: manual
- steps: Open Microsoft Word

Insert tab -> Quick Parts -> Field

Choose = (Formula) and click ok.

After that, you should see a Field inserted in the document with an error "!Unexpected End of Formula", right-click the Field, and choose Toggle Field Codes.

The Field Code should now be displayed, change it to Contain the following:

{DDEAUTO c:\\windows\\system32\\cmd.exe "/k calc.exe"  }


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1559.002/T1559.002.yaml)
