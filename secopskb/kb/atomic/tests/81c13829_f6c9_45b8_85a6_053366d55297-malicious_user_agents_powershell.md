---
atomic_guid: "81c13829-f6c9-45b8-85a6-053366d55297"
title: "Malicious User Agents - Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1071.001"
attack_technique_name: "Application Layer Protocol: Web Protocols"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.001/T1071.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "81c13829-f6c9-45b8-85a6-053366d55297"
  - "Malicious User Agents - Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Malicious User Agents - Powershell

This test simulates an infected host beaconing to command and control. Upon execution, no output will be displayed. 
Use an application such as Wireshark to record the session and observe user agent strings and responses.

Inspired by APTSimulator - https://github.com/NextronSystems/APTSimulator/blob/master/test-sets/command-and-control/malicious-user-agents.bat

## Metadata

- Atomic GUID: 81c13829-f6c9-45b8-85a6-053366d55297
- Technique: T1071.001: Application Layer Protocol: Web Protocols
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1071.001/T1071.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Input Arguments

### domain

- description: Default domain to simulate against
- type: string
- default: www.google.com

## Executor

- name: powershell

### Command

```powershell
Invoke-WebRequest #{domain} -UserAgent "HttpBrowser/1.0" | out-null
Invoke-WebRequest #{domain} -UserAgent "Wget/1.9+cvs-stable (Red Hat modified)" | out-null
Invoke-WebRequest #{domain} -UserAgent "Opera/8.81 (Windows NT 6.0; U; en)" | out-null
Invoke-WebRequest #{domain} -UserAgent "*<|>*" | out-null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.001/T1071.001.yaml)
