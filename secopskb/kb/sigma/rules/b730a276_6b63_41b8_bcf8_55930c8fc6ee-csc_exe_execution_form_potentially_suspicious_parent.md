---
sigma_id: "b730a276-6b63-41b8-bcf8-55930c8fc6ee"
title: "Csc.EXE Execution Form Potentially Suspicious Parent"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_csc_susp_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_csc_susp_parent.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b730a276-6b63-41b8-bcf8-55930c8fc6ee"
  - "Csc.EXE Execution Form Potentially Suspicious Parent"
attack_technique_ids:
  - "T1059.005"
  - "T1059.007"
  - "T1218.005"
  - "T1027.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Csc.EXE Execution Form Potentially Suspicious Parent

Detects a potentially suspicious parent of "csc.exe", which could be a sign of payload delivery.

## Metadata

- Rule ID: b730a276-6b63-41b8-bcf8-55930c8fc6ee
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems), X__Junior (Nextron Systems)
- Date: 2019-02-11
- Modified: 2024-05-27
- Source Path: rules/windows/process_creation/proc_creation_win_csc_susp_parent.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.005]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.004]]

## Detection

```yaml
selection_img:
- Image|endswith: \csc.exe
- OriginalFileName: csc.exe
selection_parent_generic:
  ParentImage|endswith:
  - \cscript.exe
  - \excel.exe
  - \mshta.exe
  - \onenote.exe
  - \outlook.exe
  - \powerpnt.exe
  - \winword.exe
  - \wscript.exe
selection_parent_powershell:
  ParentImage|endswith:
  - \powershell.exe
  - \pwsh.exe
  ParentCommandLine|contains:
  - '-Encoded '
  - FromBase64String
selection_parent_susp_location:
- ParentCommandLine|re: ([Pp]rogram[Dd]ata|%([Ll]ocal)?[Aa]pp[Dd]ata%|\\[Aa]pp[Dd]ata\\([Ll]ocal([Ll]ow)?|[Rr]oaming))\\[^\\]{1,256}$
- ParentCommandLine|contains:
  - :\PerfLogs\
  - :\Users\Public\
  - :\Windows\Temp\
  - \Temporary Internet
- ParentCommandLine|contains|all:
  - :\Users\
  - \Favorites\
- ParentCommandLine|contains|all:
  - :\Users\
  - \Favourites\
- ParentCommandLine|contains|all:
  - :\Users\
  - \Contacts\
- ParentCommandLine|contains|all:
  - :\Users\
  - \Pictures\
filter_main_programfiles:
  ParentImage|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
filter_main_sdiagnhost:
  ParentImage: C:\Windows\System32\sdiagnhost.exe
filter_main_w3p:
  ParentImage: C:\Windows\System32\inetsrv\w3wp.exe
filter_optional_chocolatey:
  ParentImage: C:\ProgramData\chocolatey\choco.exe
filter_optional_defender:
  ParentCommandLine|contains: \ProgramData\Microsoft\Windows Defender Advanced Threat
    Protection
filter_optional_ansible:
  ParentCommandLine|contains:
  - JwB7ACIAZgBhAGkAbABlAGQAIgA6AHQAcgB1AGUALAAiAG0AcwBnACIAOgAiAEEAbgBzAGkAYgBsAGUAIAByAGUAcQB1AGkAcgBlAHMAIABQAG8AdwBlAHIAUwBoAGUAbABsACAAdgAzAC4AMAAgAG8AcgAgAG4AZQB3AGUAcgAiAH0AJw
  - cAewAiAGYAYQBpAGwAZQBkACIAOgB0AHIAdQBlACwAIgBtAHMAZwAiADoAIgBBAG4AcwBpAGIAbABlACAAcgBlAHEAdQBpAHIAZQBzACAAUABvAHcAZQByAFMAaABlAGwAbAAgAHYAMwAuADAAIABvAHIAIABuAGUAdwBlAHIAIgB9ACcA
  - nAHsAIgBmAGEAaQBsAGUAZAAiADoAdAByAHUAZQAsACIAbQBzAGcAIgA6ACIAQQBuAHMAaQBiAGwAZQAgAHIAZQBxAHUAaQByAGUAcwAgAFAAbwB3AGUAcgBTAGgAZQBsAGwAIAB2ADMALgAwACAAbwByACAAbgBlAHcAZQByACIAfQAnA
condition: selection_img and 1 of selection_parent_* and not 1 of filter_main_* and
  not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://www.uptycs.com/blog/warzonerat-can-now-evade-with-process-hollowing
- https://reaqta.com/2017/11/short-journey-darkvnc/
- https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_csc_susp_parent.yml)
