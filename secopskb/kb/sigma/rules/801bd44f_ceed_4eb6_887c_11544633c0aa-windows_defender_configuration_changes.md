---
sigma_id: "801bd44f-ceed-4eb6-887c-11544633c0aa"
title: "Windows Defender Configuration Changes"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_suspicious_features_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_suspicious_features_tampering.yml"
build_date: "2026-04-27 19:13:59"
status: "stable"
level: "high"
logsource: "windows / windefend"
aliases:
  - "801bd44f-ceed-4eb6-887c-11544633c0aa"
  - "Windows Defender Configuration Changes"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious changes to the Windows Defender configuration

## Logsource

- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection:
  EventID: 5007
  NewValue|contains:
  - '\Windows Defender\DisableAntiSpyware '
  - '\Windows Defender\Scan\DisableRemovableDriveScanning '
  - '\Windows Defender\Scan\DisableScanningMappedNetworkDrivesForFullScan '
  - '\Windows Defender\SpyNet\DisableBlockAtFirstSeen '
  - '\Real-Time Protection\SpyNetReporting '
condition: selection
```

## False Positives

- Administrator activity (must be investigated)

## References

- https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide
- https://bidouillesecurity.com/disable-windows-defender-in-powershell/#DisableAntiSpyware

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_suspicious_features_tampering.yml)
