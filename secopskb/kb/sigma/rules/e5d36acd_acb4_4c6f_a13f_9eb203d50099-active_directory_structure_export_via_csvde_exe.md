---
sigma_id: "e5d36acd-acb4-4c6f-a13f-9eb203d50099"
title: "Active Directory Structure Export Via Csvde.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_csvde_export.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_csvde_export.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e5d36acd-acb4-4c6f-a13f-9eb203d50099"
  - "Active Directory Structure Export Via Csvde.EXE"
attack_technique_ids:
  - "T1087.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Active Directory Structure Export Via Csvde.EXE

Detects the execution of "csvde.exe" in order to export organizational Active Directory structure.

## Metadata

- Rule ID: e5d36acd-acb4-4c6f-a13f-9eb203d50099
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-14
- Source Path: rules/windows/process_creation/proc_creation_win_csvde_export.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Detection

```yaml
selection_img:
- Image|endswith: \csvde.exe
- OriginalFileName: csvde.exe
selection_remote:
  CommandLine|contains: ' -f'
filter_import:
  CommandLine|contains: ' -i'
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://www.cybereason.com/blog/research/operation-ghostshell-novel-rat-targets-global-aerospace-and-telecoms-firms
- https://web.archive.org/web/20180725233601/https://www.pwc.co.uk/cyber-security/pdf/cloud-hopper-annex-b-final.pdf
- https://businessinsights.bitdefender.com/deep-dive-into-a-backdoordiplomacy-attack-a-study-of-an-attackers-toolkit
- https://redcanary.com/blog/msix-installers/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_csvde_export.yml)
