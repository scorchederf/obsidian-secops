---
atomic_guid: "4700a710-c821-4e17-a3ec-9e4c81d6845f"
title: "Windows - Discover domain trusts with dsquery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1482"
attack_technique_name: "Domain Trust Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "4700a710-c821-4e17-a3ec-9e4c81d6845f"
  - "Windows - Discover domain trusts with dsquery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - Discover domain trusts with dsquery

Uses the dsquery command to discover domain trusts.
Requires the installation of dsquery via Windows RSAT or the Windows Server AD DS role.

## Metadata

- Atomic GUID: 4700a710-c821-4e17-a3ec-9e4c81d6845f
- Technique: T1482: Domain Trust Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1482/T1482.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Executor

- name: command_prompt

### Command

```commandprompt
dsquery * -filter "(objectClass=trustedDomain)" -attr *
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml)
