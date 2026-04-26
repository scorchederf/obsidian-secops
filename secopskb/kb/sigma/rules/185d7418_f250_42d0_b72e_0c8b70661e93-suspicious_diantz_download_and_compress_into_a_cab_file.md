---
sigma_id: "185d7418-f250-42d0-b72e-0c8b70661e93"
title: "Suspicious Diantz Download and Compress Into a CAB File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_diantz_remote_cab.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_diantz_remote_cab.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "185d7418-f250-42d0-b72e-0c8b70661e93"
  - "Suspicious Diantz Download and Compress Into a CAB File"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Diantz Download and Compress Into a CAB File

Download and compress a remote file and store it in a cab file on local machine.

## Metadata

- Rule ID: 185d7418-f250-42d0-b72e-0c8b70661e93
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-11-26
- Modified: 2022-08-13
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_diantz_remote_cab.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - diantz.exe
  - ' \\\\'
  - .cab
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Diantz/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_diantz_remote_cab.yml)
