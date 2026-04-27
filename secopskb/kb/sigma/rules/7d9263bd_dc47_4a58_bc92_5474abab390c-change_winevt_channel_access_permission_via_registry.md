---
sigma_id: "7d9263bd-dc47-4a58-bc92-5474abab390c"
title: "Change Winevt Channel Access Permission Via Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_change_winevt_channelaccess.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_change_winevt_channelaccess.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "7d9263bd-dc47-4a58-bc92-5474abab390c"
  - "Change Winevt Channel Access Permission Via Registry"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects tampering with the "ChannelAccess" registry key in order to change access to Windows event channel.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Detection

```yaml
selection:
  TargetObject|contains: \Microsoft\Windows\CurrentVersion\WINEVT\Channels\
  TargetObject|endswith: \ChannelAccess
  Details|contains:
  - (A;;0x1;;;LA)
  - (A;;0x1;;;SY)
  - (A;;0x5;;;BA)
filter_main_trustedinstaller:
  Image: C:\Windows\servicing\TrustedInstaller.exe
filter_main_tiworker:
  Image|startswith: C:\Windows\WinSxS\
  Image|endswith: \TiWorker.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://app.any.run/tasks/77b2e328-8f36-46b2-b2e2-8a80398217ab/
- https://learn.microsoft.com/en-us/windows/win32/api/winevt/
- https://itconnect.uw.edu/tools-services-support/it-systems-infrastructure/msinf/other-help/understanding-sddl-syntax/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_change_winevt_channelaccess.yml)
