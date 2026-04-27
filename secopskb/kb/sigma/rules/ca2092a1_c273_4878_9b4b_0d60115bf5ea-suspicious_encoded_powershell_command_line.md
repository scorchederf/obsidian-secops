---
sigma_id: "ca2092a1-c273-4878-9b4b-0d60115bf5ea"
title: "Suspicious Encoded PowerShell Command Line"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_base64_encoded_cmd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_encoded_cmd.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ca2092a1-c273-4878-9b4b-0d60115bf5ea"
  - "Suspicious Encoded PowerShell Command Line"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Encoded PowerShell Command Line

Detects suspicious powershell process starts with base64 encoded commands (e.g. Emotet)

## Metadata

- Rule ID: ca2092a1-c273-4878-9b4b-0d60115bf5ea
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Markus Neis, Jonhnathan Ribeiro, Daniil Yugoslavskiy, Anton Kutepov, oscd.community
- Date: 2018-09-03
- Modified: 2023-04-06
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_base64_encoded_cmd.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_cli_enc:
  CommandLine|contains: ' -e'
selection_cli_content:
  CommandLine|contains:
  - ' JAB'
  - ' SUVYI'
  - ' SQBFAFgA'
  - ' aQBlAHgA'
  - ' aWV4I'
  - ' IAA'
  - ' IAB'
  - ' UwB'
  - ' cwB'
selection_standalone:
  CommandLine|contains:
  - '.exe -ENCOD '
  - ' BA^J e-'
filter_optional_remote_signed:
  CommandLine|contains: ' -ExecutionPolicy remotesigned '
condition: selection_img and (all of selection_cli_* or selection_standalone) and
  not 1 of filter_optional_*
```

## References

- https://app.any.run/tasks/6217d77d-3189-4db2-a957-8ab239f3e01e

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_encoded_cmd.yml)
