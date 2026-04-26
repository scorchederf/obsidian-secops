---
sigma_id: "87911521-7098-470b-a459-9a57fc80bdfd"
title: "Sysmon Configuration Update"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_sysmon_config_update.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_sysmon_config_update.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "87911521-7098-470b-a459-9a57fc80bdfd"
  - "Sysmon Configuration Update"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Sysmon Configuration Update

Detects updates to Sysmon's configuration. Attackers might update or replace the Sysmon configuration with a bare bone one to avoid monitoring without shutting down the service completely

## Metadata

- Rule ID: 87911521-7098-470b-a459-9a57fc80bdfd
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-09
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_sysmon_config_update.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_pe:
- Image|endswith:
  - \Sysmon64.exe
  - \Sysmon.exe
- Description: System activity monitor
selection_cli:
  CommandLine|contains|windash: -c
condition: all of selection_*
```

## False Positives

- Legitimate administrators might use this command to update Sysmon configuration.

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_sysmon_config_update.yml)
