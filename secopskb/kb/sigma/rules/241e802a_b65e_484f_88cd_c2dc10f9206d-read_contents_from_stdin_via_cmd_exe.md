---
sigma_id: "241e802a-b65e-484f-88cd-c2dc10f9206d"
title: "Read Contents From Stdin Via Cmd.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_stdin_redirect.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_stdin_redirect.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "241e802a-b65e-484f-88cd-c2dc10f9206d"
  - "Read Contents From Stdin Via Cmd.EXE"
attack_technique_ids:
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Read Contents From Stdin Via Cmd.EXE

Detect the use of "<" to read and potentially execute a file via cmd.exe

## Metadata

- Rule ID: 241e802a-b65e-484f-88cd-c2dc10f9206d
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-07
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_stdin_redirect.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Detection

```yaml
selection_cmd:
- OriginalFileName: Cmd.Exe
- Image|endswith: \cmd.exe
selection_cli:
  CommandLine|contains: <
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1059.003/T1059.003.md
- https://web.archive.org/web/20220306121156/https://www.x86matthew.com/view_post?id=ntdll_pipe

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_stdin_redirect.yml)
