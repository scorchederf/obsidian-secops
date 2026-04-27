---
sigma_id: "647c7b9e-d784-4fda-b9a0-45c565a7b729"
title: "Operator Bloopers Cobalt Strike Commands"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_bloopers_cmd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_bloopers_cmd.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "647c7b9e-d784-4fda-b9a0-45c565a7b729"
  - "Operator Bloopers Cobalt Strike Commands"
attack_technique_ids:
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects use of Cobalt Strike commands accidentally entered in the CMD shell

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]

## Detection

```yaml
selection_img:
- OriginalFileName: Cmd.Exe
- Image|endswith: \cmd.exe
selection_cli:
  CommandLine|startswith:
  - 'cmd '
  - cmd.exe
  - c:\windows\system32\cmd.exe
  CommandLine|contains:
  - psinject
  - spawnas
  - make_token
  - remote-exec
  - rev2self
  - dcsync
  - logonpasswords
  - execute-assembly
  - getsystem
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/cobalt-4-5-user-guide.pdf
- https://thedfirreport.com/2021/10/04/bazarloader-and-the-conti-leaks/
- https://thedfirreport.com/2022/06/16/sans-ransomware-summit-2022-can-you-detect-this/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_bloopers_cmd.yml)
