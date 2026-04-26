---
sigma_id: "fccfb43e-09a7-4bd2-8b37-a5a7df33386d"
title: ".RDP File Created By Uncommon Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_rdp_file_susp_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_rdp_file_susp_creation.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "fccfb43e-09a7-4bd2-8b37-a5a7df33386d"
  - ".RDP File Created By Uncommon Application"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# .RDP File Created By Uncommon Application

Detects creation of a file with an ".rdp" extension by an application that doesn't commonly create such files.

## Metadata

- Rule ID: fccfb43e-09a7-4bd2-8b37-a5a7df33386d
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-18
- Modified: 2024-11-01
- Source Path: rules/windows/file/file_event/file_event_win_rdp_file_susp_creation.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|endswith: .rdp
  Image|endswith:
  - \brave.exe
  - \CCleaner Browser\Application\CCleanerBrowser.exe
  - \chromium.exe
  - \firefox.exe
  - \Google\Chrome\Application\chrome.exe
  - \iexplore.exe
  - \microsoftedge.exe
  - \msedge.exe
  - \Opera.exe
  - \Vivaldi.exe
  - \Whale.exe
  - \olk.exe
  - \Outlook.exe
  - \RuntimeBroker.exe
  - \Thunderbird.exe
  - \Discord.exe
  - \Keybase.exe
  - \msteams.exe
  - \Slack.exe
  - \teams.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.blackhillsinfosec.com/rogue-rdp-revisiting-initial-access-methods/
- https://web.archive.org/web/20230726144748/https://blog.thickmints.dev/mintsights/detecting-rogue-rdp/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_rdp_file_susp_creation.yml)
