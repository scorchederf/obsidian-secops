---
sigma_id: "fc4f4817-0c53-4683-a4ee-b17a64bc1039"
title: "Suspicious Desktopimgdownldr Target File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_desktopimgdownldr_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_desktopimgdownldr_file.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "fc4f4817-0c53-4683-a4ee-b17a64bc1039"
  - "Suspicious Desktopimgdownldr Target File"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious Microsoft desktopimgdownldr file creation that stores a file to a suspicious location or contains a file with a suspicious extension

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detection

```yaml
selection:
  Image|endswith: \svchost.exe
  TargetFilename|contains: \Personalization\LockScreenImage\
filter1:
  TargetFilename|contains: C:\Windows\
filter2:
  TargetFilename|contains:
  - .jpg
  - .jpeg
  - .png
condition: selection and not filter1 and not filter2
```

## False Positives

- False positives depend on scripts and administrative tools used in the monitored environment

## References

- https://labs.sentinelone.com/living-off-windows-land-a-new-native-file-downldr/
- https://twitter.com/SBousseaden/status/1278977301745741825

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_desktopimgdownldr_file.yml)
