---
sigma_id: "31545105-3444-4584-bebf-c466353230d2"
title: "Touch Suspicious Service File"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_touch_susp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_touch_susp.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "31545105-3444-4584-bebf-c466353230d2"
  - "Touch Suspicious Service File"
attack_technique_ids:
  - "T1070.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Touch Suspicious Service File

Detects usage of the "touch" process in service file.

## Metadata

- Rule ID: 31545105-3444-4584-bebf-c466353230d2
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-01-11
- Source Path: rules/linux/process_creation/proc_creation_lnx_touch_susp.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.006]]

## Detection

```yaml
selection:
  Image|endswith: /touch
  CommandLine|contains: ' -t '
  CommandLine|endswith: .service
condition: selection
```

## False Positives

- Admin changing date of files.

## References

- https://blogs.blackberry.com/
- https://twitter.com/Joseliyo_Jstnk/status/1620131033474822144

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_touch_susp.yml)
