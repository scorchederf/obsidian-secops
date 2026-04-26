---
sigma_id: "e32d4572-9826-4738-b651-95fa63747e8a"
title: "Base64 Encoded PowerShell Command Detected"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_frombase64string.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_frombase64string.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e32d4572-9826-4738-b651-95fa63747e8a"
  - "Base64 Encoded PowerShell Command Detected"
attack_technique_ids:
  - "T1027"
  - "T1140"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Base64 Encoded PowerShell Command Detected

Detects usage of the "FromBase64String" function in the commandline which is used to decode a base64 encoded string

## Metadata

- Rule ID: e32d4572-9826-4738-b651-95fa63747e8a
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2020-01-29
- Modified: 2023-01-26
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_frombase64string.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  CommandLine|contains: ::FromBase64String(
condition: selection
```

## False Positives

- Administrative script libraries

## References

- https://gist.github.com/Neo23x0/6af876ee72b51676c82a2db8d2cd3639

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_frombase64string.yml)
