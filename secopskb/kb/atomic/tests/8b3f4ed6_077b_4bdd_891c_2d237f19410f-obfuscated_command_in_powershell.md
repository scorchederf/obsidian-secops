---
atomic_guid: "8b3f4ed6-077b-4bdd-891c-2d237f19410f"
title: "Obfuscated Command in PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027"
attack_technique_name: "Obfuscated Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "8b3f4ed6-077b-4bdd-891c-2d237f19410f"
  - "Obfuscated Command in PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Obfuscated Command in PowerShell

This is an obfuscated PowerShell command which when executed prints "Hello, from PowerShell!". Example is from the 2021 Threat Detection Report by Red Canary.

## Metadata

- Atomic GUID: 8b3f4ed6-077b-4bdd-891c-2d237f19410f
- Technique: T1027: Obfuscated Files or Information
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1027/T1027.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Executor

- name: powershell

### Command

```powershell
$cmDwhy =[TyPe]("{0}{1}" -f 'S','TrING')  ;   $pz2Sb0  =[TYpE]("{1}{0}{2}"-f'nv','cO','ert')  ;  &("{0}{2}{3}{1}{4}" -f'In','SiO','vOKe-EXp','ReS','n') (  (&("{1}{2}{0}"-f'blE','gET-','vaRIA')  ('CMdw'+'h'+'y'))."v`ALUe"::("{1}{0}" -f'iN','jO').Invoke('',( (127, 162,151, 164,145 ,55 , 110 ,157 ,163 , 164 ,40,47, 110 , 145 ,154, 154 ,157 , 54 ,40, 146, 162 , 157,155 ,40, 120, 157 ,167,145 , 162 ,123,150 ,145 , 154 , 154 , 41,47)| .('%') { ( [CHAR] (  $Pz2sB0::"t`OinT`16"(( [sTring]${_}) ,8)))})) )
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml)
