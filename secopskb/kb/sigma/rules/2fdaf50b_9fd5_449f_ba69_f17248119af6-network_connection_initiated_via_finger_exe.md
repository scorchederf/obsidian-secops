---
sigma_id: "2fdaf50b-9fd5-449f-ba69-f17248119af6"
title: "Network Connection Initiated via Finger.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_finger.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_finger.yml"
build_date: "2026-04-27 19:13:53"
status: "experimental"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "2fdaf50b-9fd5-449f-ba69-f17248119af6"
  - "Network Connection Initiated via Finger.EXE"
attack_technique_ids:
  - "T1071.004"
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects network connections via finger.exe, which can be abused by threat actors to retrieve remote commands for execution on Windows devices.
In one ClickFix malware campaign, adversaries leveraged the finger protocol to fetch commands from a remote server.
Since the finger utility is not commonly used in modern Windows environments, its presence already raises suspicion.
Investigating such network connections can also help identify potential malicious infrastructure used by threat actors

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]

## Detection

```yaml
selection:
  Initiated: 'true'
  Image|endswith: \finger.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.bleepingcomputer.com/news/security/decades-old-finger-protocol-abused-in-clickfix-malware-attacks/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_finger.yml)
