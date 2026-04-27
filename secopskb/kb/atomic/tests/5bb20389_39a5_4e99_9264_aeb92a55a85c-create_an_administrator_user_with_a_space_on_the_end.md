---
atomic_guid: "5bb20389-39a5-4e99-9264-aeb92a55a85c"
title: "Create an \"Administrator \" user (with a space on the end)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564"
attack_technique_name: "Hide Artifacts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564/T1564.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "5bb20389-39a5-4e99-9264-aeb92a55a85c"
  - "Create an \"Administrator \" user (with a space on the end)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creating a user with a username containing with a space on the end

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564: Hide Artifacts]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-LocalUser -Name "Administrator " -NoPassword
```

### Cleanup

```powershell
Remove-LocalUser -Name "Administrator " 2>&1 | out-null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564/T1564.yaml)
