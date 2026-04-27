---
sigma_id: "79ce34ca-af29-4d0e-b832-fc1b377020db"
title: "Whoami.EXE Execution From Privileged Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_whoami_execution_from_high_priv_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_execution_from_high_priv_process.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "79ce34ca-af29-4d0e-b832-fc1b377020db"
  - "Whoami.EXE Execution From Privileged Process"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of "whoami.exe" by privileged accounts that are often abused by threat actors

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]

## Detection

```yaml
selection_img:
- OriginalFileName: whoami.exe
- Image|endswith: \whoami.exe
selection_user:
  User|contains:
  - AUTHORI
  - AUTORI
  - TrustedInstaller
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-privilege-escalation-in-windows-environment
- https://web.archive.org/web/20221019044836/https://nsudo.m2team.org/en-us/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_execution_from_high_priv_process.yml)
