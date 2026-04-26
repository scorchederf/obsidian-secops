---
sigma_id: "7f5d1c9a-3e83-48df-95a7-2b98aae6c13c"
title: "Potential Provlaunch.EXE Binary Proxy Execution Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_provlaunch_potential_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_provlaunch_potential_abuse.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7f5d1c9a-3e83-48df-95a7-2b98aae6c13c"
  - "Potential Provlaunch.EXE Binary Proxy Execution Abuse"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Provlaunch.EXE Binary Proxy Execution Abuse

Detects child processes of "provlaunch.exe" which might indicate potential abuse to proxy execution.

## Metadata

- Rule ID: 7f5d1c9a-3e83-48df-95a7-2b98aae6c13c
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan Poudel
- Date: 2023-08-08
- Source Path: rules/windows/process_creation/proc_creation_win_provlaunch_potential_abuse.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ParentImage|endswith: \provlaunch.exe
filter_main_covered_children:
- Image|endswith:
  - \calc.exe
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \notepad.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
- Image|contains:
  - :\PerfLogs\
  - :\Temp\
  - :\Users\Public\
  - \AppData\Temp\
  - \Windows\System32\Tasks\
  - \Windows\Tasks\
  - \Windows\Temp\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Provlaunch/
- https://twitter.com/0gtweet/status/1674399582162153472

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_provlaunch_potential_abuse.yml)
