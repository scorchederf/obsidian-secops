---
sigma_id: "6ddff2e8-ea1a-45d0-8938-93dfc1d67ae7"
title: "PUA - Restic Backup Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_restic.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_restic.yml"
build_date: "2026-04-26 17:03:20"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6ddff2e8-ea1a-45d0-8938-93dfc1d67ae7"
  - "PUA - Restic Backup Tool Execution"
attack_technique_ids:
  - "T1048"
  - "T1567.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PUA - Restic Backup Tool Execution

Detects the execution of the Restic backup tool, which can be used for data exfiltration.
Threat actors may leverage Restic to back up and exfiltrate sensitive data to remote storage locations, including cloud services.
If not legitimately used in the enterprise environment, its presence may indicate malicious activity.

## Metadata

- Rule ID: 6ddff2e8-ea1a-45d0-8938-93dfc1d67ae7
- Status: experimental
- Level: high
- Author: Nounou Mbeiri, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-10-17
- Source Path: rules/windows/process_creation/proc_creation_win_pua_restic.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]
- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.002]]

## Detection

```yaml
selection_specific:
- CommandLine|contains|all:
  - --password-file
  - init
  - ' -r '
- CommandLine|contains|all:
  - --use-fs-snapshot
  - backup
  - ' -r '
selection_restic:
  CommandLine|contains:
  - 'sftp:'
  - rest:http
  - s3:s3.
  - s3.http
  - 'azure:'
  - ' gs:'
  - 'rclone:'
  - 'swift:'
  - ' b2:'
  CommandLine|contains|all:
  - ' init '
  - ' -r '
condition: 1 of selection_*
```

## False Positives

- Legitimate use of Restic for backup purposes within the organization.

## References

- https://thedfirreport.com/2024/09/30/nitrogen-campaign-drops-sliver-and-ends-with-blackcat-ransomware/#exfiltration
- https://restic.net/
- https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_restic.yml)
