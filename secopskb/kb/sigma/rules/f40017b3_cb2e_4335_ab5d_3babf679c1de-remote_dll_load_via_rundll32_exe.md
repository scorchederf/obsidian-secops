---
sigma_id: "f40017b3-cb2e-4335-ab5d-3babf679c1de"
title: "Remote DLL Load Via Rundll32.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_rundll32_remote_share_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_rundll32_remote_share_load.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "f40017b3-cb2e-4335-ab5d-3babf679c1de"
  - "Remote DLL Load Via Rundll32.EXE"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote DLL Load Via Rundll32.EXE

Detects a remote DLL load event via "rundll32.exe".

## Metadata

- Rule ID: f40017b3-cb2e-4335-ab5d-3babf679c1de
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-18
- Source Path: rules/windows/image_load/image_load_rundll32_remote_share_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Detection

```yaml
selection:
  Image|endswith: \rundll32.exe
  ImageLoaded|startswith: \\\\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/gabe-k/themebleed
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_rundll32_remote_share_load.yml)
