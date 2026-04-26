---
sigma_id: "fb843269-508c-4b76-8b8d-88679db22ce7"
title: "Suspicious Execution of Powershell with Base64"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_encode.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_encode.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "fb843269-508c-4b76-8b8d-88679db22ce7"
  - "Suspicious Execution of Powershell with Base64"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Execution of Powershell with Base64

Commandline to launch powershell with a base64 payload

## Metadata

- Rule ID: fb843269-508c-4b76-8b8d-88679db22ce7
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-02
- Modified: 2023-01-05
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_encode.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains:
  - ' -e '
  - ' -en '
  - ' -enc '
  - ' -enco'
  - ' -ec '
filter_encoding:
  CommandLine|contains: ' -Encoding '
filter_azure:
  ParentImage|contains:
  - C:\Packages\Plugins\Microsoft.GuestConfiguration.ConfigurationforWindows\
  - \gc_worker.exe
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1059.001/T1059.001.md#atomic-test-20---powershell-invoke-known-malicious-cmdlets
- https://unit42.paloaltonetworks.com/unit42-pulling-back-the-curtains-on-encodedcommand-powershell-attacks/
- https://mikefrobbins.com/2017/06/15/simple-obfuscation-with-powershell-using-base64-encoding/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_encode.yml)
