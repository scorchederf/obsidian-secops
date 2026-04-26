---
sigma_id: "754ed792-634f-40ae-b3bc-e0448d33f695"
title: "Suspicious PowerShell Parent Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_susp_parent_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_susp_parent_process.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "754ed792-634f-40ae-b3bc-e0448d33f695"
  - "Suspicious PowerShell Parent Process"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Parent Process

Detects a suspicious or uncommon parent processes of PowerShell

## Metadata

- Rule ID: 754ed792-634f-40ae-b3bc-e0448d33f695
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov, Harish Segar
- Date: 2020-03-20
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_susp_parent_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_parent:
- ParentImage|contains: tomcat
- ParentImage|endswith:
  - \amigo.exe
  - \browser.exe
  - \chrome.exe
  - \firefox.exe
  - \httpd.exe
  - \iexplore.exe
  - \jbosssvc.exe
  - \microsoftedge.exe
  - \microsoftedgecp.exe
  - \MicrosoftEdgeSH.exe
  - \mshta.exe
  - \nginx.exe
  - \outlook.exe
  - \php-cgi.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \safari.exe
  - \services.exe
  - \sqlagent.exe
  - \sqlserver.exe
  - \sqlservr.exe
  - \vivaldi.exe
  - \w3wp.exe
selection_powershell:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- CommandLine|contains:
  - /c powershell
  - /c pwsh
- Description: Windows PowerShell
- Product: PowerShell Core 6
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
condition: all of selection_*
```

## False Positives

- Other scripts

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=26

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_susp_parent_process.yml)
