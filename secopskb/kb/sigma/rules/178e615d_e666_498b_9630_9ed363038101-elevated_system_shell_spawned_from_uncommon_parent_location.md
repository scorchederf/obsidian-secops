---
sigma_id: "178e615d-e666-498b-9630-9ed363038101"
title: "Elevated System Shell Spawned From Uncommon Parent Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_elevated_system_shell_uncommon_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_elevated_system_shell_uncommon_parent.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "178e615d-e666-498b-9630-9ed363038101"
  - "Elevated System Shell Spawned From Uncommon Parent Location"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Elevated System Shell Spawned From Uncommon Parent Location

Detects when a shell program such as the Windows command prompt or PowerShell is launched with system privileges from a uncommon parent location.

## Metadata

- Rule ID: 178e615d-e666-498b-9630-9ed363038101
- Status: test
- Level: medium
- Author: frack113, Tim Shelton (update fp)
- Date: 2022-12-05
- Modified: 2025-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_susp_elevated_system_shell_uncommon_parent.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_shell:
- Image|endswith:
  - \powershell.exe
  - \powershell_ise.exe
  - \pwsh.exe
  - \cmd.exe
- OriginalFileName:
  - PowerShell.EXE
  - powershell_ise.EXE
  - pwsh.dll
  - Cmd.Exe
selection_user:
  User|contains:
  - AUTHORI
  - AUTORI
  LogonId: '0x3e7'
filter_main_generic:
  ParentImage|contains:
  - :\Program Files (x86)\
  - :\Program Files\
  - :\ProgramData\
  - :\Windows\System32\
  - :\Windows\SysWOW64\
  - :\Windows\Temp\
  - :\Windows\WinSxS\
filter_optional_manageengine:
  ParentImage|endswith: :\ManageEngine\ADManager Plus\pgsql\bin\postgres.exe
  Image|endswith: \cmd.exe
filter_optional_asgard:
  CommandLine|contains: :\WINDOWS\system32\cmd.exe /c "
  CurrentDirectory|contains: :\WINDOWS\Temp\asgard2-agent\
filter_optional_ibm_spectrumprotect:
  ParentImage|contains: :\IBM\SpectrumProtect\webserver\scripts\
  CommandLine|contains: :\IBM\SpectrumProtect\webserver\scripts\
filter_main_parent_null:
  ParentImage: null
filter_main_parent_empty:
  ParentImage:
  - ''
  - '-'
condition: all of selection_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Some legitimate applications may spawn shells from uncommon parent locations. Apply additional filters and perform an initial baseline before deploying.

## References

- https://github.com/Wh04m1001/SysmonEoP

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_elevated_system_shell_uncommon_parent.yml)
