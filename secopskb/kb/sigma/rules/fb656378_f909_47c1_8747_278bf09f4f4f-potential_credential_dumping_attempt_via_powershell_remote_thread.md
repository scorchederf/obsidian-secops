---
sigma_id: "fb656378-f909-47c1-8747-278bf09f4f4f"
title: "Potential Credential Dumping Attempt Via PowerShell Remote Thread"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_remote_thread/create_remote_thread_win_powershell_lsass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_powershell_lsass.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / create_remote_thread"
aliases:
  - "fb656378-f909-47c1-8747-278bf09f4f4f"
  - "Potential Credential Dumping Attempt Via PowerShell Remote Thread"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential Credential Dumping Attempt Via PowerShell Remote Thread

Detects remote thread creation by PowerShell processes into "lsass.exe"

## Metadata

- Rule ID: fb656378-f909-47c1-8747-278bf09f4f4f
- Status: test
- Level: high
- Author: oscd.community, Natalia Shornikova
- Date: 2020-10-06
- Modified: 2022-12-18
- Source Path: rules/windows/create_remote_thread/create_remote_thread_win_powershell_lsass.yml

## Logsource

- category: create_remote_thread
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  SourceImage|endswith:
  - \powershell.exe
  - \pwsh.exe
  TargetImage|endswith: \lsass.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_powershell_lsass.yml)
