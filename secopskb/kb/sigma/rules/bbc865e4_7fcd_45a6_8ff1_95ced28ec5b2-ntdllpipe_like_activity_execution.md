---
sigma_id: "bbc865e4-7fcd-45a6-8ff1-95ced28ec5b2"
title: "NtdllPipe Like Activity Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_ntdllpipe_redirect.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_ntdllpipe_redirect.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "bbc865e4-7fcd-45a6-8ff1-95ced28ec5b2"
  - "NtdllPipe Like Activity Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# NtdllPipe Like Activity Execution

Detects command that type the content of ntdll.dll to a different file or a pipe in order to evade AV / EDR detection. As seen being used in the POC NtdllPipe

## Metadata

- Rule ID: bbc865e4-7fcd-45a6-8ff1-95ced28ec5b2
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-05
- Modified: 2023-03-07
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_ntdllpipe_redirect.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  CommandLine|contains:
  - type %windir%\system32\ntdll.dll
  - type %systemroot%\system32\ntdll.dll
  - type c:\windows\system32\ntdll.dll
  - \\ntdll.dll > \\\\.\\pipe\\
condition: selection
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20220306121156/https://www.x86matthew.com/view_post?id=ntdll_pipe

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_ntdllpipe_redirect.yml)
