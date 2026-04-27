---
atomic_guid: "bb6b51e1-ab92-45b5-aeea-e410d06405f8"
title: "Code Signing Policy Modification"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.006"
attack_technique_name: "Subvert Trust Controls: Code Signing Policy Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.006/T1553.006.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "bb6b51e1-ab92-45b5-aeea-e410d06405f8"
  - "Code Signing Policy Modification"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Allows adversaries to subvert trust controls by modifying the code signing policy, enabling the execution of unsigned drivers.

## ATT&CK Mapping

- [[kb/attack/techniques/T1553-subvert_trust_controls#^t1553006-code-signing-policy-modification|T1553.006: Code Signing Policy Modification]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
bcdedit /set testsigning on
```

### Cleanup

```cmd
bcdedit /set testsigning off
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.006/T1553.006.yaml)
