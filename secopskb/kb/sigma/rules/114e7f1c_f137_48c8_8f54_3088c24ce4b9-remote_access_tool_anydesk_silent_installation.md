---
sigma_id: "114e7f1c-f137-48c8-8f54-3088c24ce4b9"
title: "Remote Access Tool - AnyDesk Silent Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_silent_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_silent_install.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "114e7f1c-f137-48c8-8f54-3088c24ce4b9"
  - "Remote Access Tool - AnyDesk Silent Installation"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects AnyDesk Remote Desktop silent installation. Which can be used by attackers to gain remote access.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools#^t1219002-remote-desktop-software|T1219.002: Remote Desktop Software]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - --install
  - --start-with-win
  - --silent
condition: selection
```

## False Positives

- Legitimate deployment of AnyDesk

## References

- https://twitter.com/TheDFIRReport/status/1423361119926816776?s=20
- https://support.anydesk.com/Automatic_Deployment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_silent_install.yml)
