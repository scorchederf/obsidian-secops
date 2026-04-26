---
sigma_id: "4f2cd9b6-4a17-440f-bb2a-687abb65993a"
title: "Uncommon AddinUtil.EXE CommandLine Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_addinutil_uncommon_cmdline.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_cmdline.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4f2cd9b6-4a17-440f-bb2a-687abb65993a"
  - "Uncommon AddinUtil.EXE CommandLine Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon AddinUtil.EXE CommandLine Execution

Detects execution of the Add-In deployment cache updating utility (AddInutil.exe) with uncommon Addinroot or Pipelineroot paths. An adversary may execute AddinUtil.exe with uncommon Addinroot/Pipelineroot paths that point to the adversaries Addins.Store payload.

## Metadata

- Rule ID: 4f2cd9b6-4a17-440f-bb2a-687abb65993a
- Status: test
- Level: medium
- Author: Michael McKinley (@McKinleyMike), Tony Latteri (@TheLatteri)
- Date: 2023-09-18
- Source Path: rules/windows/process_creation/proc_creation_win_addinutil_uncommon_cmdline.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \addinutil.exe
- OriginalFileName: AddInUtil.exe
selection_cli:
  CommandLine|contains:
  - '-AddInRoot:'
  - '-PipelineRoot:'
filter_main_addinroot:
  CommandLine|contains:
  - -AddInRoot:"C:\Program Files (x86)\Common Files\Microsoft Shared\VSTA
  - -AddInRoot:C:\Program Files (x86)\Common Files\Microsoft Shared\VSTA
  - -PipelineRoot:"C:\Program Files (x86)\Common Files\Microsoft Shared\VSTA
  - -PipelineRoot:C:\Program Files (x86)\Common Files\Microsoft Shared\VSTA
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.blue-prints.blog/content/blog/posts/lolbin/addinutil-lolbas.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_uncommon_cmdline.yml)
