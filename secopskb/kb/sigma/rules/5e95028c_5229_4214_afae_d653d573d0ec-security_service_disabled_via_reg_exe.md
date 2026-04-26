---
sigma_id: "5e95028c-5229-4214-afae-d653d573d0ec"
title: "Security Service Disabled Via Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_disable_sec_services.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_disable_sec_services.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5e95028c-5229-4214-afae-d653d573d0ec"
  - "Security Service Disabled Via Reg.EXE"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Security Service Disabled Via Reg.EXE

Detects execution of "reg.exe" to disable security services such as Windows Defender.

## Metadata

- Rule ID: 5e95028c-5229-4214-afae-d653d573d0ec
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), John Lambert (idea), elhoim
- Date: 2021-07-14
- Modified: 2023-06-05
- Source Path: rules/windows/process_creation/proc_creation_win_reg_disable_sec_services.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_reg_add:
  CommandLine|contains|all:
  - reg
  - add
selection_cli_reg_start:
  CommandLine|contains|all:
  - d 4
  - v Start
  CommandLine|contains:
  - \AppIDSvc
  - \MsMpSvc
  - \NisSrv
  - \SecurityHealthService
  - \Sense
  - \UsoSvc
  - \WdBoot
  - \WdFilter
  - \WdNisDrv
  - \WdNisSvc
  - \WinDefend
  - \wscsvc
  - \wuauserv
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://twitter.com/JohnLaTwC/status/1415295021041979392
- https://github.com/gordonbay/Windows-On-Reins/blob/e587ac7a0407847865926d575e3c46f68cf7c68d/wor.ps1
- https://vms.drweb.fr/virus/?i=24144899
- https://bidouillesecurity.com/disable-windows-defender-in-powershell/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_disable_sec_services.yml)
