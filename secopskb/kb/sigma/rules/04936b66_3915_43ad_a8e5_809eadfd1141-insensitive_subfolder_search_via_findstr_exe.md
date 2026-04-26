---
sigma_id: "04936b66-3915-43ad-a8e5-809eadfd1141"
title: "Insensitive Subfolder Search Via Findstr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_findstr_subfolder_search.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_subfolder_search.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "04936b66-3915-43ad-a8e5-809eadfd1141"
  - "Insensitive Subfolder Search Via Findstr.EXE"
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

# Insensitive Subfolder Search Via Findstr.EXE

Detects execution of findstr with the "s" and "i" flags for a "subfolder" and "insensitive" search respectively. Attackers sometimes leverage this built-in utility to search the system for interesting files or filter through results of commands.

## Metadata

- Rule ID: 04936b66-3915-43ad-a8e5-809eadfd1141
- Status: test
- Level: low
- Author: Furkan CALISKAN, @caliskanfurkan_, @oscd_initiative, Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-10-05
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_findstr_subfolder_search.yml

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
selection_cli_search_subfolder:
  CommandLine|contains|windash: ' -s '
selection_cli_search_insensitive:
  CommandLine|contains|windash: ' -i '
condition: selection_findstr and all of selection_cli_search_*
```

## False Positives

- Administrative or software activity

## References

- https://lolbas-project.github.io/lolbas/Binaries/Findstr/
- https://oddvar.moe/2018/04/11/putting-data-in-alternate-data-streams-and-how-to-execute-it-part-2/
- https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_subfolder_search.yml)
