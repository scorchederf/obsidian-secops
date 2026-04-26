---
sigma_id: "0a98a10c-685d-4ab0-bddc-b6bdd1d48458"
title: "Uncommon Userinit Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_userinit_uncommon_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_userinit_uncommon_child_processes.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0a98a10c-685d-4ab0-bddc-b6bdd1d48458"
  - "Uncommon Userinit Child Process"
attack_technique_ids:
  - "T1037.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Uncommon Userinit Child Process

Detects uncommon "userinit.exe" child processes, which could be a sign of uncommon shells or login scripts used for persistence.

## Metadata

- Rule ID: 0a98a10c-685d-4ab0-bddc-b6bdd1d48458
- Status: test
- Level: high
- Author: Tom Ueltschi (@c_APT_ure), Tim Shelton
- Date: 2019-01-12
- Modified: 2023-11-14
- Source Path: rules/windows/process_creation/proc_creation_win_userinit_uncommon_child_processes.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037.001]]

## Detection

```yaml
selection:
  ParentImage|endswith: \userinit.exe
filter_main_explorer:
  Image|endswith: :\WINDOWS\explorer.exe
filter_optional_logonscripts:
  CommandLine|contains:
  - netlogon.bat
  - UsrLogon.cmd
filter_optional_windows_core:
  CommandLine: PowerShell.exe
filter_optional_proquota:
  Image|endswith:
  - :\Windows\System32\proquota.exe
  - :\Windows\SysWOW64\proquota.exe
filter_optional_citrix:
  Image|endswith:
  - :\Program Files (x86)\Citrix\HDX\bin\cmstart.exe
  - :\Program Files (x86)\Citrix\HDX\bin\icast.exe
  - :\Program Files (x86)\Citrix\System32\icast.exe
  - :\Program Files\Citrix\HDX\bin\cmstart.exe
  - :\Program Files\Citrix\HDX\bin\icast.exe
  - :\Program Files\Citrix\System32\icast.exe
filter_optional_image_null:
  Image: null
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate logon scripts or custom shells may trigger false positives. Apply additional filters accordingly.

## References

- https://cocomelonc.github.io/persistence/2022/12/09/malware-pers-20.html
- https://learn.microsoft.com/en-us/windows-server/administration/server-core/server-core-sconfig#powershell-is-the-default-shell-on-server-core

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_userinit_uncommon_child_processes.yml)
