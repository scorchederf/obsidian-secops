---
sigma_id: "88a87a10-384b-4ad7-8871-2f9bf9259ce5"
title: "Suspicious Regsvr32 Execution From Remote Share"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regsvr32_remote_share.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_remote_share.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "88a87a10-384b-4ad7-8871-2f9bf9259ce5"
  - "Suspicious Regsvr32 Execution From Remote Share"
attack_technique_ids:
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Regsvr32 Execution From Remote Share

Detects REGSVR32.exe to execute DLL hosted on remote shares

## Metadata

- Rule ID: 88a87a10-384b-4ad7-8871-2f9bf9259ce5
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-31
- Source Path: rules/windows/process_creation/proc_creation_win_regsvr32_remote_share.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Detection

```yaml
selection_img:
- Image|endswith: \regsvr32.exe
- OriginalFileName: \REGSVR32.EXE
selection_cli:
  CommandLine|contains: ' \\\\'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/10/31/follina-exploit-leads-to-domain-compromise/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_remote_share.yml)
