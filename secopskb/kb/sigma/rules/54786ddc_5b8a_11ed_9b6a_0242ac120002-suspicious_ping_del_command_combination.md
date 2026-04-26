---
sigma_id: "54786ddc-5b8a-11ed-9b6a-0242ac120002"
title: "Suspicious Ping/Del Command Combination"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_ping_del_combined_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_ping_del_combined_execution.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "54786ddc-5b8a-11ed-9b6a-0242ac120002"
  - "Suspicious Ping/Del Command Combination"
attack_technique_ids:
  - "T1070.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Ping/Del Command Combination

Detects a method often used by ransomware. Which combines the "ping" to wait a couple of seconds and then "del" to delete the file in question. Its used to hide the file responsible for the initial infection for example

## Metadata

- Rule ID: 54786ddc-5b8a-11ed-9b6a-0242ac120002
- Status: test
- Level: high
- Author: Ilya Krestinichev
- Date: 2022-11-03
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_ping_del_combined_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Detection

```yaml
selection_count:
  CommandLine|contains|windash: ' -n '
selection_nul:
  CommandLine|contains: Nul
selection_del_param:
  CommandLine|contains|windash:
  - ' -f '
  - ' -q '
selection_all:
  CommandLine|contains|all:
  - ping
  - 'del '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blog.sygnia.co/kaseya-ransomware-supply-chain-attack
- https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2022/06/23093553/Common-TTPs-of-the-modern-ransomware_low-res.pdf
- https://www.acronis.com/en-us/blog/posts/lockbit-ransomware/
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/blackbyte-exbyte-ransomware

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_ping_del_combined_execution.yml)
