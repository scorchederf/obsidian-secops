---
sigma_id: "45239e6a-b035-4aaf-b339-8ad379fcb67e"
title: "Process Proxy Execution Via Squirrel.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_squirrel_proxy_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_squirrel_proxy_execution.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "45239e6a-b035-4aaf-b339-8ad379fcb67e"
  - "Process Proxy Execution Via Squirrel.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Process Proxy Execution Via Squirrel.EXE

Detects the usage of the "Squirrel.exe" binary to execute arbitrary processes. This binary is part of multiple Electron based software installations (Slack, Teams, Discord, etc.)

## Metadata

- Rule ID: 45239e6a-b035-4aaf-b339-8ad379fcb67e
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Karneades / Markus Neis, Jonhnathan Ribeiro, oscd.community
- Date: 2022-06-09
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_squirrel_proxy_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - \squirrel.exe
  - \update.exe
selection_exec:
  CommandLine|contains:
  - --processStart
  - --processStartAndWait
  - --createShortcut
filter_optional_discord:
  CommandLine|contains|all:
  - :\Users\
  - \AppData\Local\Discord\Update.exe
  - Discord.exe
  CommandLine|contains:
  - --createShortcut
  - --processStart
filter_optional_github_desktop:
  CommandLine|contains|all:
  - :\Users\
  - \AppData\Local\GitHubDesktop\Update.exe
  - GitHubDesktop.exe
  CommandLine|contains:
  - --createShortcut
  - --processStartAndWait
filter_optional_teams:
  CommandLine|contains|all:
  - :\Users\
  - \AppData\Local\Microsoft\Teams\Update.exe
  - Teams.exe
  CommandLine|contains:
  - --processStart
  - --createShortcut
filter_optional_yammer:
  CommandLine|contains|all:
  - :\Users\
  - \AppData\Local\yammerdesktop\Update.exe
  - Yammer.exe
  CommandLine|contains:
  - --processStart
  - --createShortcut
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Expected FP with some Electron based applications such as (1Clipboard, Beaker Browser, Caret, Discord, GitHub Desktop, etc.)

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Squirrel/
- http://www.hexacorn.com/blog/2019/03/30/sqirrel-packages-manager-as-a-lolbin-a-k-a-many-electron-apps-are-lolbins-by-default/
- http://www.hexacorn.com/blog/2018/08/16/squirrel-as-a-lolbin/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_squirrel_proxy_execution.yml)
