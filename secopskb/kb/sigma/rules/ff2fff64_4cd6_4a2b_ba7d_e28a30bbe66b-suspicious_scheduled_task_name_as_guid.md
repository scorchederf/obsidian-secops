---
sigma_id: "ff2fff64-4cd6-4a2b-ba7d-e28a30bbe66b"
title: "Suspicious Scheduled Task Name As GUID"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_guid_task_name.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_guid_task_name.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ff2fff64-4cd6-4a2b-ba7d-e28a30bbe66b"
  - "Suspicious Scheduled Task Name As GUID"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Scheduled Task Name As GUID

Detects creation of a scheduled task with a GUID like name

## Metadata

- Rule ID: ff2fff64-4cd6-4a2b-ba7d-e28a30bbe66b
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-31
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_guid_task_name.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_img:
  Image|endswith: \schtasks.exe
  CommandLine|contains: '/Create '
selection_tn:
  CommandLine|contains:
  - /TN "{
  - /TN '{
  - /TN {
selection_end:
  CommandLine|contains:
  - '}"'
  - '}'''
  - '} '
condition: all of selection_*
```

## False Positives

- Legitimate software naming their tasks as GUIDs

## References

- https://thedfirreport.com/2022/10/31/follina-exploit-leads-to-domain-compromise/
- https://thedfirreport.com/2022/02/21/qbot-and-zerologon-lead-to-full-domain-compromise/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_guid_task_name.yml)
