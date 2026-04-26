---
sigma_id: "b17ea6f7-6e90-447e-a799-e6c0a493d6ce"
title: "Shadow Copies Creation Using Operating Systems Utilities"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_shadow_copies_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_shadow_copies_creation.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b17ea6f7-6e90-447e-a799-e6c0a493d6ce"
  - "Shadow Copies Creation Using Operating Systems Utilities"
attack_technique_ids:
  - "T1003"
  - "T1003.002"
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Shadow Copies Creation Using Operating Systems Utilities

Shadow Copies creation using operating systems utilities, possible credential access

## Metadata

- Rule ID: b17ea6f7-6e90-447e-a799-e6c0a493d6ce
- Status: test
- Level: medium
- Author: Teymur Kheirkhabarov, Daniil Yugoslavskiy, oscd.community
- Date: 2019-10-22
- Modified: 2022-11-10
- Source Path: rules/windows/process_creation/proc_creation_win_susp_shadow_copies_creation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \wmic.exe
  - \vssadmin.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
  - wmic.exe
  - VSSADMIN.EXE
selection_cli:
  CommandLine|contains|all:
  - shadow
  - create
condition: all of selection_*
```

## False Positives

- Legitimate administrator working with shadow copies, access for backup purposes

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment
- https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/tutorial-for-ntds-goodness-vssadmin-wmis-ntdsdit-system/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_shadow_copies_creation.yml)
