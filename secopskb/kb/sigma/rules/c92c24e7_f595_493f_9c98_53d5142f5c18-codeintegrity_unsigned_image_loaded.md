---
sigma_id: "c92c24e7-f595-493f-9c98-53d5142f5c18"
title: "CodeIntegrity - Unsigned Image Loaded"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/code_integrity/win_codeintegrity_unsigned_image_loaded.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_unsigned_image_loaded.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / codeintegrity-operational"
aliases:
  - "c92c24e7-f595-493f-9c98-53d5142f5c18"
  - "CodeIntegrity - Unsigned Image Loaded"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CodeIntegrity - Unsigned Image Loaded

Detects loaded unsigned image on the system

## Metadata

- Rule ID: c92c24e7-f595-493f-9c98-53d5142f5c18
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-06
- Source Path: rules/windows/builtin/code_integrity/win_codeintegrity_unsigned_image_loaded.yml

## Logsource

- product: windows
- service: codeintegrity-operational

## Detection

```yaml
selection:
  EventID: 3037
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-id-explanations
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-tag-explanations
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_unsigned_image_loaded.yml)
