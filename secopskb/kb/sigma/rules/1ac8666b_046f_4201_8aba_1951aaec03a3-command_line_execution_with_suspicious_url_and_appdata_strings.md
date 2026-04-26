---
sigma_id: "1ac8666b-046f-4201-8aba-1951aaec03a3"
title: "Command Line Execution with Suspicious URL and AppData Strings"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_http_appdata.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_http_appdata.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1ac8666b-046f-4201-8aba-1951aaec03a3"
  - "Command Line Execution with Suspicious URL and AppData Strings"
attack_technique_ids:
  - "T1059.003"
  - "T1059.001"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Command Line Execution with Suspicious URL and AppData Strings

Detects a suspicious command line execution that includes an URL and AppData string in the command line parameters as used by several droppers (js/vbs > powershell)

## Metadata

- Rule ID: 1ac8666b-046f-4201-8aba-1951aaec03a3
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
- Date: 2019-01-16
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_http_appdata.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  Image|endswith: \cmd.exe
  CommandLine|contains|all:
  - http
  - ://
  - '%AppData%'
condition: selection
```

## False Positives

- High

## References

- https://www.hybrid-analysis.com/sample/3a1f01206684410dbe8f1900bbeaaa543adfcd07368ba646b499fa5274b9edf6?environmentId=100
- https://www.hybrid-analysis.com/sample/f16c729aad5c74f19784a24257236a8bbe27f7cdc4a89806031ec7f1bebbd475?environmentId=100

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_http_appdata.yml)
