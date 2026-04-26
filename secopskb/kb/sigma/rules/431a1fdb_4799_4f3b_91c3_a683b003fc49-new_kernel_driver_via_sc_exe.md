---
sigma_id: "431a1fdb-4799-4f3b-91c3-a683b003fc49"
title: "New Kernel Driver Via SC.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_new_kernel_driver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_new_kernel_driver.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "431a1fdb-4799-4f3b-91c3-a683b003fc49"
  - "New Kernel Driver Via SC.EXE"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Kernel Driver Via SC.EXE

Detects creation of a new service (kernel driver) with the type "kernel"

## Metadata

- Rule ID: 431a1fdb-4799-4f3b-91c3-a683b003fc49
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-14
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_sc_new_kernel_driver.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
  Image|endswith: \sc.exe
  CommandLine|contains:
  - create
  - config
  CommandLine|contains|all:
  - binPath
  - type
  - kernel
filter_optional_avira_driver:
- CommandLine|contains|all:
  - create netprotection_network_filter
  - 'type= kernel start= '
  - binPath= System32\drivers\netprotection_network_filter
  - DisplayName= netprotection_network_filter
  - group= PNP_TDI tag= yes
- CommandLine|contains|all:
  - create avelam binpath=C:\Windows\system32\drivers\avelam.sys
  - type=kernel start=boot error=critical group=Early-Launch
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Rare legitimate installation of kernel drivers via sc.exe

## References

- https://www.aon.com/cyber-solutions/aon_cyber_labs/yours-truly-signed-av-driver-weaponizing-an-antivirus-driver/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_new_kernel_driver.yml)
