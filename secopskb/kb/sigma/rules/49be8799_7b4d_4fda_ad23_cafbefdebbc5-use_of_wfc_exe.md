---
sigma_id: "49be8799-7b4d-4fda-ad23-cafbefdebbc5"
title: "Use of Wfc.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_wfc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_wfc.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "49be8799-7b4d-4fda-ad23-cafbefdebbc5"
  - "Use of Wfc.exe"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use of Wfc.exe

The Workflow Command-line Compiler can be used for AWL bypass and is listed in Microsoft's recommended block rules.

## Metadata

- Rule ID: 49be8799-7b4d-4fda-ad23-cafbefdebbc5
- Status: test
- Level: medium
- Author: Christopher Peacock @SecurePeacock, SCYTHE @scythe_io
- Date: 2022-06-01
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_wfc.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection:
- Image|endswith: \wfc.exe
- OriginalFileName: wfc.exe
condition: selection
```

## False Positives

- Legitimate use by a software developer

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Wfc/
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/design/applications-that-can-bypass-wdac

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_wfc.yml)
