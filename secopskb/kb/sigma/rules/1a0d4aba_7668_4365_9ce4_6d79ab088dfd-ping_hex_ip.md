---
sigma_id: "1a0d4aba-7668-4365-9ce4-6d79ab088dfd"
title: "Ping Hex IP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ping_hex_ip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ping_hex_ip.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1a0d4aba-7668-4365-9ce4-6d79ab088dfd"
  - "Ping Hex IP"
attack_technique_ids:
  - "T1140"
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Ping Hex IP

Detects a ping command that uses a hex encoded IP address

## Metadata

- Rule ID: 1a0d4aba-7668-4365-9ce4-6d79ab088dfd
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2018-03-23
- Modified: 2025-10-17
- Source Path: rules/windows/process_creation/proc_creation_win_ping_hex_ip.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Detection

```yaml
selection:
  Image|endswith: \ping.exe
  CommandLine|re: 0x[a-fA-F0-9]{8}
condition: selection
```

## False Positives

- Unlikely, because no sane admin pings IP addresses in a hexadecimal form

## References

- https://github.com/vysecurity/Aggressor-VYSEC/blob/0d61c80387b9432dab64b8b8a9fb52d20cfef80e/ping.cna
- https://twitter.com/vysecurity/status/977198418354491392

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ping_hex_ip.yml)
