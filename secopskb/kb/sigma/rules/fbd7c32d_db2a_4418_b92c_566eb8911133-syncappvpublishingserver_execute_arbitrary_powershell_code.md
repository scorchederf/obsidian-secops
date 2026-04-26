---
sigma_id: "fbd7c32d-db2a-4418-b92c-566eb8911133"
title: "SyncAppvPublishingServer Execute Arbitrary PowerShell Code"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_execute_psh.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_execute_psh.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "fbd7c32d-db2a-4418-b92c-566eb8911133"
  - "SyncAppvPublishingServer Execute Arbitrary PowerShell Code"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# SyncAppvPublishingServer Execute Arbitrary PowerShell Code

Executes arbitrary PowerShell code using SyncAppvPublishingServer.exe.

## Metadata

- Rule ID: fbd7c32d-db2a-4418-b92c-566eb8911133
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-12
- Modified: 2022-10-04
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_execute_psh.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \SyncAppvPublishingServer.exe
- OriginalFileName: syncappvpublishingserver.exe
selection_cli:
  CommandLine|contains: '"n; '
condition: all of selection_*
```

## False Positives

- App-V clients

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T1218.md
- https://lolbas-project.github.io/lolbas/Binaries/Syncappvpublishingserver/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_execute_psh.yml)
