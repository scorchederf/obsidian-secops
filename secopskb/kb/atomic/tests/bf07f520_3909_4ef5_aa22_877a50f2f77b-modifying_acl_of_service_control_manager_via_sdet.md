---
atomic_guid: "bf07f520-3909-4ef5-aa22-877a50f2f77b"
title: "Modifying ACL of Service Control Manager via SDET"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.002"
attack_technique_name: "System Services: Service Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "bf07f520-3909-4ef5-aa22-877a50f2f77b"
  - "Modifying ACL of Service Control Manager via SDET"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Modifying ACL of Service Control Manager via SDET

Modify permissions of Service Control Manager via SDSET. This allows any administrative user to escalate privilege and create a service with SYSTEM level privileges.Restart is required.
[Blog](https://0xv1n.github.io/posts/scmanager/)

## Metadata

- Atomic GUID: bf07f520-3909-4ef5-aa22-877a50f2f77b
- Technique: T1569.002: System Services: Service Execution
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1569.002/T1569.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
sc.exe sdset scmanager D:(A;;KA;;;WD)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml)
