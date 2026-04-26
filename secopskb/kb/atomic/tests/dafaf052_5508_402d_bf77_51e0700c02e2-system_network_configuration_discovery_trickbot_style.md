---
atomic_guid: "dafaf052-5508-402d-bf77-51e0700c02e2"
title: "System Network Configuration Discovery (TrickBot Style)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016"
attack_technique_name: "System Network Configuration Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "dafaf052-5508-402d-bf77-51e0700c02e2"
  - "System Network Configuration Discovery (TrickBot Style)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Network Configuration Discovery (TrickBot Style)

Identify network configuration information as seen by Trickbot and described here https://www.sneakymonkey.net/2019/10/29/trickbot-analysis-part-ii/

Upon successful execution, cmd.exe will spawn `ipconfig /all`, `net config workstation`, `net view /all /domain`, `nltest /domain_trusts`. Output will be via stdout.

## Metadata

- Atomic GUID: dafaf052-5508-402d-bf77-51e0700c02e2
- Technique: T1016: System Network Configuration Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1016/T1016.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Executor

- name: command_prompt

### Command

```commandprompt
ipconfig /all
net config workstation
net view /all /domain
nltest /domain_trusts
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml)
