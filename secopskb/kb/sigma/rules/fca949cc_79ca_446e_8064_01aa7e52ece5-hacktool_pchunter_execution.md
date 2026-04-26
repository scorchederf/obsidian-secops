---
sigma_id: "fca949cc-79ca-446e-8064-01aa7e52ece5"
title: "HackTool - PCHunter Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_pchunter.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_pchunter.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "fca949cc-79ca-446e-8064-01aa7e52ece5"
  - "HackTool - PCHunter Execution"
attack_technique_ids:
  - "T1082"
  - "T1057"
  - "T1012"
  - "T1083"
  - "T1007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - PCHunter Execution

Detects suspicious use of PCHunter, a tool like Process Hacker to view and manipulate processes, kernel options and other low level stuff

## Metadata

- Rule ID: fca949cc-79ca-446e-8064-01aa7e52ece5
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali
- Date: 2022-10-10
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_pchunter.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]
- [[kb/attack/techniques/T1057-process_discovery|T1057]]
- [[kb/attack/techniques/T1012-query_registry|T1012]]
- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]
- [[kb/attack/techniques/T1007-system_service_discovery|T1007]]

## Detection

```yaml
selection_image:
  Image|endswith:
  - \PCHunter64.exe
  - \PCHunter32.exe
selection_pe:
- OriginalFileName: PCHunter.exe
- Description: Epoolsoft Windows Information View Tools
selection_hashes:
  Hashes|contains:
  - SHA1=5F1CBC3D99558307BC1250D084FA968521482025
  - MD5=987B65CD9B9F4E9A1AFD8F8B48CF64A7
  - SHA256=2B214BDDAAB130C274DE6204AF6DBA5AEEC7433DA99AA950022FA306421A6D32
  - IMPHASH=444D210CEA1FF8112F256A4997EED7FF
  - SHA1=3FB89787CB97D902780DA080545584D97FB1C2EB
  - MD5=228DD0C2E6287547E26FFBD973A40F14
  - SHA256=55F041BF4E78E9BFA6D4EE68BE40E496CE3A1353E1CA4306598589E19802522C
  - IMPHASH=0479F44DF47CFA2EF1CCC4416A538663
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://web.archive.org/web/20231210115125/http://www.xuetr.com/
- https://www.crowdstrike.com/blog/falcon-overwatch-report-finds-increase-in-ecrime/
- https://www.hexacorn.com/blog/2018/04/20/kernel-hacking-tool-you-might-have-never-heard-of-xuetr-pchunter/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_pchunter.yml)
