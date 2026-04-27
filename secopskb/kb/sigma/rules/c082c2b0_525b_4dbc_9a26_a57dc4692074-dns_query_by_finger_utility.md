---
sigma_id: "c082c2b0-525b-4dbc-9a26-a57dc4692074"
title: "DNS Query by Finger Utility"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_finger.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_finger.yml"
build_date: "2026-04-27 19:13:51"
status: "experimental"
level: "high"
logsource: "windows / dns_query"
aliases:
  - "c082c2b0-525b-4dbc-9a26-a57dc4692074"
  - "DNS Query by Finger Utility"
attack_technique_ids:
  - "T1071.004"
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects DNS queries made by the finger utility, which can be abused by threat actors to retrieve remote commands for execution on Windows devices.
In one ClickFix malware campaign, adversaries leveraged the finger protocol to fetch commands from a remote server.
Since the finger utility is not commonly used in modern Windows environments, its presence already raises suspicion.
Investigating such DNS queries can also help identify potential malicious infrastructure used by threat actors for command and control (C2) communication.

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]

## Detection

```yaml
selection:
  Image|endswith: \finger.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.bleepingcomputer.com/news/security/decades-old-finger-protocol-abused-in-clickfix-malware-attacks/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_finger.yml)
