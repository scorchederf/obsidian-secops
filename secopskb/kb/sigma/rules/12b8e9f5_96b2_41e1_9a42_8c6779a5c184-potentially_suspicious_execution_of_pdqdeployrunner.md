---
sigma_id: "12b8e9f5-96b2-41e1-9a42-8c6779a5c184"
title: "Potentially Suspicious Execution Of PDQDeployRunner"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pdqdeploy_runner_susp_children.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pdqdeploy_runner_susp_children.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "12b8e9f5-96b2-41e1-9a42-8c6779a5c184"
  - "Potentially Suspicious Execution Of PDQDeployRunner"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Execution Of PDQDeployRunner

Detects suspicious execution of "PDQDeployRunner" which is part of the PDQDeploy service stack that is responsible for executing commands and packages on a remote machines

## Metadata

- Rule ID: 12b8e9f5-96b2-41e1-9a42-8c6779a5c184
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-22
- Modified: 2024-05-02
- Source Path: rules/windows/process_creation/proc_creation_win_pdqdeploy_runner_susp_children.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_parent:
  ParentImage|contains: \PDQDeployRunner-
selection_child:
- Image|endswith:
  - \bash.exe
  - \certutil.exe
  - \cmd.exe
  - \csc.exe
  - \cscript.exe
  - \dllhost.exe
  - \mshta.exe
  - \msiexec.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \scriptrunner.exe
  - \wmic.exe
  - \wscript.exe
  - \wsl.exe
- Image|contains:
  - :\ProgramData\
  - :\Users\Public\
  - :\Windows\TEMP\
  - \AppData\Local\Temp
- CommandLine|contains:
  - ' -decode '
  - ' -enc '
  - ' -encodedcommand '
  - ' -w hidden'
  - DownloadString
  - FromBase64String
  - http
  - 'iex '
  - Invoke-
condition: all of selection_*
```

## False Positives

- Legitimate use of the PDQDeploy tool to execute these commands

## References

- https://twitter.com/malmoeb/status/1550483085472432128

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pdqdeploy_runner_susp_children.yml)
