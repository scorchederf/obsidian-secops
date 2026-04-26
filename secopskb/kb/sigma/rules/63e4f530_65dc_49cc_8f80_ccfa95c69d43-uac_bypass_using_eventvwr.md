---
sigma_id: "63e4f530-65dc-49cc-8f80-ccfa95c69d43"
title: "UAC Bypass Using EventVwr"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_uac_bypass_eventvwr.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_eventvwr.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "63e4f530-65dc-49cc-8f80-ccfa95c69d43"
  - "UAC Bypass Using EventVwr"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UAC Bypass Using EventVwr

Detects the pattern of a UAC bypass using Windows Event Viewer

## Metadata

- Rule ID: 63e4f530-65dc-49cc-8f80-ccfa95c69d43
- Status: test
- Level: high
- Author: Antonio Cocomazzi (idea), Florian Roth (Nextron Systems)
- Date: 2022-04-27
- Modified: 2022-11-22
- Source Path: rules/windows/file/file_event/file_event_win_uac_bypass_eventvwr.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - \Microsoft\Event Viewer\RecentViews
  - \Microsoft\EventV~1\RecentViews
filter:
  Image|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://twitter.com/orange_8361/status/1518970259868626944?s=20&t=RFXqZjtA7tWM3HxqEH78Aw
- https://twitter.com/splinter_code/status/1519075134296006662?s=12&t=DLUXH86WtcmG_AZ5gY3C6g
- https://lolbas-project.github.io/lolbas/Binaries/Eventvwr/#execute

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_eventvwr.yml)
