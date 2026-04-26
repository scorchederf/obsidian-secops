---
sigma_id: "ea9bf0fa-edec-4fb8-8b78-b119f2528186"
title: "Windows Defender AMSI Trigger Detected"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_malware_detected_amsi_source.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_malware_detected_amsi_source.yml"
build_date: "2026-04-26 15:01:54"
status: "stable"
level: "high"
logsource: "windows / windefend"
aliases:
  - "ea9bf0fa-edec-4fb8-8b78-b119f2528186"
  - "Windows Defender AMSI Trigger Detected"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Defender AMSI Trigger Detected

Detects triggering of AMSI by Windows Defender.

## Metadata

- Rule ID: ea9bf0fa-edec-4fb8-8b78-b119f2528186
- Status: stable
- Level: high
- Author: Bhabesh Raj
- Date: 2020-09-14
- Modified: 2022-12-07
- Source Path: rules/windows/builtin/windefend/win_defender_malware_detected_amsi_source.yml

## Logsource

- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  EventID: 1116
  SourceName: AMSI
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/windows/win32/amsi/how-amsi-helps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_malware_detected_amsi_source.yml)
