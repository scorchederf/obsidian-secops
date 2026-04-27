---
atomic_guid: "510cc97f-56ac-4cd3-a198-d3218c23d889"
title: "Use of SecEdit.exe to export the local security policy (including the password policy)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "510cc97f-56ac-4cd3-a198-d3218c23d889"
  - "Use of SecEdit.exe to export the local security policy (including the password policy)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

SecEdit.exe can be used to export the current local security policy applied to a host.
[Reference](https://blueteamops.medium.com/secedit-and-i-know-it-595056dee53d)

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201: Password Policy Discovery]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
secedit.exe /export /areas SECURITYPOLICY /cfg output_mysecpol.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
