---
sigma_id: "4eddc365-79b4-43ff-a9d7-99422dc34b93"
title: "Use of Remote.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_remote.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_remote.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4eddc365-79b4-43ff-a9d7-99422dc34b93"
  - "Use of Remote.exe"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use of Remote.exe

Remote.exe is part of WinDbg in the Windows SDK and can be used for AWL bypass and running remote files.

## Metadata

- Rule ID: 4eddc365-79b4-43ff-a9d7-99422dc34b93
- Status: test
- Level: medium
- Author: Christopher Peacock @SecurePeacock, SCYTHE @scythe_io
- Date: 2022-06-02
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_remote.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection:
- Image|endswith: \remote.exe
- OriginalFileName: remote.exe
condition: selection
```

## False Positives

- Approved installs of Windows SDK with Debugging Tools for Windows (WinDbg).

## References

- https://blog.thecybersecuritytutor.com/Exeuction-AWL-Bypass-Remote-exe-LOLBin/
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Remote/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_remote.yml)
