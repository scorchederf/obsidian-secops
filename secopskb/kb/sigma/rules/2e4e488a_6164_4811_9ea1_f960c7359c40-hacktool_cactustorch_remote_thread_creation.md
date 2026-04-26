---
sigma_id: "2e4e488a-6164-4811-9ea1-f960c7359c40"
title: "HackTool - CACTUSTORCH Remote Thread Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_remote_thread/create_remote_thread_win_hktl_cactustorch.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_hktl_cactustorch.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / create_remote_thread"
aliases:
  - "2e4e488a-6164-4811-9ea1-f960c7359c40"
  - "HackTool - CACTUSTORCH Remote Thread Creation"
attack_technique_ids:
  - "T1055.012"
  - "T1059.005"
  - "T1059.007"
  - "T1218.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - CACTUSTORCH Remote Thread Creation

Detects remote thread creation from CACTUSTORCH as described in references.

## Metadata

- Rule ID: 2e4e488a-6164-4811-9ea1-f960c7359c40
- Status: test
- Level: high
- Author: @SBousseaden (detection), Thomas Patzke (rule)
- Date: 2019-02-01
- Modified: 2023-05-05
- Source Path: rules/windows/create_remote_thread/create_remote_thread_win_hktl_cactustorch.yml

## Logsource

- category: create_remote_thread
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055.012]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.005]]

## Detection

```yaml
selection:
  SourceImage|endswith:
  - \System32\cscript.exe
  - \System32\wscript.exe
  - \System32\mshta.exe
  - \winword.exe
  - \excel.exe
  TargetImage|contains: \SysWOW64\
  StartModule: null
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/SBousseaden/status/1090588499517079552
- https://github.com/mdsecactivebreach/CACTUSTORCH

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_hktl_cactustorch.yml)
