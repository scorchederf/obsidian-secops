---
sigma_id: "f5d19838-41b5-476c-98d8-ba8af4929ee2"
title: "LOL-Binary Copied From System Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_copy_system_dir_lolbin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_copy_system_dir_lolbin.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f5d19838-41b5-476c-98d8-ba8af4929ee2"
  - "LOL-Binary Copied From System Directory"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LOL-Binary Copied From System Directory

Detects a suspicious copy operation that tries to copy a known LOLBIN from system (System32, SysWOW64, WinSxS) directories to another on disk in order to bypass detections based on locations.

## Metadata

- Rule ID: f5d19838-41b5-476c-98d8-ba8af4929ee2
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-29
- Modified: 2025-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_susp_copy_system_dir_lolbin.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection_tools_cmd:
  Image|endswith: \cmd.exe
  CommandLine|contains: 'copy '
selection_tools_pwsh:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains:
  - copy-item
  - ' copy '
  - 'cpi '
  - ' cp '
selection_tools_other:
- Image|endswith:
  - \robocopy.exe
  - \xcopy.exe
- OriginalFileName:
  - robocopy.exe
  - XCOPY.EXE
selection_target_path:
  CommandLine|contains:
  - \System32
  - \SysWOW64
  - \WinSxS
selection_target_lolbin:
  CommandLine|contains:
  - \bitsadmin.exe
  - \calc.exe
  - \certutil.exe
  - \cmdl32.exe
  - \cscript.exe
  - \mshta.exe
  - \rundll32.exe
  - \wscript.exe
  - \ie4uinit.exe
condition: 1 of selection_tools_* and all of selection_target_*
```

## False Positives

- Unknown

## References

- https://www.hybrid-analysis.com/sample/8da5b75b6380a41eee3a399c43dfe0d99eeefaa1fd21027a07b1ecaa4cd96fdd?environmentId=120
- https://web.archive.org/web/20180331144337/https://www.fireeye.com/blog/threat-research/2018/03/sanny-malware-delivery-method-updated-in-recently-observed-attacks.html
- https://thedfirreport.com/2023/08/28/html-smuggling-leads-to-domain-wide-ransomware/
- https://www.virustotal.com/gui/file/14e722855605ba78dc1d21153f0e1be90e7528149f2cd2d7d6eba8ef27534bdc/behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_copy_system_dir_lolbin.yml)
