---
sigma_id: "6a69f62d-ce75-4b57-8dce-6351eb55b362"
title: "Esentutl Steals Browser Information"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_esentutl_webcache.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_esentutl_webcache.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "6a69f62d-ce75-4b57-8dce-6351eb55b362"
  - "Esentutl Steals Browser Information"
attack_technique_ids:
  - "T1005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Esentutl Steals Browser Information

One way Qbot steals sensitive information is by extracting browser data from Internet Explorer and Microsoft Edge by using the built-in utility esentutl.exe

## Metadata

- Rule ID: 6a69f62d-ce75-4b57-8dce-6351eb55b362
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-13
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_esentutl_webcache.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1005-data_from_local_system|T1005]]

## Detection

```yaml
selection_img:
- Image|endswith: \esentutl.exe
- OriginalFileName: esentutl.exe
selection_flag:
  CommandLine|contains|windash: -r
selection_webcache:
  CommandLine|contains: \Windows\WebCache
condition: all of selection*
```

## False Positives

- Legitimate use

## References

- https://thedfirreport.com/2022/02/07/qbot-likes-to-move-it-move-it/
- https://redcanary.com/threat-detection-report/threats/qbot/
- https://thedfirreport.com/2022/10/31/follina-exploit-leads-to-domain-compromise/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_esentutl_webcache.yml)
