---
sigma_id: "6120ac2a-a34b-42c0-a9bd-1fb9f459f348"
title: "AddinUtil.EXE Execution From Uncommon Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_addinutil_uncommon_dir_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_dir_exec.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "6120ac2a-a34b-42c0-a9bd-1fb9f459f348"
  - "AddinUtil.EXE Execution From Uncommon Directory"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AddinUtil.EXE Execution From Uncommon Directory

Detects execution of the Add-In deployment cache updating utility (AddInutil.exe) from a non-standard directory.

## Metadata

- Rule ID: 6120ac2a-a34b-42c0-a9bd-1fb9f459f348
- Status: test
- Level: medium
- Author: Michael McKinley (@McKinleyMike), Tony Latteri (@TheLatteri)
- Date: 2023-09-18
- Modified: 2025-02-24
- Source Path: rules/windows/process_creation/proc_creation_win_addinutil_uncommon_dir_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
- Image|endswith: \addinutil.exe
- OriginalFileName: AddInUtil.exe
filter_main_legit_location:
  Image|contains:
  - :\Windows\Microsoft.NET\Framework\
  - :\Windows\Microsoft.NET\Framework64\
  - :\Windows\Microsoft.NET\FrameworkArm\
  - :\Windows\Microsoft.NET\FrameworkArm64\
  - :\Windows\WinSxS\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.blue-prints.blog/content/blog/posts/lolbin/addinutil-lolbas.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_dir_exec.yml)
