---
sigma_id: "340a090b-c4e9-412e-bb36-b4b16fe96f9b"
title: "Renamed ZOHO Dctask64 Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_dctask64.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_dctask64.yml"
build_date: "2026-04-27 19:13:55"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a renamed "dctask64.exe" execution, a signed binary by ZOHO Corporation part of ManageEngine Endpoint Central.
This binary can be abused for DLL injection, arbitrary command and process execution.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036: Masquerading]]
- [[kb/attack/techniques/T1055-process_injection#^t1055001-dynamic-link-library-injection|T1055.001: Dynamic-link Library Injection]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

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
