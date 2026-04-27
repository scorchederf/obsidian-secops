---
sigma_id: "49e5bc24-8b86-49f1-b743-535f332c2856"
title: "Microsoft Defender Tamper Protection Trigger"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_tamper_protection_trigger.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_tamper_protection_trigger.yml"
build_date: "2026-04-27 19:13:53"
status: "stable"
level: "high"
logsource: "windows / windefend"
aliases:
  - "49e5bc24-8b86-49f1-b743-535f332c2856"
  - "Microsoft Defender Tamper Protection Trigger"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects blocked attempts to change any of Defender's settings such as "Real Time Monitoring" and "Behavior Monitoring"

## Logsource

- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection:
  EventID: 5013
  Value|endswith:
  - \Windows Defender\DisableAntiSpyware
  - \Windows Defender\DisableAntiVirus
  - \Windows Defender\Scan\DisableArchiveScanning
  - \Windows Defender\Scan\DisableScanningNetworkFiles
  - \Real-Time Protection\DisableRealtimeMonitoring
  - \Real-Time Protection\DisableBehaviorMonitoring
  - \Real-Time Protection\DisableIOAVProtection
  - \Real-Time Protection\DisableScriptScanning
condition: selection
```

## False Positives

- Administrator might try to disable defender features during testing (must be investigated)

## References

- https://bhabeshraj.com/post/tampering-with-microsoft-defenders-tamper-protection
- https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_tamper_protection_trigger.yml)
