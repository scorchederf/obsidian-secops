---
sigma_id: "3e8207c5-fcd2-4ea6-9418-15d45b4890e4"
title: "Potential Data Stealing Via Chromium Headless Debugging"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_debugging.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_debugging.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "3e8207c5-fcd2-4ea6-9418-15d45b4890e4"
  - "Potential Data Stealing Via Chromium Headless Debugging"
attack_technique_ids:
  - "T1185"
  - "T1564.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Data Stealing Via Chromium Headless Debugging

Detects chromium based browsers starting in headless and debugging mode and pointing to a user profile. This could be a sign of data stealing or remote control

## Metadata

- Rule ID: 3e8207c5-fcd2-4ea6-9418-15d45b4890e4
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-23
- Source Path: rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_debugging.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1185-browser_session_hijacking|T1185]]
- [[kb/attack/techniques/T1564-hide_artifacts|T1564.003]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - --remote-debugging-
  - --user-data-dir
  - --headless
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/defaultnamehere/cookie_crimes/
- https://mango.pdf.zone/stealing-chrome-cookies-without-a-password
- https://embracethered.com/blog/posts/2020/cookie-crimes-on-mirosoft-edge/
- https://embracethered.com/blog/posts/2020/chrome-spy-remote-control/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_headless_debugging.yml)
