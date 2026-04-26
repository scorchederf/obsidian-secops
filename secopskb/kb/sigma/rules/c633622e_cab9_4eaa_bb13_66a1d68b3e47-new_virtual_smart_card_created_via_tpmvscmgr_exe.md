---
sigma_id: "c633622e-cab9-4eaa-bb13-66a1d68b3e47"
title: "New Virtual Smart Card Created Via TpmVscMgr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_tpmvscmgr_add_virtual_smartcard.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tpmvscmgr_add_virtual_smartcard.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c633622e-cab9-4eaa-bb13-66a1d68b3e47"
  - "New Virtual Smart Card Created Via TpmVscMgr.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Virtual Smart Card Created Via TpmVscMgr.EXE

Detects execution of "Tpmvscmgr.exe" to create a new virtual smart card.

## Metadata

- Rule ID: c633622e-cab9-4eaa-bb13-66a1d68b3e47
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-15
- Source Path: rules/windows/process_creation/proc_creation_win_tpmvscmgr_add_virtual_smartcard.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
  Image|endswith: \tpmvscmgr.exe
  OriginalFileName: TpmVscMgr.exe
selection_cli:
  CommandLine|contains: create
condition: all of selection_*
```

## False Positives

- Legitimate usage by an administrator

## References

- https://learn.microsoft.com/en-us/windows/security/identity-protection/virtual-smart-cards/virtual-smart-card-tpmvscmgr

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tpmvscmgr_add_virtual_smartcard.yml)
