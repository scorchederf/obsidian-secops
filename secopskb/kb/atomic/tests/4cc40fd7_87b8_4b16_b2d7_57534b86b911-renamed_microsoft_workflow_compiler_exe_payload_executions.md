---
atomic_guid: "4cc40fd7-87b8-4b16-b2d7-57534b86b911"
title: "Renamed Microsoft.Workflow.Compiler.exe Payload Executions"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "4cc40fd7-87b8-4b16-b2d7-57534b86b911"
  - "Renamed Microsoft.Workflow.Compiler.exe Payload Executions"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Emulates attack with a renamed Microsoft.Workflow.Compiler.exe running a .Net assembly that launches calc.exe

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Input Arguments

### mwcname

- description: Default name of microsoft.workflow.compiler.exe
- type: path
- default: microsoft.workflow.compiler.exe

### mwcpath

- description: Default location of Microsoft.Workflow.Compiler.exe
- type: path
- default: C:\Windows\Microsoft.NET\Framework64\v4.0.30319

### renamed_binary

- description: renamed Microsoft.Workflow.Compiler
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\svchost.exe

### xml_payload

- description: XML to execution
- type: path
- default: PathToAtomicsFolder\T1218\src\T1218.xml

## Dependencies

.Net must be installed for this test to work correctly.

### Prerequisite Check

```powershell
if (Test-Path "#{renamed_binary}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Copy-Item #{mwcpath}\#{mwcname} "#{renamed_binary}" -Force
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
&"#{renamed_binary}" "#{xml_payload}" output.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
