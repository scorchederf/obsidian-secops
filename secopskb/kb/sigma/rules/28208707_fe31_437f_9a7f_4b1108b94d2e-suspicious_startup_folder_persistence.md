---
sigma_id: "28208707-fe31-437f-9a7f-4b1108b94d2e"
title: "Suspicious Startup Folder Persistence"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_startup_folder_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_startup_folder_persistence.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "28208707-fe31-437f-9a7f-4b1108b94d2e"
  - "Suspicious Startup Folder Persistence"
attack_technique_ids:
  - "T1204.002"
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Startup Folder Persistence

Detects the creation of potentially malicious script and executable files in Windows startup folders, which is a common persistence technique used by threat actors.
These files (.ps1, .vbs, .js, .bat, etc.) are automatically executed when a user logs in, making the Startup folder an attractive target for attackers.
This technique is frequently observed in malvertising campaigns and malware distribution where attackers attempt to maintain long-term access to compromised systems.

## Metadata

- Rule ID: 28208707-fe31-437f-9a7f-4b1108b94d2e
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2022-08-10
- Modified: 2025-10-12
- Source Path: rules/windows/file/file_event/file_event_win_susp_startup_folder_persistence.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]
- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection:
  TargetFilename|contains: \Windows\Start Menu\Programs\Startup\
  TargetFilename|endswith:
  - .bat
  - .cmd
  - .dll
  - .hta
  - .jar
  - .js
  - .jse
  - .msi
  - .ps1
  - .psd1
  - .psm1
  - .scr
  - .url
  - .vba
  - .vbe
  - .vbs
  - .wsf
condition: selection
```

## False Positives

- Rare legitimate usage of some of the extensions mentioned in the rule

## References

- https://github.com/last-byte/PersistenceSniper
- https://www.microsoft.com/en-us/security/blog/2025/03/06/malvertising-campaign-leads-to-info-stealers-hosted-on-github/
- https://github.com/redcanaryco/atomic-red-team/blob/5ede8f21e42ebe37e0a6eff757dba60bcfa85859/atomics/T1547.001/T1547.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_startup_folder_persistence.yml)
