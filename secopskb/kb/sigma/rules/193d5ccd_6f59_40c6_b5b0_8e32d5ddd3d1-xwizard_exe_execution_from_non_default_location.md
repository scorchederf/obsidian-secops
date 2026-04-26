---
sigma_id: "193d5ccd-6f59-40c6-b5b0-8e32d5ddd3d1"
title: "Xwizard.EXE Execution From Non-Default Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_xwizard_execution_non_default_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_xwizard_execution_non_default_location.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "193d5ccd-6f59-40c6-b5b0-8e32d5ddd3d1"
  - "Xwizard.EXE Execution From Non-Default Location"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Xwizard.EXE Execution From Non-Default Location

Detects the execution of Xwizard tool from a non-default directory.
When executed from a non-default directory, this utility can be abused in order to side load a custom version of "xwizards.dll".

## Metadata

- Rule ID: 193d5ccd-6f59-40c6-b5b0-8e32d5ddd3d1
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-09-20
- Modified: 2024-08-15
- Source Path: rules/windows/process_creation/proc_creation_win_xwizard_execution_non_default_location.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
- Image|endswith: \xwizard.exe
- OriginalFileName: xwizard.exe
filter_main_legit_location:
  Image|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Windows installed on non-C drive

## References

- https://lolbas-project.github.io/lolbas/Binaries/Xwizard/
- http://www.hexacorn.com/blog/2017/07/31/the-wizard-of-x-oppa-plugx-style/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_xwizard_execution_non_default_location.yml)
