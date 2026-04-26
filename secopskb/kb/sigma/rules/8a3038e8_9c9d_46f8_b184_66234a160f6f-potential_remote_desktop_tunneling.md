---
sigma_id: "8a3038e8-9c9d-46f8-b184-66234a160f6f"
title: "Potential Remote Desktop Tunneling"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_remote_desktop_tunneling.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_remote_desktop_tunneling.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "8a3038e8-9c9d-46f8-b184-66234a160f6f"
  - "Potential Remote Desktop Tunneling"
attack_technique_ids:
  - "T1021"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Remote Desktop Tunneling

Detects potential use of an SSH utility to establish RDP over a reverse SSH Tunnel. This can be used by attackers to enable routing of network packets that would otherwise not reach their intended destination.

## Metadata

- Rule ID: 8a3038e8-9c9d-46f8-b184-66234a160f6f
- Status: test
- Level: medium
- Author: Tim Rauch, Elastic (idea)
- Date: 2022-09-27
- Source Path: rules/windows/process_creation/proc_creation_win_susp_remote_desktop_tunneling.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021]]

## Detection

```yaml
selection:
  CommandLine|contains: :3389
selection_opt:
  CommandLine|contains:
  - ' -L '
  - ' -P '
  - ' -R '
  - ' -pw '
  - ' -ssh '
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/potential-remote-desktop-tunneling-detected.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_remote_desktop_tunneling.yml)
