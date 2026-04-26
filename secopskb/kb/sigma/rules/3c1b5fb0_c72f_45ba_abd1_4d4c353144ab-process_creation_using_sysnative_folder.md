---
sigma_id: "3c1b5fb0-c72f-45ba-abd1-4d4c353144ab"
title: "Process Creation Using Sysnative Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_sysnative.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_sysnative.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3c1b5fb0-c72f-45ba-abd1-4d4c353144ab"
  - "Process Creation Using Sysnative Folder"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Process Creation Using Sysnative Folder

Detects process creation events that use the Sysnative folder (common for CobaltStrike spawns)

## Metadata

- Rule ID: 3c1b5fb0-c72f-45ba-abd1-4d4c353144ab
- Status: test
- Level: medium
- Author: Max Altgelt (Nextron Systems)
- Date: 2022-08-23
- Modified: 2025-10-08
- Source Path: rules/windows/process_creation/proc_creation_win_susp_sysnative.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection:
- CommandLine|contains: :\Windows\Sysnative\
- Image|contains: :\Windows\Sysnative\
filter_main_ngen:
  Image|contains:
  - C:\Windows\Microsoft.NET\Framework64\v
  - C:\Windows\Microsoft.NET\Framework\v
  - C:\Windows\Microsoft.NET\FrameworkArm\v
  - C:\Windows\Microsoft.NET\FrameworkArm64\v
  Image|endswith: \ngen.exe
  CommandLine|contains: install
filter_optional_xampp:
  CommandLine|contains|all:
  - '"C:\Windows\sysnative\cmd.exe"'
  - \xampp\
  - \catalina_start.bat
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_sysnative.yml)
