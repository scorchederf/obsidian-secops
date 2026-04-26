---
sigma_id: "0e8cfe08-02c9-4815-a2f8-0d157b7ed33e"
title: "File Download with Headless Browser"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_file_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_file_download.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0e8cfe08-02c9-4815-a2f8-0d157b7ed33e"
  - "File Download with Headless Browser"
attack_technique_ids:
  - "T1105"
  - "T1564.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File Download with Headless Browser

Detects execution of chromium based browser in headless mode using the "dump-dom" command line to download files

## Metadata

- Rule ID: 0e8cfe08-02c9-4815-a2f8-0d157b7ed33e
- Status: test
- Level: high
- Author: Sreeman, Florian Roth (Nextron Systems)
- Date: 2022-01-04
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_file_download.yml

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
  CommandLine|contains|all:
  - --headless
  - dump-dom
  - http
filter_optional_edge_1:
  Image|startswith:
  - C:\Program Files (x86)\Microsoft\Edge\Application\
  - C:\Program Files (x86)\Microsoft\EdgeCore\
  - C:\Program Files (x86)\Microsoft\EdgeWebView\
  - C:\Program Files\Microsoft\Edge\Application\
  - C:\Program Files\Microsoft\EdgeCore\
  - C:\Program Files\Microsoft\EdgeWebView\
  - C:\Program Files\WindowsApps\Microsoft.MicrosoftEdge
  Image|endswith:
  - \msedge.exe
  - \msedgewebview2.exe
  - \MicrosoftEdge.exe
  CommandLine|contains: --headless --disable-gpu --disable-extensions --disable-plugins
    --mute-audio --no-first-run --incognito --aggressive-cache-discard --dump-dom
filter_optional_edge_2:
  Image|contains:
  - \AppData\Local\Microsoft\WindowsApps\
  - \Windows\SystemApps\Microsoft.MicrosoftEdge
  Image|endswith:
  - \msedge.exe
  - \MicrosoftEdge.exe
  CommandLine|contains: --headless --disable-gpu --disable-extensions --disable-plugins
    --mute-audio --no-first-run --incognito --aggressive-cache-discard --dump-dom
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1478234484881436672?s=12
- https://www.trendmicro.com/en_us/research/23/e/managed-xdr-investigation-of-ducktail-in-trend-micro-vision-one.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_file_download.yml)
