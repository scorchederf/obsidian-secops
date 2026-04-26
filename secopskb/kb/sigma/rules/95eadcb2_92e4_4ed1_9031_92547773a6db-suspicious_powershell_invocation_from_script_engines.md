---
sigma_id: "95eadcb2-92e4-4ed1-9031-92547773a6db"
title: "Suspicious PowerShell Invocation From Script Engines"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_script_engine_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_script_engine_parent.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "95eadcb2-92e4-4ed1-9031-92547773a6db"
  - "Suspicious PowerShell Invocation From Script Engines"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Invocation From Script Engines

Detects suspicious powershell invocations from interpreters or unusual programs

## Metadata

- Rule ID: 95eadcb2-92e4-4ed1-9031-92547773a6db
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2019-01-16
- Modified: 2023-01-05
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_script_engine_parent.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \wscript.exe
  - \cscript.exe
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
filter_health_service:
  CurrentDirectory|contains: \Health Service State\
condition: selection and not 1 of filter_*
```

## False Positives

- Microsoft Operations Manager (MOM)
- Other scripts

## References

- https://www.securitynewspaper.com/2017/03/20/attackers-leverage-excel-powershell-dns-latest-non-malware-attack/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_script_engine_parent.yml)
