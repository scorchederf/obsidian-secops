---
sigma_id: "ebef4391-1a81-4761-a40a-1db446c0e625"
title: "New ActiveScriptEventConsumer Created Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_eventconsumer_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_eventconsumer_creation.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ebef4391-1a81-4761-a40a-1db446c0e625"
  - "New ActiveScriptEventConsumer Created Via Wmic.EXE"
attack_technique_ids:
  - "T1546.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# New ActiveScriptEventConsumer Created Via Wmic.EXE

Detects WMIC executions in which an event consumer gets created. This could be used to establish persistence

## Metadata

- Rule ID: ebef4391-1a81-4761-a40a-1db446c0e625
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-06-25
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_eventconsumer_creation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - ActiveScriptEventConsumer
  - ' CREATE '
condition: selection
```

## False Positives

- Legitimate software creating script event consumers

## References

- https://twitter.com/johnlatwc/status/1408062131321270282?s=12
- https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_eventconsumer_creation.yml)
