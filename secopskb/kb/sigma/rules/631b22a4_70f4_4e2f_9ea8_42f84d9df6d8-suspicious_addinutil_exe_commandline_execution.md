---
sigma_id: "631b22a4-70f4-4e2f-9ea8-42f84d9df6d8"
title: "Suspicious AddinUtil.EXE CommandLine Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_addinutil_suspicious_cmdline.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_suspicious_cmdline.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "631b22a4-70f4-4e2f-9ea8-42f84d9df6d8"
  - "Suspicious AddinUtil.EXE CommandLine Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious AddinUtil.EXE CommandLine Execution

Detects execution of the Add-In deployment cache updating utility (AddInutil.exe) with suspicious Addinroot or Pipelineroot paths. An adversary may execute AddinUtil.exe with uncommon Addinroot/Pipelineroot paths that point to the adversaries Addins.Store payload.

## Metadata

- Rule ID: 631b22a4-70f4-4e2f-9ea8-42f84d9df6d8
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Michael McKinley (@McKinleyMike), Tony Latteri (@TheLatteri)
- Date: 2023-09-18
- Source Path: rules/windows/process_creation/proc_creation_win_addinutil_suspicious_cmdline.yml

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
selection_susp_1_flags:
  CommandLine|contains:
  - '-AddInRoot:'
  - '-PipelineRoot:'
selection_susp_1_paths:
  CommandLine|contains:
  - \AppData\Local\Temp\
  - \Desktop\
  - \Downloads\
  - \Users\Public\
  - \Windows\Temp\
selection_susp_2:
  CommandLine|contains:
  - -AddInRoot:.
  - -AddInRoot:"."
  - -PipelineRoot:.
  - -PipelineRoot:"."
  CurrentDirectory|contains:
  - \AppData\Local\Temp\
  - \Desktop\
  - \Downloads\
  - \Users\Public\
  - \Windows\Temp\
condition: selection_img and (all of selection_susp_1_* or selection_susp_2)
```

## False Positives

- Unknown

## References

- https://www.blue-prints.blog/content/blog/posts/lolbin/addinutil-lolbas.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_addinutil_suspicious_cmdline.yml)
