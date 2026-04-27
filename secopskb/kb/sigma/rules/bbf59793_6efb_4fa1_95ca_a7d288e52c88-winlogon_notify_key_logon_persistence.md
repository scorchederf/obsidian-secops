---
sigma_id: "bbf59793-6efb-4fa1-95ca-a7d288e52c88"
title: "Winlogon Notify Key Logon Persistence"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_winlogon_notify_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_winlogon_notify_key.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "bbf59793-6efb-4fa1-95ca-a7d288e52c88"
  - "Winlogon Notify Key Logon Persistence"
attack_technique_ids:
  - "T1547.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Winlogon Notify Key Logon Persistence

Adversaries may abuse features of Winlogon to execute DLLs and/or executables when a user logs in.
Winlogon.exe is a Windows component responsible for actions at logon/logoff as well as the secure attention sequence (SAS) triggered by Ctrl-Alt-Delete.

## Metadata

- Rule ID: bbf59793-6efb-4fa1-95ca-a7d288e52c88
- Status: test
- Level: high
- Author: frack113
- Date: 2021-12-30
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_winlogon_notify_key.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.004]]

## Detection

```yaml
selection:
  TargetObject|endswith: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify\logon
  Details|endswith: .dll
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.004/T1547.004.md#atomic-test-3---winlogon-notify-key-logon-persistence---powershell

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_winlogon_notify_key.yml)
