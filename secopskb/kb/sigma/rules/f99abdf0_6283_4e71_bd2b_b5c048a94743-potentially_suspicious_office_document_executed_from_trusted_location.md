---
sigma_id: "f99abdf0-6283-4e71-bd2b-b5c048a94743"
title: "Potentially Suspicious Office Document Executed From Trusted Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_exec_from_trusted_locations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_exec_from_trusted_locations.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f99abdf0-6283-4e71-bd2b-b5c048a94743"
  - "Potentially Suspicious Office Document Executed From Trusted Location"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potentially Suspicious Office Document Executed From Trusted Location

Detects the execution of an Office application that points to a document that is located in a trusted location. Attackers often used this to avoid macro security and execute their malicious code.

## Metadata

- Rule ID: f99abdf0-6283-4e71-bd2b-b5c048a94743
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-21
- Modified: 2023-10-18
- Source Path: rules/windows/process_creation/proc_creation_win_office_exec_from_trusted_locations.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \explorer.exe
  - \dopus.exe
selection_img:
- Image|endswith:
  - \EXCEL.EXE
  - \POWERPNT.EXE
  - \WINWORD.exe
- OriginalFileName:
  - Excel.exe
  - POWERPNT.EXE
  - WinWord.exe
selection_trusted_location:
  CommandLine|contains:
  - \AppData\Roaming\Microsoft\Templates
  - \AppData\Roaming\Microsoft\Word\Startup\
  - \Microsoft Office\root\Templates\
  - \Microsoft Office\Templates\
filter_main_dotx:
  CommandLine|endswith:
  - .dotx
  - .xltx
  - .potx
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- Internal Research
- https://twitter.com/Max_Mal_/status/1633863678909874176
- https://techcommunity.microsoft.com/t5/microsoft-365-blog/new-security-hardening-policies-for-trusted-documents/ba-p/3023465
- https://twitter.com/_JohnHammond/status/1588155401752788994

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_exec_from_trusted_locations.yml)
