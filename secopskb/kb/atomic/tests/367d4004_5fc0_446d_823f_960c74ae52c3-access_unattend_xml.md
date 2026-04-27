---
atomic_guid: "367d4004-5fc0-446d-823f-960c74ae52c3"
title: "Access unattend.xml"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "367d4004-5fc0-446d-823f-960c74ae52c3"
  - "Access unattend.xml"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Attempts to access unattend.xml, where credentials are commonly stored, within the Panther directory where installation logs are stored.
If these files exist, their contents will be displayed. They are used to store credentials/answers during the unattended windows install process.

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
type C:\Windows\Panther\unattend.xml
type C:\Windows\Panther\Unattend\unattend.xml
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
