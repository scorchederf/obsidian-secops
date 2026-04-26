---
sigma_id: "fff9d2b7-e11c-4a69-93d3-40ef66189767"
title: "Suspicious Copy From or To System Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_copy_system_dir.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_copy_system_dir.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "fff9d2b7-e11c-4a69-93d3-40ef66189767"
  - "Suspicious Copy From or To System Directory"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Copy From or To System Directory

Detects a suspicious copy operation that tries to copy a program from system (System32, SysWOW64, WinSxS) directories to another on disk.
Often used to move LOLBINs such as 'certutil' or 'desktopimgdownldr' to a different location with a different name in order to bypass detections based on locations.

## Metadata

- Rule ID: fff9d2b7-e11c-4a69-93d3-40ef66189767
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Markus Neis, Tim Shelton (HAWK.IO), Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-07-03
- Modified: 2025-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_susp_copy_system_dir.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection_img_cmd:
  Image|endswith: \cmd.exe
  CommandLine|contains: 'copy '
selection_img_pwsh:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains:
  - copy-item
  - ' copy '
  - 'cpi '
  - ' cp '
selection_img_other:
- Image|endswith:
  - \robocopy.exe
  - \xcopy.exe
- OriginalFileName:
  - robocopy.exe
  - XCOPY.EXE
selection_target:
  CommandLine|re|i: \s['"]?C:\\Windows\\(System32|SysWOW64|WinSxS)
filter_optional_avira:
  Image|endswith: \cmd.exe
  CommandLine|contains|all:
  - /c copy
  - \Temp\
  - \avira_system_speedup.exe
  CommandLine|contains:
  - C:\Program Files\Avira\
  - C:\Program Files (x86)\Avira\
condition: 1 of selection_img_* and selection_target and not 1 of filter_optional_*
```

## False Positives

- Depend on scripts and administrative tools used in the monitored environment (For example an admin scripts like https://www.itexperience.net/sccm-batch-files-and-32-bits-processes-on-64-bits-os/)
- When cmd.exe and xcopy.exe are called directly
- When the command contains the keywords but not in the correct order

## References

- https://www.hybrid-analysis.com/sample/8da5b75b6380a41eee3a399c43dfe0d99eeefaa1fd21027a07b1ecaa4cd96fdd?environmentId=120
- https://web.archive.org/web/20180331144337/https://www.fireeye.com/blog/threat-research/2018/03/sanny-malware-delivery-method-updated-in-recently-observed-attacks.html
- https://thedfirreport.com/2023/08/28/html-smuggling-leads-to-domain-wide-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_copy_system_dir.yml)
