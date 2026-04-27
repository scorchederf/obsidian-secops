---
sigma_id: "6ea3bf32-9680-422d-9f50-e90716b12a66"
title: "UAC Bypass Via Wsreset"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_bypass_via_wsreset.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_bypass_via_wsreset.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "6ea3bf32-9680-422d-9f50-e90716b12a66"
  - "UAC Bypass Via Wsreset"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# UAC Bypass Via Wsreset

Unfixed method for UAC bypass from Windows 10. WSReset.exe file associated with the Windows Store. It will run a binary file contained in a low-privilege registry.

## Metadata

- Rule ID: 6ea3bf32-9680-422d-9f50-e90716b12a66
- Status: test
- Level: high
- Author: oscd.community, Dmitry Uchakin
- Date: 2020-10-07
- Modified: 2021-11-27
- Source Path: rules/windows/registry/registry_event/registry_event_bypass_via_wsreset.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  TargetObject|endswith: \AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command
condition: selection
```

## False Positives

- Unknown

## References

- https://www.bleepingcomputer.com/news/security/trickbot-uses-a-new-windows-10-uac-bypass-to-launch-quietly
- https://lolbas-project.github.io/lolbas/Binaries/Wsreset

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_bypass_via_wsreset.yml)
