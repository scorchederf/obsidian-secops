---
sigma_id: "a0459f02-ac51-4c09-b511-b8c9203fc429"
title: "Potential Process Execution Proxy Via CL_Invocation.ps1"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_cl_invocation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cl_invocation.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a0459f02-ac51-4c09-b511-b8c9203fc429"
  - "Potential Process Execution Proxy Via CL_Invocation.ps1"
attack_technique_ids:
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Process Execution Proxy Via CL_Invocation.ps1

Detects calls to "SyncInvoke" that is part of the "CL_Invocation.ps1" script to proxy execution using "System.Diagnostics.Process"

## Metadata

- Rule ID: a0459f02-ac51-4c09-b511-b8c9203fc429
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), oscd.community, Natalia Shornikova
- Date: 2020-10-14
- Modified: 2023-08-17
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_cl_invocation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detection

```yaml
selection:
  CommandLine|contains: 'SyncInvoke '
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Scripts/Cl_invocation/
- https://twitter.com/bohops/status/948061991012327424

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cl_invocation.yml)
