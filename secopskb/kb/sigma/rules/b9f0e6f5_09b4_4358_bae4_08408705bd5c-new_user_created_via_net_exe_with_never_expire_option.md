---
sigma_id: "b9f0e6f5-09b4-4358-bae4-08408705bd5c"
title: "New User Created Via Net.EXE With Never Expire Option"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_user_add_never_expire.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_user_add_never_expire.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b9f0e6f5-09b4-4358-bae4-08408705bd5c"
  - "New User Created Via Net.EXE With Never Expire Option"
attack_technique_ids:
  - "T1136.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New User Created Via Net.EXE With Never Expire Option

Detects creation of local users via the net.exe command with the option "never expire"

## Metadata

- Rule ID: b9f0e6f5-09b4-4358-bae4-08408705bd5c
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-12
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_net_user_add_never_expire.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \net.exe
  - \net1.exe
- OriginalFileName:
  - net.exe
  - net1.exe
selection_cli:
  CommandLine|contains|all:
  - user
  - add
  - expires:never
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_user_add_never_expire.yml)
