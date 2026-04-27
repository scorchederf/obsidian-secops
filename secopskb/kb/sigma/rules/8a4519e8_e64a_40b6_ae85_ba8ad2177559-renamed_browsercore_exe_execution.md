---
sigma_id: "8a4519e8-e64a-40b6-ae85-ba8ad2177559"
title: "Renamed BrowserCore.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_browsercore.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_browsercore.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8a4519e8-e64a-40b6-ae85-ba8ad2177559"
  - "Renamed BrowserCore.EXE Execution"
attack_technique_ids:
  - "T1528"
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects process creation with a renamed BrowserCore.exe (used to extract Azure tokens)

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528: Steal Application Access Token]]
- [[kb/attack/techniques/T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]

## Detection

```yaml
selection:
  OriginalFileName: BrowserCore.exe
filter_realbrowsercore:
  Image|endswith: \BrowserCore.exe
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://twitter.com/mariuszbit/status/1531631015139102720

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_browsercore.yml)
