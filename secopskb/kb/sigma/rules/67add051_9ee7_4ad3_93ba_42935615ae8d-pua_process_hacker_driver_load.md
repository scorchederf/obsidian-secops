---
sigma_id: "67add051-9ee7-4ad3-93ba-42935615ae8d"
title: "PUA - Process Hacker Driver Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/driver_load/driver_load_win_pua_process_hacker.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_pua_process_hacker.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "windows / driver_load"
aliases:
  - "67add051-9ee7-4ad3-93ba-42935615ae8d"
  - "PUA - Process Hacker Driver Load"
attack_technique_ids:
  - "T1543"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Process Hacker Driver Load

Detects driver load of the Process Hacker tool

## Metadata

- Rule ID: 67add051-9ee7-4ad3-93ba-42935615ae8d
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-11-16
- Modified: 2024-11-23
- Source Path: rules/windows/driver_load/driver_load_win_pua_process_hacker.yml

## Logsource

- category: driver_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543]]

## Detection

```yaml
selection:
- ImageLoaded|endswith: \kprocesshacker.sys
- Hashes|contains:
  - IMPHASH=821D74031D3F625BCBD0DF08B70F1E77
  - IMPHASH=F86759BB4DE4320918615DC06E998A39
  - IMPHASH=0A64EEB85419257D0CE32BD5D55C3A18
  - IMPHASH=6E7B34DFC017700B1517B230DF6FF0D0
condition: selection
```

## False Positives

- Legitimate use of process hacker or system informer by developers or system administrators

## References

- https://processhacker.sourceforge.io/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_pua_process_hacker.yml)
