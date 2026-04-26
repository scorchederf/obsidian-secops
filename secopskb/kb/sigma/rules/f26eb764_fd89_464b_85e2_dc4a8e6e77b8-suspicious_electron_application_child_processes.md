---
sigma_id: "f26eb764-fd89-464b-85e2-dc4a8e6e77b8"
title: "Suspicious Electron Application Child Processes"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_electron_app_children.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_electron_app_children.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f26eb764-fd89-464b-85e2-dc4a8e6e77b8"
  - "Suspicious Electron Application Child Processes"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Electron Application Child Processes

Detects suspicious child processes of electron apps (teams, discord, slack, etc.). This could be a potential sign of ".asar" file tampering (See reference section for more information) or binary execution proxy through specific CLI arguments (see related rule)

## Metadata

- Rule ID: f26eb764-fd89-464b-85e2-dc4a8e6e77b8
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-21
- Modified: 2024-07-12
- Source Path: rules/windows/process_creation/proc_creation_win_susp_electron_app_children.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \chrome.exe
  - \discord.exe
  - \GitHubDesktop.exe
  - \keybase.exe
  - \msedge.exe
  - \msedgewebview2.exe
  - \msteams.exe
  - \slack.exe
  - \teams.exe
selection_child_image:
  Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \whoami.exe
  - \wscript.exe
selection_child_paths:
  Image|contains:
  - :\ProgramData\
  - :\Temp\
  - \AppData\Local\Temp\
  - \Users\Public\
  - \Windows\Temp\
filter_optional_discord:
  ParentImage|endswith: \Discord.exe
  Image|endswith: \cmd.exe
  CommandLine|contains: \NVSMI\nvidia-smi.exe
condition: selection_parent and 1 of selection_child_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://taggart-tech.com/quasar-electron/
- https://github.com/mttaggart/quasar
- https://positive.security/blog/ms-officecmd-rce
- https://lolbas-project.github.io/lolbas/Binaries/Msedge/
- https://lolbas-project.github.io/lolbas/Binaries/Teams/
- https://lolbas-project.github.io/lolbas/Binaries/msedgewebview2/
- https://medium.com/@MalFuzzer/one-electron-to-rule-them-all-dc2e9b263daf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_electron_app_children.yml)
