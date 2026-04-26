---
sigma_id: "5a9e1b2c-8f7d-4a1e-9b3c-0f6d7e5a4b1f"
title: "Windows Defender Threat Severity Default Action Modified"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_defender_threat_action_modified.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_defender_threat_action_modified.yml"
build_date: "2026-04-26 15:01:54"
status: "experimental"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "5a9e1b2c-8f7d-4a1e-9b3c-0f6d7e5a4b1f"
  - "Windows Defender Threat Severity Default Action Modified"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Defender Threat Severity Default Action Modified

Detects modifications or creations of Windows Defender's default threat action settings based on severity to 'allow' or take 'no action'.
This is a highly suspicious configuration change that effectively disables Defender's ability to automatically mitigate threats of a certain severity level,
allowing malicious software to run unimpeded. An attacker might use this technique to bypass defenses before executing payloads.

## Metadata

- Rule ID: 5a9e1b2c-8f7d-4a1e-9b3c-0f6d7e5a4b1f
- Status: experimental
- Level: high
- Author: Matt Anderson (Huntress)
- Date: 2025-07-11
- Source Path: rules/windows/registry/registry_event/registry_event_defender_threat_action_modified.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|contains: \Microsoft\Windows Defender\Threats\ThreatSeverityDefaultAction\
  TargetObject|endswith:
  - \1
  - \2
  - \4
  - \5
  Details:
  - DWORD (0x00000006)
  - DWORD (0x00000009)
condition: selection
```

## False Positives

- Legitimate administration via scripts or tools (e.g., SCCM, Intune, GPO enforcement). Correlate with administrative activity.
- Software installations that legitimately modify Defender settings (less common for these specific keys).

## References

- https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference
- https://learn.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/security-malware-windows-defender-threatseveritydefaultaction
- https://research.splunk.com/endpoint/7215831c-8252-4ae3-8d43-db588e82f952
- https://gist.github.com/Dump-GUY/8daef859f382b895ac6fd0cf094555d2
- https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_defender_threat_action_modified.yml)
