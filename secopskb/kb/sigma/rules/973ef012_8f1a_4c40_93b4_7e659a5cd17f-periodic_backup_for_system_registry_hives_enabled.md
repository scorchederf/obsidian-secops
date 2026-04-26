---
sigma_id: "973ef012-8f1a-4c40-93b4-7e659a5cd17f"
title: "Periodic Backup For System Registry Hives Enabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_enable_periodic_backup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_enable_periodic_backup.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "973ef012-8f1a-4c40-93b4-7e659a5cd17f"
  - "Periodic Backup For System Registry Hives Enabled"
attack_technique_ids:
  - "T1113"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Periodic Backup For System Registry Hives Enabled

Detects the enabling of the "EnablePeriodicBackup" registry value. Once enabled, The OS will backup System registry hives on restarts to the "C:\Windows\System32\config\RegBack" folder. Windows creates a "RegIdleBackup" task to manage subsequent backups.
Registry backup was a default behavior on Windows and was disabled as of "Windows 10, version 1803".

## Metadata

- Rule ID: 973ef012-8f1a-4c40-93b4-7e659a5cd17f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-07-01
- Source Path: rules/windows/registry/registry_set/registry_set_enable_periodic_backup.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Control\Session Manager\Configuration Manager\EnablePeriodicBackup
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Legitimate need for RegBack feature by administrators.

## References

- https://learn.microsoft.com/en-us/troubleshoot/windows-client/installing-updates-features-roles/system-registry-no-backed-up-regback-folder

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_enable_periodic_backup.yml)
