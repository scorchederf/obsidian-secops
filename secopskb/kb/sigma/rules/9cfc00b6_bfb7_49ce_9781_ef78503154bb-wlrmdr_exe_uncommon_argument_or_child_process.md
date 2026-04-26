---
sigma_id: "9cfc00b6-bfb7-49ce-9781-ef78503154bb"
title: "Wlrmdr.EXE Uncommon Argument Or Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wlrmdr_uncommon_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wlrmdr_uncommon_child_process.yml"
build_date: "2026-04-26 14:14:40"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9cfc00b6-bfb7-49ce-9781-ef78503154bb"
  - "Wlrmdr.EXE Uncommon Argument Or Child Process"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Wlrmdr.EXE Uncommon Argument Or Child Process

Detects the execution of "Wlrmdr.exe" with the "-u" command line flag which allows anything passed to it to be an argument of the ShellExecute API, which would allow an attacker to execute arbitrary binaries.
This detection also focuses on any uncommon child processes spawned from "Wlrmdr.exe" as a supplement for those that posses "ParentImage" telemetry.

## Metadata

- Rule ID: 9cfc00b6-bfb7-49ce-9781-ef78503154bb
- Status: experimental
- Level: medium
- Author: frack113, manasmbellani
- Date: 2022-02-16
- Modified: 2025-10-31
- Source Path: rules/windows/process_creation/proc_creation_win_wlrmdr_uncommon_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \wlrmdr.exe
selection_child_img:
- Image|endswith: \wlrmdr.exe
- OriginalFileName: WLRMNDR.EXE
selection_child_cli_flags_s:
  CommandLine|contains|windash: '-s '
selection_child_cli_flags_f:
  CommandLine|contains|windash: '-f '
selection_child_cli_flags_t:
  CommandLine|contains|windash: '-t '
selection_child_cli_flags_m:
  CommandLine|contains|windash: '-m '
selection_child_cli_flags_a:
  CommandLine|contains|windash: '-a '
selection_child_cli_flags_u:
  CommandLine|contains|windash: '-u '
filter_main_winlogon:
  ParentImage: C:\Windows\System32\winlogon.exe
filter_main_empty:
  ParentImage:
  - ''
  - '-'
filter_main_null:
  ParentImage: null
condition: selection_parent or (all of selection_child_* and not 1 of filter_main_*)
```

## False Positives

- Unknown

## References

- https://twitter.com/0gtweet/status/1493963591745220608?s=20&t=xUg9DsZhJy1q9bPTUWgeIQ
- https://lolbas-project.github.io/lolbas/Binaries/Wlrmdr/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wlrmdr_uncommon_child_process.yml)
