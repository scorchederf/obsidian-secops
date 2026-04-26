---
sigma_id: "3e102cd9-a70d-4a7a-9508-403963092f31"
title: "Linux Network Service Scanning Tools Execution"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_network_utilities_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_network_utilities_execution.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "3e102cd9-a70d-4a7a-9508-403963092f31"
  - "Linux Network Service Scanning Tools Execution"
attack_technique_ids:
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Linux Network Service Scanning Tools Execution

Detects execution of network scanning and reconnaisance tools. These tools can be used for the enumeration of local or remote network services for example.

## Metadata

- Rule ID: 3e102cd9-a70d-4a7a-9508-403963092f31
- Status: test
- Level: low
- Author: Alejandro Ortuno, oscd.community, Georg Lauenstein (sure[secure])
- Date: 2020-10-21
- Modified: 2024-09-19
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_network_utilities_execution.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Detection

```yaml
selection_netcat:
  Image|endswith:
  - /nc
  - /ncat
  - /netcat
  - /socat
selection_network_scanning_tools:
  Image|endswith:
  - /autorecon
  - /hping
  - /hping2
  - /hping3
  - /naabu
  - /nmap
  - /nping
  - /telnet
  - /zenmap
filter_main_netcat_listen_flag:
  CommandLine|contains:
  - ' --listen '
  - ' -l '
condition: (selection_netcat and not filter_main_netcat_listen_flag) or selection_network_scanning_tools
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1046/T1046.md
- https://github.com/projectdiscovery/naabu
- https://github.com/Tib3rius/AutoRecon

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_network_utilities_execution.yml)
