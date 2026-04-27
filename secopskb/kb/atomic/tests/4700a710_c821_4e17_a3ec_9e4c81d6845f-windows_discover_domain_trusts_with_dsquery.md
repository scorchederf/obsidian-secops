---
atomic_guid: "4700a710-c821-4e17-a3ec-9e4c81d6845f"
title: "Windows - Discover domain trusts with dsquery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1482"
attack_technique_name: "Domain Trust Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml"
build_date: "2026-04-27 19:12:27"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Uses the dsquery command to discover domain trusts.
Requires the installation of dsquery via Windows RSAT or the Windows Server AD DS role.

## ATT&CK Mapping

- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
dsquery * -filter "(objectClass=trustedDomain)" -attr *
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml)
