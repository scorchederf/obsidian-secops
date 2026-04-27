---
sigma_id: "85b0b087-eddf-4a2b-b033-d771fa2b9775"
title: "PowerShell Download and Execution Cradles"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_download_iex.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_download_iex.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "85b0b087-eddf-4a2b-b033-d771fa2b9775"
  - "PowerShell Download and Execution Cradles"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PowerShell Download and Execution Cradles

Detects PowerShell download and execution cradles.

## Metadata

- Rule ID: 85b0b087-eddf-4a2b-b033-d771fa2b9775
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-24
- Modified: 2025-07-18
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_download_iex.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_download:
  CommandLine|contains:
  - .DownloadString(
  - .DownloadFile(
  - 'Invoke-WebRequest '
  - 'iwr '
  - 'Invoke-RestMethod '
  - 'irm '
selection_iex:
  CommandLine|contains:
  - ;iex $
  - '| IEX'
  - '|IEX '
  - I`E`X
  - I`EX
  - IE`X
  - 'iex '
  - IEX (
  - IEX(
  - Invoke-Expression
condition: all of selection_*
```

## False Positives

- Some PowerShell installers were seen using similar combinations. Apply filters accordingly

## References

- https://github.com/VirtualAlllocEx/Payload-Download-Cradles/blob/88e8eca34464a547c90d9140d70e9866dcbc6a12/Download-Cradles.cmd
- https://labs.withsecure.com/publications/fin7-target-veeam-servers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_download_iex.yml)
