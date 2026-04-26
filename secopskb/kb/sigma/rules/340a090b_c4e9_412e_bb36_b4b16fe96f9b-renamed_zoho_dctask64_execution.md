---
sigma_id: "340a090b-c4e9-412e-bb36-b4b16fe96f9b"
title: "Renamed ZOHO Dctask64 Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_dctask64.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_dctask64.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "340a090b-c4e9-412e-bb36-b4b16fe96f9b"
  - "Renamed ZOHO Dctask64 Execution"
attack_technique_ids:
  - "T1036"
  - "T1055.001"
  - "T1202"
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Renamed ZOHO Dctask64 Execution

Detects a renamed "dctask64.exe" execution, a signed binary by ZOHO Corporation part of ManageEngine Endpoint Central.
This binary can be abused for DLL injection, arbitrary command and process execution.

## Metadata

- Rule ID: 340a090b-c4e9-412e-bb36-b4b16fe96f9b
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-01-28
- Modified: 2025-01-22
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_dctask64.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]
- [[kb/attack/techniques/T1055-process_injection|T1055.001]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Hashes|contains:
  - IMPHASH=6834B1B94E49701D77CCB3C0895E1AFD
  - IMPHASH=1BB6F93B129F398C7C4A76BB97450BBA
  - IMPHASH=FAA2AC19875FADE461C8D89DCF2710A3
  - IMPHASH=F1039CED4B91572AB7847D26032E6BBF
filter_main_legit_name:
  Image|endswith: \dctask64.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/gN3mes1s/status/1222088214581825540
- https://twitter.com/gN3mes1s/status/1222095963789111296
- https://twitter.com/gN3mes1s/status/1222095371175911424

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_dctask64.yml)
