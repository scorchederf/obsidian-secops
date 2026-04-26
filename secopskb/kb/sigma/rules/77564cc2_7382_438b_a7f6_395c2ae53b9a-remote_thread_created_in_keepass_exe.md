---
sigma_id: "77564cc2-7382-438b-a7f6-395c2ae53b9a"
title: "Remote Thread Created In KeePass.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_remote_thread/create_remote_thread_win_keepass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_keepass.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "high"
logsource: "windows / create_remote_thread"
aliases:
  - "77564cc2-7382-438b-a7f6-395c2ae53b9a"
  - "Remote Thread Created In KeePass.EXE"
attack_technique_ids:
  - "T1555.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Thread Created In KeePass.EXE

Detects remote thread creation in "KeePass.exe" which could indicates potential password dumping activity

## Metadata

- Rule ID: 77564cc2-7382-438b-a7f6-395c2ae53b9a
- Status: test
- Level: high
- Author: Timon Hackenjos
- Date: 2022-04-22
- Modified: 2023-05-05
- Source Path: rules/windows/create_remote_thread/create_remote_thread_win_keepass.yml

## Logsource

- category: create_remote_thread
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.005]]

## Detection

```yaml
selection:
  TargetImage|endswith: \KeePass.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.cisa.gov/uscert/ncas/alerts/aa20-259a
- https://github.com/denandz/KeeFarce
- https://github.com/GhostPack/KeeThief

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_keepass.yml)
