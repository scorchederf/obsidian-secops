---
sigma_id: "8e0bb260-d4b2-4fff-bb8d-3f82118e6892"
title: "Potentially Suspicious CMD Shell Output Redirect"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_redirection_susp_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_redirection_susp_folder.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "8e0bb260-d4b2-4fff-bb8d-3f82118e6892"
  - "Potentially Suspicious CMD Shell Output Redirect"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious CMD Shell Output Redirect

Detects inline Windows shell commands redirecting output via the ">" symbol to a suspicious location.
This technique is sometimes used by malicious actors in order to redirect the output of reconnaissance commands such as "hostname" and "dir" to files for future exfiltration.

## Metadata

- Rule ID: 8e0bb260-d4b2-4fff-bb8d-3f82118e6892
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-12
- Modified: 2024-03-19
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_redirection_susp_folder.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_cli_1:
  CommandLine|contains:
  - '>?%APPDATA%\'
  - '>?%TEMP%\'
  - '>?%TMP%\'
  - '>?%USERPROFILE%\'
  - '>?C:\ProgramData\'
  - '>?C:\Temp\'
  - '>?C:\Users\Public\'
  - '>?C:\Windows\Temp\'
selection_cli_2:
  CommandLine|contains:
  - ' >'
  - '">'
  - '''>'
  CommandLine|contains|all:
  - C:\Users\
  - \AppData\Local\
condition: selection_img and 1 of selection_cli_*
```

## False Positives

- Legitimate admin or third party scripts used for diagnostic collection might generate some false positives

## References

- https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_redirection_susp_folder.yml)
