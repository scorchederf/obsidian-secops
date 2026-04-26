---
sigma_id: "3ab79e90-9fab-4cdf-a7b2-6522bc742adb"
title: "HackTool - RemoteKrbRelay SMB Relay Secrets Dump Module Indicators"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_krbrelay_remote_ioc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_krbrelay_remote_ioc.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "3ab79e90-9fab-4cdf-a7b2-6522bc742adb"
  - "HackTool - RemoteKrbRelay SMB Relay Secrets Dump Module Indicators"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - RemoteKrbRelay SMB Relay Secrets Dump Module Indicators

Detects the creation of file with specific names used by RemoteKrbRelay SMB Relay attack module.

## Metadata

- Rule ID: 3ab79e90-9fab-4cdf-a7b2-6522bc742adb
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-06-27
- Source Path: rules/windows/file/file_event/file_event_win_hktl_krbrelay_remote_ioc.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - :\windows\temp\sam.tmp
  - :\windows\temp\sec.tmp
  - :\windows\temp\sys.tmp
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/CICADA8-Research/RemoteKrbRelay/blob/19ec76ba7aa50c2722b23359bc4541c0a9b2611c/Exploit/RemoteKrbRelay/Relay/Attacks/RemoteRegistry.cs#L31-L40

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_krbrelay_remote_ioc.yml)
