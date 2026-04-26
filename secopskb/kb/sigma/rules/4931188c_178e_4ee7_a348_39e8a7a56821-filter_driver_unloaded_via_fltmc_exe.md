---
sigma_id: "4931188c-178e-4ee7-a348-39e8a7a56821"
title: "Filter Driver Unloaded Via Fltmc.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_fltmc_unload_driver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fltmc_unload_driver.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4931188c-178e-4ee7-a348-39e8a7a56821"
  - "Filter Driver Unloaded Via Fltmc.EXE"
attack_technique_ids:
  - "T1070"
  - "T1562"
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Filter Driver Unloaded Via Fltmc.EXE

Detect filter driver unloading activity via fltmc.exe

## Metadata

- Rule ID: 4931188c-178e-4ee7-a348-39e8a7a56821
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-13
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_fltmc_unload_driver.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Detection

```yaml
selection_img:
- Image|endswith: \fltMC.exe
- OriginalFileName: fltMC.exe
selection_cli:
  CommandLine|contains: unload
filter_optional_avira:
  ParentImage|contains:
  - \AppData\Local\Temp\
  - :\Windows\Temp\
  ParentImage|endswith: \endpoint-protection-installer-x64.tmp
  CommandLine|endswith:
  - unload rtp_filesystem_filter
  - unload rtp_filter
filter_optional_manageengine:
  ParentImage: C:\Program Files (x86)\ManageEngine\uems_agent\bin\dcfaservice64.exe
  CommandLine|endswith: unload DFMFilter
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://www.darkoperator.com/blog/2018/10/5/operating-offensively-against-sysmon
- https://www.cybereason.com/blog/threat-analysis-report-lockbit-2.0-all-paths-lead-to-ransom

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fltmc_unload_driver.yml)
