---
sigma_id: "68bcd73b-37ef-49cb-95fc-edc809730be6"
title: "Potential Unquoted Service Path Reconnaissance Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_recon_unquoted_service_search.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_unquoted_service_search.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "68bcd73b-37ef-49cb-95fc-edc809730be6"
  - "Potential Unquoted Service Path Reconnaissance Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Unquoted Service Path Reconnaissance Via Wmic.EXE

Detects known WMI recon method to look for unquoted service paths using wmic. Often used by pentester and attacker enumeration scripts

## Metadata

- Rule ID: 68bcd73b-37ef-49cb-95fc-edc809730be6
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-20
- Modified: 2023-09-11
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_recon_unquoted_service_search.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_img:
- OriginalFileName: wmic.exe
- Image|endswith: \WMIC.exe
selection_cli:
  CommandLine|contains|all:
  - ' service get '
  - name,displayname,pathname,startmode
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/nccgroup/redsnarf/blob/35949b30106ae543dc6f2bc3f1be10c6d9a8d40e/redsnarf.py
- https://github.com/S3cur3Th1sSh1t/Creds/blob/eac23d67f7f90c7fc8e3130587d86158c22aa398/PowershellScripts/jaws-enum.ps1
- https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_unquoted_service_search.yml)
