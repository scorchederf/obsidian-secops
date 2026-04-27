---
sigma_id: "396f6630-f3ac-44e3-bfc8-1b161bc00c4e"
title: "Suspicious Child Process Of Wermgr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wermgr_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wermgr_susp_child_process.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "396f6630-f3ac-44e3-bfc8-1b161bc00c4e"
  - "Suspicious Child Process Of Wermgr.EXE"
attack_technique_ids:
  - "T1055"
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Child Process Of Wermgr.EXE

Detects suspicious Windows Error Reporting manager (wermgr.exe) child process

## Metadata

- Rule ID: 396f6630-f3ac-44e3-bfc8-1b161bc00c4e
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-10-14
- Modified: 2024-08-29
- Source Path: rules/windows/process_creation/proc_creation_win_wermgr_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]
- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
  ParentImage|endswith: \wermgr.exe
  Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \ipconfig.exe
  - \mshta.exe
  - \net.exe
  - \net1.exe
  - \netstat.exe
  - \nslookup.exe
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \systeminfo.exe
  - \whoami.exe
  - \wscript.exe
filter_main_rundll32:
  Image|endswith: \rundll32.exe
  CommandLine|contains|all:
  - C:\Windows\system32\WerConCpl.dll
  - 'LaunchErcApp '
  CommandLine|contains:
  - -queuereporting
  - -responsepester
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html
- https://www.echotrail.io/insights/search/wermgr.exe
- https://github.com/binderlabs/DirCreate2System

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wermgr_susp_child_process.yml)
