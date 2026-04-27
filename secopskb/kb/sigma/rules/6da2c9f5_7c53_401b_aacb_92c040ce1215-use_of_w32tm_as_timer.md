---
sigma_id: "6da2c9f5-7c53-401b-aacb-92c040ce1215"
title: "Use of W32tm as Timer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_w32tm.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_w32tm.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6da2c9f5-7c53-401b-aacb-92c040ce1215"
  - "Use of W32tm as Timer"
attack_technique_ids:
  - "T1124"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

When configured with suitable command line arguments, w32tm can act as a delay mechanism

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1124-system_time_discovery|T1124: System Time Discovery]]

## Detection

```yaml
selection_w32tm:
- Image|endswith: \w32tm.exe
- OriginalFileName: w32time.dll
selection_cmd:
  CommandLine|contains|all:
  - /stripchart
  - '/computer:'
  - '/period:'
  - /dataonly
  - '/samples:'
condition: all of selection_*
```

## False Positives

- Legitimate use

## References

- https://github.com/redcanaryco/atomic-red-team/blob/d0dad62dbcae9c60c519368e82c196a3db577055/atomics/T1124/T1124.md
- https://blogs.blackberry.com/en/2022/05/dirty-deeds-done-dirt-cheap-russian-rat-offers-backdoor-bargains

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_w32tm.yml)
