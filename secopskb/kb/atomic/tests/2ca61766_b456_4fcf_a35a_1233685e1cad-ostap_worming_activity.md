---
atomic_guid: "2ca61766-b456-4fcf-a35a-1233685e1cad"
title: "OSTAP Worming Activity"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "2ca61766-b456-4fcf-a35a-1233685e1cad"
  - "OSTAP Worming Activity"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# OSTAP Worming Activity

OSTap copies itself in a specfic way to shares and secondary drives. This emulates the activity.

## Metadata

- Atomic GUID: 2ca61766-b456-4fcf-a35a-1233685e1cad
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### destination_path

- description: Path to create remote file at. Default is local admin share.
- type: string
- default: \\localhost\C$

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
pushd #{destination_path}
echo var fileObject = WScript.createobject("Scripting.FileSystemObject");var newfile = fileObject.CreateTextFile("AtomicTestFileT1105.js", true);newfile.WriteLine("This is an atomic red team test file for T1105. It simulates how OSTap worms accross network shares and drives.");newfile.Close(); > AtomicTestT1105.js
CScript.exe AtomicTestT1105.js //E:JScript
del AtomicTestT1105.js /Q >nul 2>&1
del AtomicTestFileT1105.js /Q >nul 2>&1
popd
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
