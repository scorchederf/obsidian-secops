---
sigma_id: "05a2ab7e-ce11-4b63-86db-ab32e763e11d"
title: "MMC Spawning Windows Shell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mmc_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mmc_susp_child_process.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "05a2ab7e-ce11-4b63-86db-ab32e763e11d"
  - "MMC Spawning Windows Shell"
attack_technique_ids:
  - "T1021.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MMC Spawning Windows Shell

Detects a Windows command line executable started from MMC

## Metadata

- Rule ID: 05a2ab7e-ce11-4b63-86db-ab32e763e11d
- Status: test
- Level: high
- Author: Karneades, Swisscom CSIRT
- Date: 2019-08-05
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_mmc_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.003]]

## Detection

```yaml
selection1:
  ParentImage|endswith: \mmc.exe
selection2:
- Image|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
  - \wscript.exe
  - \cscript.exe
  - \sh.exe
  - \bash.exe
  - \reg.exe
  - \regsvr32.exe
- Image|contains: \BITSADMIN
condition: all of selection*
```

## References

- https://enigma0x3.net/2017/01/05/lateral-movement-using-the-mmc20-application-com-object/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mmc_susp_child_process.yml)
