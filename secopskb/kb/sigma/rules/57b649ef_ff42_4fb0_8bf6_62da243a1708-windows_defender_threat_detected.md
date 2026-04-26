---
sigma_id: "57b649ef-ff42-4fb0-8bf6-62da243a1708"
title: "Windows Defender Threat Detected"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_threat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_threat.yml"
build_date: "2026-04-26 15:01:54"
status: "stable"
level: "high"
logsource: "windows / windefend"
aliases:
  - "57b649ef-ff42-4fb0-8bf6-62da243a1708"
  - "Windows Defender Threat Detected"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Defender Threat Detected

Detects actions taken by Windows Defender malware detection engines

## Metadata

- Rule ID: 57b649ef-ff42-4fb0-8bf6-62da243a1708
- Status: stable
- Level: high
- Author: Ján Trenčanský
- Date: 2020-07-28
- Source Path: rules/windows/builtin/windefend/win_defender_threat.yml

## Logsource

- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  EventID:
  - 1006
  - 1015
  - 1116
  - 1117
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_threat.yml)
