---
atomic_guid: "46c2c362-2679-4ef5-aec9-0e958e135be4"
title: "Examine domain password policy - Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "46c2c362-2679-4ef5-aec9-0e958e135be4"
  - "Examine domain password policy - Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Examine domain password policy - Windows

Lists the domain password policy to console on Windows.

## Metadata

- Atomic GUID: 46c2c362-2679-4ef5-aec9-0e958e135be4
- Technique: T1201: Password Policy Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1201/T1201.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201]]

## Executor

- name: command_prompt

### Command

```cmd
net accounts /domain
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
