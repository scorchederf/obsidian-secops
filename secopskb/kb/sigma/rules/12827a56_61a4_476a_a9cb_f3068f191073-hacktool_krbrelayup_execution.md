---
sigma_id: "12827a56-61a4-476a-a9cb-f3068f191073"
title: "HackTool - KrbRelayUp Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_krbrelayup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_krbrelayup.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "12827a56-61a4-476a-a9cb-f3068f191073"
  - "HackTool - KrbRelayUp Execution"
attack_technique_ids:
  - "T1558.003"
  - "T1550.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - KrbRelayUp Execution

Detects KrbRelayUp used to perform a universal no-fix local privilege escalation in Windows domain environments where LDAP signing is not enforced

## Metadata

- Rule ID: 12827a56-61a4-476a-a9cb-f3068f191073
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-04-26
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_krbrelayup.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]
- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \KrbRelayUp.exe
- OriginalFileName: KrbRelayUp.exe
selection_cli_1:
  CommandLine|contains|all:
  - ' relay '
  - ' -Domain '
  - ' -ComputerName '
selection_cli_2:
  CommandLine|contains|all:
  - ' krbscm '
  - ' -sc '
selection_cli_3:
  CommandLine|contains|all:
  - ' spawn '
  - ' -d '
  - ' -cn '
  - ' -cp '
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://github.com/Dec0ne/KrbRelayUp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_krbrelayup.yml)
