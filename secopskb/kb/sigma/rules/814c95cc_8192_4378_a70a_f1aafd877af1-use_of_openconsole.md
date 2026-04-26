---
sigma_id: "814c95cc-8192-4378-a70a-f1aafd877af1"
title: "Use of OpenConsole"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_openconsole.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_openconsole.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "814c95cc-8192-4378-a70a-f1aafd877af1"
  - "Use of OpenConsole"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use of OpenConsole

Detects usage of OpenConsole binary as a LOLBIN to launch other binaries to bypass application Whitelisting

## Metadata

- Rule ID: 814c95cc-8192-4378-a70a-f1aafd877af1
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-16
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_openconsole.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
- OriginalFileName: OpenConsole.exe
- Image|endswith: \OpenConsole.exe
filter:
  Image|startswith: C:\Program Files\WindowsApps\Microsoft.WindowsTerminal
condition: selection and not filter
```

## False Positives

- Legitimate use by an administrator

## References

- https://twitter.com/nas_bench/status/1537563834478645252

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_openconsole.yml)
