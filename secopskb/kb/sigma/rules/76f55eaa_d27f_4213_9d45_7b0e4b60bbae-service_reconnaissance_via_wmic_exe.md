---
sigma_id: "76f55eaa-d27f-4213-9d45-7b0e4b60bbae"
title: "Service Reconnaissance Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_recon_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_service.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "76f55eaa-d27f-4213-9d45-7b0e4b60bbae"
  - "Service Reconnaissance Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service Reconnaissance Via Wmic.EXE

An adversary might use WMI to check if a certain remote service is running on a remote device.
When the test completes, a service information will be displayed on the screen if it exists.
A common feedback message is that "No instance(s) Available" if the service queried is not running.
A common error message is "Node - (provided IP or default) ERROR Description =The RPC server is unavailable" if the provided remote host is unreachable

## Metadata

- Rule ID: 76f55eaa-d27f-4213-9d45-7b0e4b60bbae
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_recon_service.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_img:
- Image|endswith: \WMIC.exe
- OriginalFileName: wmic.exe
selection_cli:
  CommandLine|contains: service
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1047/T1047.md
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wmic

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_service.yml)
