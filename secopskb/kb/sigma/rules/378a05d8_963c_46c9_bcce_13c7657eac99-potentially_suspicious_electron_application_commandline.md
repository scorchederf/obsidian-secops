---
sigma_id: "378a05d8-963c-46c9-bcce-13c7657eac99"
title: "Potentially Suspicious Electron Application CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "378a05d8-963c-46c9-bcce-13c7657eac99"
  - "Potentially Suspicious Electron Application CommandLine"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Electron Application CommandLine

Detects potentially suspicious CommandLine of electron apps (teams, discord, slack, etc.). This could be a sign of abuse to proxy execution through a signed binary.

## Metadata

- Rule ID: 378a05d8-963c-46c9-bcce-13c7657eac99
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-05
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith:
  - \chrome.exe
  - \code.exe
  - \discord.exe
  - \GitHubDesktop.exe
  - \keybase.exe
  - \msedge_proxy.exe
  - \msedge.exe
  - \msedgewebview2.exe
  - \msteams.exe
  - \slack.exe
  - \Teams.exe
- OriginalFileName:
  - chrome.exe
  - code.exe
  - discord.exe
  - GitHubDesktop.exe
  - keybase.exe
  - msedge_proxy.exe
  - msedge.exe
  - msedgewebview2.exe
  - msteams.exe
  - slack.exe
  - Teams.exe
selection_cli:
  CommandLine|contains:
  - --browser-subprocess-path
  - --gpu-launcher
  - --renderer-cmd-prefix
  - --utility-cmd-prefix
condition: all of selection_*
```

## False Positives

- Legitimate usage for debugging purposes

## References

- https://positive.security/blog/ms-officecmd-rce
- https://lolbas-project.github.io/lolbas/Binaries/Teams/
- https://lolbas-project.github.io/lolbas/Binaries/Msedge/
- https://lolbas-project.github.io/lolbas/Binaries/msedgewebview2/
- https://medium.com/@MalFuzzer/one-electron-to-rule-them-all-dc2e9b263daf
- https://chromium.googlesource.com/chromium/chromium/+/master/content/public/common/content_switches.cc

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml)
