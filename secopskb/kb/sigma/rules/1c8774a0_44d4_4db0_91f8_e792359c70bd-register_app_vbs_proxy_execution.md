---
sigma_id: "1c8774a0-44d4-4db0-91f8-e792359c70bd"
title: "REGISTER_APP.VBS Proxy Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_register_app.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_register_app.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1c8774a0-44d4-4db0-91f8-e792359c70bd"
  - "REGISTER_APP.VBS Proxy Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# REGISTER_APP.VBS Proxy Execution

Detects the use of a Microsoft signed script 'REGISTER_APP.VBS' to register a VSS/VDS Provider as a COM+ application.

## Metadata

- Rule ID: 1c8774a0-44d4-4db0-91f8-e792359c70bd
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-19
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_register_app.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \register_app.vbs
  - -register
condition: selection
```

## False Positives

- Legitimate usage of the script. Always investigate what's being registered to confirm if it's benign

## References

- https://twitter.com/sblmsrsn/status/1456613494783160325?s=20

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_register_app.yml)
