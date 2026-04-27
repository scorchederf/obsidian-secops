---
sigma_id: "ba226dcf-d390-4642-b9af-b534872f1156"
title: "Windows Event Log Access Tampering Via Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_windows_event_log_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_windows_event_log_access.yml"
build_date: "2026-04-27 19:13:59"
status: "experimental"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "ba226dcf-d390-4642-b9af-b534872f1156"
  - "Windows Event Log Access Tampering Via Registry"
attack_technique_ids:
  - "T1547.001"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects changes to the Windows EventLog channel permission values. It focuses on changes to the Security Descriptor Definition Language (SDDL) string, as modifications to these values can restrict access to specific users or groups, potentially aiding in defense evasion by controlling who can view or modify a event log channel. Upon execution, the user shouldn't be able to access the event log channel via the event viewer or via utilities such as "Get-EventLog" or "wevtutil".

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]
- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Detection

```yaml
selection_key_1:
  TargetObject|contains: \SYSTEM\CurrentControlSet\Services\EventLog\
  TargetObject|endswith: \CustomSD
selection_key_2:
  TargetObject|contains:
  - \Policies\Microsoft\Windows\EventLog\
  - \Microsoft\Windows\CurrentVersion\WINEVT\Channels
  TargetObject|endswith: \ChannelAccess
selection_details:
- Details|contains: D:(D;
- Details|contains|all:
  - D:(
  - )(D;
filter_main_trustedinstaller:
  Image: C:\Windows\servicing\TrustedInstaller.exe
filter_main_tiworker:
  Image|startswith: C:\Windows\WinSxS\
  Image|endswith: \TiWorker.exe
filter_optional_empty:
  Image: ''
filter_optional_null:
  Image: null
condition: 1 of selection_key_* and selection_details and not 1 of filter_main_* and
  not 1 of filter_optional_*
```

## False Positives

- Administrative activity, still unlikely

## References

- https://www.atomicredteam.io/atomic-red-team/atomics/T1562.002#atomic-test-8---modify-event-log-channel-access-permissions-via-registry---powershell
- https://www.youtube.com/watch?v=uSYvHUVU8xY
- https://learn.microsoft.com/en-us/windows/win32/secauthz/security-descriptor-definition-language

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_windows_event_log_access.yml)
