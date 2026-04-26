---
sigma_id: "1321dc4e-a1fe-481d-a016-52c45f0c8b4f"
title: "Windows Defender Exclusions Added"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_config_change_exclusion_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_config_change_exclusion_added.yml"
build_date: "2026-04-26 14:14:40"
status: "stable"
level: "medium"
logsource: "windows / windefend"
aliases:
  - "1321dc4e-a1fe-481d-a016-52c45f0c8b4f"
  - "Windows Defender Exclusions Added"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Exclusions Added

Detects the Setting of Windows Defender Exclusions

## Metadata

- Rule ID: 1321dc4e-a1fe-481d-a016-52c45f0c8b4f
- Status: stable
- Level: medium
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-07-06
- Modified: 2022-12-06
- Source Path: rules/windows/builtin/windefend/win_defender_config_change_exclusion_added.yml

## Logsource

- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  EventID: 5007
  NewValue|contains: \Microsoft\Windows Defender\Exclusions
condition: selection
```

## False Positives

- Administrator actions

## References

- https://twitter.com/_nullbind/status/1204923340810543109

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_config_change_exclusion_added.yml)
