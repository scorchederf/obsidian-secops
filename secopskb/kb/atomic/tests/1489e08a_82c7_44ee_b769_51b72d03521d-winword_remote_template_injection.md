---
atomic_guid: "1489e08a-82c7-44ee-b769-51b72d03521d"
title: "WINWORD Remote Template Injection"
framework: "atomic"
generated: "true"
attack_technique_id: "T1221"
attack_technique_name: "Template Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1221/T1221.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "1489e08a-82c7-44ee-b769-51b72d03521d"
  - "WINWORD Remote Template Injection"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WINWORD Remote Template Injection

Open a .docx file that loads a remote .dotm macro enabled template from https://github.com/redcanaryco/atomic-red-team/tree/master/atomics/T1221/src/opencalc.dotm 
Executes the code specified within the .dotm template.
Requires download of WINWORD found in Microsoft Ofiice at Microsoft: https://www.microsoft.com/en-us/download/office.aspx.  
Default docs file opens Calculator.exe when test sucessfully executed, while AV turned off.

## Metadata

- Atomic GUID: 1489e08a-82c7-44ee-b769-51b72d03521d
- Technique: T1221: Template Injection
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1221/T1221.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1221-template_injection|T1221]]

## Input Arguments

### docx_file

- description: Location of the test docx file on the local filesystem.
- type: path
- default: PathToAtomicsFolder\T1221\src\Calculator.docx

## Executor

- name: command_prompt

### Command

```commandprompt
start "#{docx_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1221/T1221.yaml)
