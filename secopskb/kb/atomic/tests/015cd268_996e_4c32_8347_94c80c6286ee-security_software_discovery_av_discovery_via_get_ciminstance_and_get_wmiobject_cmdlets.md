---
atomic_guid: "015cd268-996e-4c32-8347-94c80c6286ee"
title: "Security Software Discovery - AV Discovery via Get-CimInstance and Get-WmiObject cmdlets"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518.001"
attack_technique_name: "Software Discovery: Security Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "015cd268-996e-4c32-8347-94c80c6286ee"
  - "Security Software Discovery - AV Discovery via Get-CimInstance and Get-WmiObject cmdlets"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Discovery of installed antivirus products via Get-CimInstance and Get-WmiObject cmdlets of powershell.

when sucessfully executed, information about installed AV software is displayed..

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
powershell Get-CimInstance -Namespace root/securityCenter2 -classname antivirusproduct
powershell Get-WmiObject -Namespace root\securitycenter2 -Class antivirusproduct
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml)
