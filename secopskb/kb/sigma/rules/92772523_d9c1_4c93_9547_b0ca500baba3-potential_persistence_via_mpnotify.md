---
sigma_id: "92772523-d9c1-4c93-9547-b0ca500baba3"
title: "Potential Persistence Via Mpnotify"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_mpnotify.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_mpnotify.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "92772523-d9c1-4c93-9547-b0ca500baba3"
  - "Potential Persistence Via Mpnotify"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when an attacker register a new SIP provider for persistence and defense evasion

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\mpnotify
condition: selection
```

## False Positives

- Might trigger if a legitimate new SIP provider is registered. But this is not a common occurrence in an environment and should be investigated either way

## References

- https://persistence-info.github.io/Data/mpnotify.html
- https://www.youtube.com/watch?v=ggY3srD9dYs&ab_channel=GrzegorzTworek

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_mpnotify.yml)
