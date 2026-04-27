---
sigma_id: "77564cc2-7382-438b-a7f6-395c2ae53b9a"
title: "Remote Thread Created In KeePass.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_remote_thread/create_remote_thread_win_keepass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_keepass.yml"
build_date: "2026-04-27 19:13:55"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects remote thread creation in "KeePass.exe" which could indicates potential password dumping activity

## Logsource

- category: create_remote_thread
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores#^t1555005-password-managers|T1555.005: Password Managers]]

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
