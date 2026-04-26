---
sigma_id: "ef9dcfed-690c-4c5d-a9d1-482cd422225c"
title: "Browser Execution In Headless Mode"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_exec.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "ef9dcfed-690c-4c5d-a9d1-482cd422225c"
  - "Browser Execution In Headless Mode"
attack_technique_ids:
  - "T1105"
  - "T1564.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Browser Execution In Headless Mode

Detects execution of Chromium based browser in headless mode

## Metadata

- Rule ID: ef9dcfed-690c-4c5d-a9d1-482cd422225c
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-12
- Source Path: rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]
- [[kb/attack/techniques/T1564-hide_artifacts|T1564.003]]

## Detection

```yaml
selection:
  Image|endswith:
  - \brave.exe
  - \chrome.exe
  - \msedge.exe
  - \opera.exe
  - \vivaldi.exe
  CommandLine|contains: --headless
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1478234484881436672?s=12
- https://www.trendmicro.com/en_us/research/23/e/managed-xdr-investigation-of-ducktail-in-trend-micro-vision-one.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_exec.yml)
