---
sigma_id: "1c526788-0abe-4713-862f-b520da5e5316"
title: "Chromium Browser Headless Execution To Mockbin Like Site"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_browsers_chromium_mockbin_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_mockbin_abuse.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1c526788-0abe-4713-862f-b520da5e5316"
  - "Chromium Browser Headless Execution To Mockbin Like Site"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Chromium Browser Headless Execution To Mockbin Like Site

Detects the execution of a Chromium based browser process with the "headless" flag and a URL pointing to the mockbin.org service (which can be used to exfiltrate data).

## Metadata

- Rule ID: 1c526788-0abe-4713-862f-b520da5e5316
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2023-09-11
- Source Path: rules/windows/process_creation/proc_creation_win_browsers_chromium_mockbin_abuse.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
  Image|endswith:
  - \brave.exe
  - \chrome.exe
  - \msedge.exe
  - \opera.exe
  - \vivaldi.exe
selection_headless:
  CommandLine|contains: --headless
selection_url:
  CommandLine|contains:
  - ://run.mocky
  - ://mockbin
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.zscaler.com/blogs/security-research/steal-it-campaign

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_mockbin_abuse.yml)
