---
sigma_id: "f38ce0b9-5e97-4b47-a211-7dc8d8b871da"
title: "Potential RDP Tunneling Via Plink"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_plink_susp_tunneling.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_plink_susp_tunneling.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f38ce0b9-5e97-4b47-a211-7dc8d8b871da"
  - "Potential RDP Tunneling Via Plink"
attack_technique_ids:
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Execution of plink to perform data exfiltration and tunneling

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572: Protocol Tunneling]]

## Detection

```yaml
selection_a:
  Image|endswith: \plink.exe
  CommandLine|contains: :127.0.0.1:3389
selection_b1:
  Image|endswith: \plink.exe
  CommandLine|contains: :3389
selection_b2:
  CommandLine|contains:
  - ' -P 443'
  - ' -P 22'
condition: selection_a or all of selection_b*
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2022/07/26/malicious-iis-extensions-quietly-open-persistent-backdoors-into-servers/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_plink_susp_tunneling.yml)
