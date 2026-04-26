---
sigma_id: "aae1243f-d8af-40d8-ab20-33fc6d0c55bc"
title: "Suspicious Use of PsLogList"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_psloglist.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psloglist.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "aae1243f-d8af-40d8-ab20-33fc6d0c55bc"
  - "Suspicious Use of PsLogList"
attack_technique_ids:
  - "T1087"
  - "T1087.001"
  - "T1087.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Use of PsLogList

Detects usage of the PsLogList utility to dump event log in order to extract admin accounts and perform account discovery or delete events logs

## Metadata

- Rule ID: aae1243f-d8af-40d8-ab20-33fc6d0c55bc
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-12-18
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_psloglist.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087]]
- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]
- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Detection

```yaml
selection_img:
- OriginalFileName: psloglist.exe
- Image|endswith:
  - \psloglist.exe
  - \psloglist64.exe
selection_cli_eventlog:
  CommandLine|contains:
  - ' security'
  - ' application'
  - ' system'
selection_cli_flags:
  CommandLine|contains|windash:
  - ' -d'
  - ' -x'
  - ' -s'
  - ' -c'
  - ' -g'
condition: all of selection_*
```

## False Positives

- Another tool that uses the command line switches of PsLogList
- Legitimate use of PsLogList by an administrator

## References

- https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/
- https://www.cybereason.com/blog/deadringer-exposing-chinese-threat-actors-targeting-major-telcos
- https://github.com/3CORESec/MAL-CL/tree/master/Descriptors/Sysinternals/PsLogList
- https://twitter.com/EricaZelic/status/1614075109827874817

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psloglist.yml)
