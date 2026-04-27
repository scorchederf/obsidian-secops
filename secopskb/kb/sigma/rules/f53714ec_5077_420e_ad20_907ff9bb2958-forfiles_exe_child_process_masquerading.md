---
sigma_id: "f53714ec-5077-420e-ad20-907ff9bb2958"
title: "Forfiles.EXE Child Process Masquerading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_forfiles_child_process_masquerading.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_forfiles_child_process_masquerading.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f53714ec-5077-420e-ad20-907ff9bb2958"
  - "Forfiles.EXE Child Process Masquerading"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Forfiles.EXE Child Process Masquerading

Detects the execution of "forfiles" from a non-default location, in order to potentially spawn a custom "cmd.exe" from the current working directory.

## Metadata

- Rule ID: f53714ec-5077-420e-ad20-907ff9bb2958
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Anish Bogati
- Date: 2024-01-05
- Source Path: rules/windows/process_creation/proc_creation_win_forfiles_child_process_masquerading.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
  ParentCommandLine|endswith:
  - .exe
  - .exe"
  Image|endswith: \cmd.exe
  CommandLine|startswith: /c echo "
filter_main_parent_not_sys:
  ParentImage|contains:
  - :\Windows\System32\
  - :\Windows\SysWOW64\
  ParentImage|endswith: \forfiles.exe
  Image|contains:
  - :\Windows\System32\
  - :\Windows\SysWOW64\
  Image|endswith: \cmd.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.hexacorn.com/blog/2023/12/31/1-little-known-secret-of-forfiles-exe/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_forfiles_child_process_masquerading.yml)
