---
sigma_id: "e37db05d-d1f9-49c8-b464-cee1a4b11638"
title: "PUA - Rclone Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_rclone_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_rclone_execution.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e37db05d-d1f9-49c8-b464-cee1a4b11638"
  - "PUA - Rclone Execution"
attack_technique_ids:
  - "T1567.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Rclone Execution

Detects execution of RClone utility for exfiltration as used by various ransomwares strains like REvil, Conti, FiveHands, etc

## Metadata

- Rule ID: e37db05d-d1f9-49c8-b464-cee1a4b11638
- Status: test
- Level: high
- Author: Bhabesh Raj, Sittikorn S, Aaron Greetham (@beardofbinary) - NCC Group
- Date: 2021-05-10
- Modified: 2023-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_pua_rclone_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.002]]

## Detection

```yaml
selection_specific_options:
  CommandLine|contains|all:
  - '--config '
  - '--no-check-certificate '
  - ' copy '
selection_rclone_img:
- Image|endswith: \rclone.exe
- Description: Rsync for cloud storage
selection_rclone_cli:
  CommandLine|contains:
  - pass
  - user
  - copy
  - sync
  - config
  - lsd
  - remote
  - ls
  - mega
  - pcloud
  - ftp
  - ignore-existing
  - auto-confirm
  - transfers
  - multi-thread-streams
  - 'no-check-certificate '
condition: selection_specific_options or all of selection_rclone_*
```

## False Positives

- Unknown

## References

- https://research.nccgroup.com/2021/05/27/detecting-rclone-an-effective-tool-for-exfiltration/
- https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware
- https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a
- https://labs.sentinelone.com/egregor-raas-continues-the-chaos-with-cobalt-strike-and-rclone
- https://www.splunk.com/en_us/blog/security/darkside-ransomware-splunk-threat-update-and-detections.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_rclone_execution.yml)
