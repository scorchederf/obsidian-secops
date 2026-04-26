---
atomic_guid: "752191b1-7c71-445c-9dbe-21bb031b18eb"
title: "Powershell Execute COM Object"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.015"
attack_technique_name: "Event Triggered Execution: Component Object Model Hijacking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.015/T1546.015.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "752191b1-7c71-445c-9dbe-21bb031b18eb"
  - "Powershell Execute COM Object"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Powershell Execute COM Object

Use the PowerShell to execute COM CLSID object.
Reference: https://pentestlab.blog/2020/05/20/persistence-com-hijacking/

## Metadata

- Atomic GUID: 752191b1-7c71-445c-9dbe-21bb031b18eb
- Technique: T1546.015: Event Triggered Execution: Component Object Model Hijacking
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1546.015/T1546.015.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.015]]

## Executor

- name: powershell

### Command

```powershell
$o= [activator]::CreateInstance([type]::GetTypeFromCLSID("9BA05972-F6A8-11CF-A442-00A0C90A8F39"))
$item = $o.Item()
$item.Document.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```

### Cleanup

```powershell
Get-Process -Name "*calc" | Stop-Process
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.015/T1546.015.yaml)
