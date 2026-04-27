---
sigma_id: "65d506d3-fcfe-4071-b4b2-bcefe721bbbb"
title: "Potential Persistence Via PlistBuddy"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_persistence_via_plistbuddy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_persistence_via_plistbuddy.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "macos / process_creation"
aliases:
  - "65d506d3-fcfe-4071-b4b2-bcefe721bbbb"
  - "Potential Persistence Via PlistBuddy"
attack_technique_ids:
  - "T1543.001"
  - "T1543.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential persistence activity using LaunchAgents or LaunchDaemons via the PlistBuddy utility

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543001-launch-agent|T1543.001: Launch Agent]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543004-launch-daemon|T1543.004: Launch Daemon]]

## Detection

```yaml
selection:
  Image|endswith: /PlistBuddy
  CommandLine|contains|all:
  - RunAtLoad
  - 'true'
  CommandLine|contains:
  - LaunchAgents
  - LaunchDaemons
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/clipping-silver-sparrows-wings/
- https://www.manpagez.com/man/8/PlistBuddy/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_persistence_via_plistbuddy.yml)
