---
sigma_id: "6385697e-9f1b-40bd-8817-f4a91f40508e"
title: "PowerShell Base64 Encoded Invoke Keyword"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_base64_invoke.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_invoke.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6385697e-9f1b-40bd-8817-f4a91f40508e"
  - "PowerShell Base64 Encoded Invoke Keyword"
attack_technique_ids:
  - "T1059.001"
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PowerShell Base64 Encoded Invoke Keyword

Detects UTF-8 and UTF-16 Base64 encoded powershell 'Invoke-' calls

## Metadata

- Rule ID: 6385697e-9f1b-40bd-8817-f4a91f40508e
- Status: test
- Level: high
- Author: pH-T (Nextron Systems), Harjot Singh, @cyb3rjy0t
- Date: 2022-05-20
- Modified: 2023-04-06
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_base64_invoke.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

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
selection_cli_invoke:
  CommandLine|contains:
  - SQBuAHYAbwBrAGUALQ
  - kAbgB2AG8AawBlAC0A
  - JAG4AdgBvAGsAZQAtA
  - SW52b2tlL
  - ludm9rZS
  - JbnZva2Ut
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_invoke.yml)
