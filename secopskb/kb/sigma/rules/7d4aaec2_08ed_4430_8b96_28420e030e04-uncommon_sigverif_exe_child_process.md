---
sigma_id: "7d4aaec2-08ed-4430-8b96-28420e030e04"
title: "Uncommon Sigverif.EXE Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sigverif_uncommon_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sigverif_uncommon_child_process.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7d4aaec2-08ed-4430-8b96-28420e030e04"
  - "Uncommon Sigverif.EXE Child Process"
attack_technique_ids:
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Sigverif.EXE Child Process

Detects uncommon child processes spawning from "sigverif.exe", which could indicate potential abuse of the latter as a living of the land binary in order to proxy execution.

## Metadata

- Rule ID: 7d4aaec2-08ed-4430-8b96-28420e030e04
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-19
- Modified: 2024-08-27
- Source Path: rules/windows/process_creation/proc_creation_win_sigverif_uncommon_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detection

```yaml
selection:
  ParentImage|endswith: \sigverif.exe
filter_main_werfault:
  Image:
  - C:\Windows\System32\WerFault.exe
  - C:\Windows\SysWOW64\WerFault.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.hexacorn.com/blog/2018/04/27/i-shot-the-sigverif-exe-the-gui-based-lolbin/
- https://twitter.com/0gtweet/status/1457676633809330184

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sigverif_uncommon_child_process.yml)
