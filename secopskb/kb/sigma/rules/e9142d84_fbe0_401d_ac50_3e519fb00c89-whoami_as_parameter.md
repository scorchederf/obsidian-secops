---
sigma_id: "e9142d84-fbe0-401d-ac50-3e519fb00c89"
title: "WhoAmI as Parameter"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_whoami_as_param.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_whoami_as_param.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e9142d84-fbe0-401d-ac50-3e519fb00c89"
  - "WhoAmI as Parameter"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious process command line that uses whoami as first parameter (as e.g. used by EfsPotato)

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]

## Detection

```yaml
selection:
  CommandLine|contains: .exe whoami
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/blackarrowsec/status/1463805700602224645?s=12

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_whoami_as_param.yml)
