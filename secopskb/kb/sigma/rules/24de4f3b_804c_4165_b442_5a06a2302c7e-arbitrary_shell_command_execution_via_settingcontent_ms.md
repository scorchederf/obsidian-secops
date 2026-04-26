---
sigma_id: "24de4f3b-804c-4165-b442-5a06a2302c7e"
title: "Arbitrary Shell Command Execution Via Settingcontent-Ms"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_arbitrary_shell_execution_via_settingcontent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_arbitrary_shell_execution_via_settingcontent.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "24de4f3b-804c-4165-b442-5a06a2302c7e"
  - "Arbitrary Shell Command Execution Via Settingcontent-Ms"
attack_technique_ids:
  - "T1204"
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Arbitrary Shell Command Execution Via Settingcontent-Ms

The .SettingContent-ms file type was introduced in Windows 10 and allows a user to create "shortcuts" to various Windows 10 setting pages. These files are simply XML and contain paths to various Windows 10 settings binaries.

## Metadata

- Rule ID: 24de4f3b-804c-4165-b442-5a06a2302c7e
- Status: test
- Level: medium
- Author: Sreeman
- Date: 2020-03-13
- Modified: 2022-04-14
- Source Path: rules/windows/process_creation/proc_creation_win_susp_arbitrary_shell_execution_via_settingcontent.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204]]
- [[kb/attack/techniques/T1566-phishing|T1566.001]]

## Detection

```yaml
selection:
  CommandLine|contains: .SettingContent-ms
filter:
  CommandLine|contains: immersivecontrolpanel
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://posts.specterops.io/the-tale-of-settingcontent-ms-files-f1ea253e4d39

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_arbitrary_shell_execution_via_settingcontent.yml)
