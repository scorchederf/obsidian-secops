---
atomic_guid: "22cfde89-befe-4e15-9753-47306b37a6e3"
title: "Execution of HTA and VBS Files using Rundll32 and URL.dll"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.011"
attack_technique_name: "Signed Binary Proxy Execution: Rundll32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "22cfde89-befe-4e15-9753-47306b37a6e3"
  - "Execution of HTA and VBS Files using Rundll32 and URL.dll"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

IcedID uses this TTP as follows:
  rundll32.exe url.dll,OpenURL %PUBLIC%\index.hta
Trickbot uses this TTP as follows:
  rundll32.exe URL.dll,FileProtocolHandler C:\\..\\Detail\\akteullen.vbs

In this atomic, the sample hta file opens the calculator and the vbs file shows a message dialog with "rundll32 spawned wscript"

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Executor

- name: command_prompt

### Command

```cmd
rundll32.exe url.dll,OpenURL "PathToAtomicsFolder\T1218.011\src\index.hta"
rundll32.exe URL.dll,FileProtocolHandler "PathToAtomicsFolder\T1218.011\src\akteullen.vbs"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml)
