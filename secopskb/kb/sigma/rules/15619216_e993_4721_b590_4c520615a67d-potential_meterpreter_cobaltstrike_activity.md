---
sigma_id: "15619216-e993-4721-b590-4c520615a67d"
title: "Potential Meterpreter/CobaltStrike Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_meterpreter_getsystem.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_meterpreter_getsystem.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "15619216-e993-4721-b590-4c520615a67d"
  - "Potential Meterpreter/CobaltStrike Activity"
attack_technique_ids:
  - "T1134.001"
  - "T1134.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential Meterpreter/CobaltStrike Activity

Detects the use of getsystem Meterpreter/Cobalt Strike command by detecting a specific service starting

## Metadata

- Rule ID: 15619216-e993-4721-b590-4c520615a67d
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov, Ecco, Florian Roth
- Date: 2019-10-26
- Modified: 2023-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_meterpreter_getsystem.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.001]]
- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.002]]

## Detection

```yaml
selection_img:
  ParentImage|endswith: \services.exe
selection_technique_1:
  CommandLine|contains|all:
  - /c
  - echo
  - \pipe\
  CommandLine|contains:
  - cmd
  - '%COMSPEC%'
selection_technique_2:
  CommandLine|contains|all:
  - rundll32
  - .dll,a
  - '/p:'
filter_defender:
  CommandLine|contains: MpCmdRun
condition: selection_img and 1 of selection_technique_* and not 1 of filter_*
```

## False Positives

- Commandlines containing components like cmd accidentally
- Jobs and services started with cmd

## References

- https://speakerdeck.com/heirhabarov/hunting-for-privilege-escalation-in-windows-environment
- https://blog.cobaltstrike.com/2014/04/02/what-happens-when-i-type-getsystem/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_meterpreter_getsystem.yml)
