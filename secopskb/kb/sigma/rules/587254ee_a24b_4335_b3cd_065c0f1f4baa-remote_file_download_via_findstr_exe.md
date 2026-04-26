---
sigma_id: "587254ee-a24b-4335-b3cd-065c0f1f4baa"
title: "Remote File Download Via Findstr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_findstr_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_download.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "587254ee-a24b-4335-b3cd-065c0f1f4baa"
  - "Remote File Download Via Findstr.EXE"
attack_technique_ids:
  - "T1218"
  - "T1564.004"
  - "T1552.001"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote File Download Via Findstr.EXE

Detects execution of "findstr" with specific flags and a remote share path. This specific set of CLI flags would allow "findstr" to download the content of the file located on the remote share as described in the LOLBAS entry.

## Metadata

- Rule ID: 587254ee-a24b-4335-b3cd-065c0f1f4baa
- Status: test
- Level: medium
- Author: Furkan CALISKAN, @caliskanfurkan_, @oscd_initiative, Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-10-05
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_findstr_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_findstr:
- CommandLine|contains: findstr
- Image|endswith: findstr.exe
- OriginalFileName: FINDSTR.EXE
selection_cli_download_1:
  CommandLine|contains|windash: ' -v '
selection_cli_download_2:
  CommandLine|contains|windash: ' -l '
selection_cli_download_3:
  CommandLine|contains: \\\\
condition: selection_findstr and all of selection_cli_download_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Findstr/
- https://oddvar.moe/2018/04/11/putting-data-in-alternate-data-streams-and-how-to-execute-it-part-2/
- https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_download.yml)
