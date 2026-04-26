---
sigma_id: "0ea52357-cd59-4340-9981-c46c7e900428"
title: "Potentially Suspicious Rundll32.EXE Execution of UDL File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_udl_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_udl_exec.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0ea52357-cd59-4340-9981-c46c7e900428"
  - "Potentially Suspicious Rundll32.EXE Execution of UDL File"
attack_technique_ids:
  - "T1218.011"
  - "T1071"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Rundll32.EXE Execution of UDL File

Detects the execution of rundll32.exe with the oledb32.dll library to open a UDL file.
Threat actors can abuse this technique as a phishing vector to capture authentication credentials or other sensitive data.

## Metadata

- Rule ID: 0ea52357-cd59-4340-9981-c46c7e900428
- Status: test
- Level: medium
- Author: @kostastsale
- Date: 2024-08-16
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_udl_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]
- [[kb/attack/techniques/T1071-application_layer_protocol|T1071]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \explorer.exe
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
selection_cli:
  CommandLine|contains|all:
  - oledb32.dll
  - ',OpenDSLFile '
  - \\Users\\*\\Downloads\\
  CommandLine|endswith: .udl
condition: all of selection_*
```

## False Positives

- UDL files serve as a convenient and flexible tool for managing and testing database connections in various development and administrative scenarios.

## References

- https://trustedsec.com/blog/oops-i-udld-it-again

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_udl_exec.yml)
