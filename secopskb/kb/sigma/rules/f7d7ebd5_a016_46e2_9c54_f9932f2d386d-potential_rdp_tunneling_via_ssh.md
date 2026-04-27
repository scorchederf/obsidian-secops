---
sigma_id: "f7d7ebd5-a016-46e2-9c54-f9932f2d386d"
title: "Potential RDP Tunneling Via SSH"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ssh_rdp_tunneling.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ssh_rdp_tunneling.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f7d7ebd5-a016-46e2-9c54-f9932f2d386d"
  - "Potential RDP Tunneling Via SSH"
attack_technique_ids:
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Execution of ssh.exe to perform data exfiltration and tunneling through RDP

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572: Protocol Tunneling]]

## Detection

```yaml
selection:
  Image|endswith: \ssh.exe
  CommandLine|contains: :3389
condition: selection
```

## False Positives

- Unknown

## References

- https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ssh_rdp_tunneling.yml)
