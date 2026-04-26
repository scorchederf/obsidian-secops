---
sigma_id: "7ec2c172-dceb-4c10-92c9-87c1881b7e18"
title: "HackTool - Rubeus Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_rubeus.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_rubeus.yml"
build_date: "2026-04-26 15:01:45"
status: "stable"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "7ec2c172-dceb-4c10-92c9-87c1881b7e18"
  - "HackTool - Rubeus Execution"
attack_technique_ids:
  - "T1003"
  - "T1558.003"
  - "T1550.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Rubeus Execution

Detects the execution of the hacktool Rubeus via PE information of command line parameters

## Metadata

- Rule ID: 7ec2c172-dceb-4c10-92c9-87c1881b7e18
- Status: stable
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2018-12-19
- Modified: 2023-04-20
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_rubeus.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]
- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]
- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.003]]

## Detection

```yaml
selection:
- Image|endswith: \Rubeus.exe
- OriginalFileName: Rubeus.exe
- Description: Rubeus
- CommandLine|contains:
  - 'asreproast '
  - 'dump /service:krbtgt '
  - dump /luid:0x
  - 'kerberoast '
  - 'createnetonly /program:'
  - 'ptt /ticket:'
  - '/impersonateuser:'
  - 'renew /ticket:'
  - 'asktgt /user:'
  - 'harvest /interval:'
  - 's4u /user:'
  - 's4u /ticket:'
  - 'hash /password:'
  - 'golden /aes256:'
  - 'silver /user:'
condition: selection
```

## False Positives

- Unlikely

## References

- https://blog.harmj0y.net/redteaming/from-kekeo-to-rubeus
- https://m0chan.github.io/2019/07/31/How-To-Attack-Kerberos-101.html
- https://github.com/GhostPack/Rubeus

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_rubeus.yml)
