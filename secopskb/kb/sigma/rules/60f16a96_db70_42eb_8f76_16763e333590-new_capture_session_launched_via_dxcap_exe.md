---
sigma_id: "60f16a96-db70-42eb-8f76-16763e333590"
title: "New Capture Session Launched Via DXCap.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dxcap_arbitrary_binary_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dxcap_arbitrary_binary_execution.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "60f16a96-db70-42eb-8f76-16763e333590"
  - "New Capture Session Launched Via DXCap.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Capture Session Launched Via DXCap.EXE

Detects the execution of "DXCap.EXE" with the "-c" flag, which allows a user to launch any arbitrary binary or windows package through DXCap itself. This can be abused to potentially bypass application whitelisting.

## Metadata

- Rule ID: 60f16a96-db70-42eb-8f76-16763e333590
- Status: test
- Level: medium
- Author: Beyu Denis, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-10-26
- Modified: 2022-06-09
- Source Path: rules/windows/process_creation/proc_creation_win_dxcap_arbitrary_binary_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \DXCap.exe
- OriginalFileName: DXCap.exe
selection_cli:
  CommandLine|contains: ' -c '
condition: all of selection*
```

## False Positives

- Legitimate execution of dxcap.exe by legitimate user

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Dxcap/
- https://twitter.com/harr0ey/status/992008180904419328

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dxcap_arbitrary_binary_execution.yml)
