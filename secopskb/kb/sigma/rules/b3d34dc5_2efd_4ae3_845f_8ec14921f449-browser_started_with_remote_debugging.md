---
sigma_id: "b3d34dc5-2efd-4ae3-845f-8ec14921f449"
title: "Browser Started with Remote Debugging"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_browsers_remote_debugging.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_remote_debugging.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b3d34dc5-2efd-4ae3-845f-8ec14921f449"
  - "Browser Started with Remote Debugging"
attack_technique_ids:
  - "T1185"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Browser Started with Remote Debugging

Detects browsers starting with the remote debugging flags. Which is a technique often used to perform browser injection attacks

## Metadata

- Rule ID: b3d34dc5-2efd-4ae3-845f-8ec14921f449
- Status: test
- Level: medium
- Author: pH-T (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-27
- Modified: 2022-12-23
- Source Path: rules/windows/process_creation/proc_creation_win_browsers_remote_debugging.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1185-browser_session_hijacking|T1185]]

## Detection

```yaml
selection_chromium_based:
  CommandLine|contains: ' --remote-debugging-'
selection_firefox:
  Image|endswith: \firefox.exe
  CommandLine|contains: ' -start-debugger-server'
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://yoroi.company/wp-content/uploads/2022/05/EternityGroup_report_compressed.pdf
- https://www.mdsec.co.uk/2022/10/analysing-lastpass-part-1/
- https://github.com/defaultnamehere/cookie_crimes/
- https://github.com/wunderwuzzi23/firefox-cookiemonster

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_remote_debugging.yml)
