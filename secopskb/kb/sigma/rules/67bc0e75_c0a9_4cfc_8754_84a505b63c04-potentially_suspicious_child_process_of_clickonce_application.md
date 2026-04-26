---
sigma_id: "67bc0e75-c0a9-4cfc-8754-84a505b63c04"
title: "Potentially Suspicious Child Process Of ClickOnce Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dfsvc_suspicious_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dfsvc_suspicious_child_processes.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "67bc0e75-c0a9-4cfc-8754-84a505b63c04"
  - "Potentially Suspicious Child Process Of ClickOnce Application"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Child Process Of ClickOnce Application

Detects potentially suspicious child processes of a ClickOnce deployment application

## Metadata

- Rule ID: 67bc0e75-c0a9-4cfc-8754-84a505b63c04
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-12
- Source Path: rules/windows/process_creation/proc_creation_win_dfsvc_suspicious_child_processes.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  ParentImage|contains: \AppData\Local\Apps\2.0\
  Image|endswith:
  - \calc.exe
  - \cmd.exe
  - \cscript.exe
  - \explorer.exe
  - \mshta.exe
  - \net.exe
  - \net1.exe
  - \nltest.exe
  - \notepad.exe
  - \powershell.exe
  - \pwsh.exe
  - \reg.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \schtasks.exe
  - \werfault.exe
  - \wscript.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://posts.specterops.io/less-smartscreen-more-caffeine-ab-using-clickonce-for-trusted-code-execution-1446ea8051c5

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dfsvc_suspicious_child_processes.yml)
