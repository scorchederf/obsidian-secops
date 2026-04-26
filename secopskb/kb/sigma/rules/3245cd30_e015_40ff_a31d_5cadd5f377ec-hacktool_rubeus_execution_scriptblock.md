---
sigma_id: "3245cd30-e015-40ff-a31d-5cadd5f377ec"
title: "HackTool - Rubeus Execution - ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_hktl_rubeus.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_hktl_rubeus.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "3245cd30-e015-40ff-a31d-5cadd5f377ec"
  - "HackTool - Rubeus Execution - ScriptBlock"
attack_technique_ids:
  - "T1003"
  - "T1558.003"
  - "T1550.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Rubeus Execution - ScriptBlock

Detects the execution of the hacktool Rubeus using specific command line flags

## Metadata

- Rule ID: 3245cd30-e015-40ff-a31d-5cadd5f377ec
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems), Florian Roth (Nextron Systems)
- Date: 2023-04-27
- Source Path: rules/windows/powershell/powershell_script/posh_ps_hktl_rubeus.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]
- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]
- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.003]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_hktl_rubeus.yml)
