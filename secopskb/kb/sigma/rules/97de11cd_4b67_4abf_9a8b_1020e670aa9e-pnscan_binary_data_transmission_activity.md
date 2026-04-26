---
sigma_id: "97de11cd-4b67-4abf-9a8b-1020e670aa9e"
title: "Pnscan Binary Data Transmission Activity"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_pnscan_binary_cli_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_pnscan_binary_cli_pattern.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "97de11cd-4b67-4abf-9a8b-1020e670aa9e"
  - "Pnscan Binary Data Transmission Activity"
attack_technique_ids:
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Pnscan Binary Data Transmission Activity

Detects command line patterns associated with the use of Pnscan for sending and receiving binary data across the network.
This behavior has been identified in a Linux malware campaign targeting Docker, Apache Hadoop, Redis, and Confluence and was previously used by the threat actor known as TeamTNT

## Metadata

- Rule ID: 97de11cd-4b67-4abf-9a8b-1020e670aa9e
- Status: test
- Level: medium
- Author: David Burkett (@signalblur)
- Date: 2024-04-16
- Source Path: rules/linux/process_creation/proc_creation_lnx_pnscan_binary_cli_pattern.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Detection

```yaml
selection:
  CommandLine|re: -(W|R)\s?(\s|"|')([0-9a-fA-F]{2}\s?){2,20}(\s|"|')
condition: selection
```

## False Positives

- Unknown

## References

- https://www.cadosecurity.com/blog/spinning-yarn-a-new-linux-malware-campaign-targets-docker-apache-hadoop-redis-and-confluence
- https://intezer.com/wp-content/uploads/2021/09/TeamTNT-Cryptomining-Explosion.pdf
- https://regex101.com/r/RugQYK/1
- https://www.virustotal.com/gui/file/beddf70a7bab805f0c0b69ac0989db6755949f9f68525c08cb874988353f78a9/content

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_pnscan_binary_cli_pattern.yml)
