---
sigma_id: "bc92ca75-cd42-4d61-9a37-9d5aa259c88b"
title: "Win Defender Restored Quarantine File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_restored_quarantine_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_restored_quarantine_file.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / windefend"
aliases:
  - "bc92ca75-cd42-4d61-9a37-9d5aa259c88b"
  - "Win Defender Restored Quarantine File"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Win Defender Restored Quarantine File

Detects the restoration of files from the defender quarantine

## Metadata

- Rule ID: bc92ca75-cd42-4d61-9a37-9d5aa259c88b
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-06
- Source Path: rules/windows/builtin/windefend/win_defender_restored_quarantine_file.yml

## Logsource

- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  EventID: 1009
condition: selection
```

## False Positives

- Legitimate administrator activity restoring a file

## References

- https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_restored_quarantine_file.yml)
