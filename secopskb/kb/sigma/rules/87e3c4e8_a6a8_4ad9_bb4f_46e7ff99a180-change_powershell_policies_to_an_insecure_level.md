---
sigma_id: "87e3c4e8-a6a8-4ad9-bb4f-46e7ff99a180"
title: "Change PowerShell Policies to an Insecure Level"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_set_policies_to_unsecure_level.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_set_policies_to_unsecure_level.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "87e3c4e8-a6a8-4ad9-bb4f-46e7ff99a180"
  - "Change PowerShell Policies to an Insecure Level"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Change PowerShell Policies to an Insecure Level

Detects changing the PowerShell script execution policy to a potentially insecure level using the "-ExecutionPolicy" flag.

## Metadata

- Rule ID: 87e3c4e8-a6a8-4ad9-bb4f-46e7ff99a180
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-11-01
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_set_policies_to_unsecure_level.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_img:
- OriginalFileName:
  - powershell_ise.exe
  - PowerShell.EXE
  - pwsh.dll
- Image|endswith:
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
selection_option:
  CommandLine|contains:
  - '-executionpolicy '
  - ' -ep '
  - ' -exec '
selection_level:
  CommandLine|contains:
  - Bypass
  - Unrestricted
filter_main_powershell_core:
  ParentImage:
  - C:\Windows\SysWOW64\msiexec.exe
  - C:\Windows\System32\msiexec.exe
  CommandLine|contains:
  - -NoProfile -ExecutionPolicy Bypass -File "C:\Program Files\PowerShell\7\
  - -NoProfile -ExecutionPolicy Bypass -File "C:\Program Files (x86)\PowerShell\7\
filter_optional_avast:
  ParentImage|contains:
  - C:\Program Files\Avast Software\Avast\
  - C:\Program Files (x86)\Avast Software\Avast\
  - \instup.exe
  CommandLine|contains:
  - -ExecutionPolicy ByPass -File "C:\Program Files\Avast Software\Avast
  - -ExecutionPolicy ByPass -File "C:\Program Files (x86)\Avast Software\Avast\
condition: all of selection_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Administrator scripts

## References

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4
- https://adsecurity.org/?p=2604
- https://thedfirreport.com/2021/11/01/from-zero-to-domain-admin/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_set_policies_to_unsecure_level.yml)
