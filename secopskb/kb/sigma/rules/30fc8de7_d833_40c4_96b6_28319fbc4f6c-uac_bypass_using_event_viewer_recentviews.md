---
sigma_id: "30fc8de7-d833-40c4-96b6-28319fbc4f6c"
title: "UAC Bypass Using Event Viewer RecentViews"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_eventvwr_recentviews.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_eventvwr_recentviews.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "30fc8de7-d833-40c4-96b6-28319fbc4f6c"
  - "UAC Bypass Using Event Viewer RecentViews"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Bypass Using Event Viewer RecentViews

Detects the pattern of UAC Bypass using Event Viewer RecentViews

## Metadata

- Rule ID: 30fc8de7-d833-40c4-96b6-28319fbc4f6c
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-11-22
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_eventvwr_recentviews.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_path:
  CommandLine|contains:
  - \Event Viewer\RecentViews
  - \EventV~1\RecentViews
selection_redirect:
  CommandLine|contains: '>'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/orange_8361/status/1518970259868626944
- https://lolbas-project.github.io/lolbas/Binaries/Eventvwr/#execute

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_eventvwr_recentviews.yml)
