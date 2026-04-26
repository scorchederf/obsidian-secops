---
sigma_id: "700fb7e8-2981-401c-8430-be58e189e741"
title: "Suspicious Package Installed - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_install_suspicious_packages.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_install_suspicious_packages.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "700fb7e8-2981-401c-8430-be58e189e741"
  - "Suspicious Package Installed - Linux"
attack_technique_ids:
  - "T1553.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Package Installed - Linux

Detects installation of suspicious packages using system installation utilities

## Metadata

- Rule ID: 700fb7e8-2981-401c-8430-be58e189e741
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-03
- Modified: 2026-01-01
- Source Path: rules/linux/process_creation/proc_creation_lnx_install_suspicious_packages.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Detection

```yaml
selection_tool_apt:
  Image|endswith:
  - /apt
  - /apt-get
  CommandLine|contains: install
selection_tool_yum:
  Image|endswith: /yum
  CommandLine|contains:
  - localinstall
  - install
selection_tool_rpm:
  Image|endswith: /rpm
  CommandLine|contains: -i
selection_tool_dpkg:
  Image|endswith: /dpkg
  CommandLine|contains:
  - --install
  - -i
selection_keyword:
  CommandLine|contains:
  - nmap
  - ' nc'
  - netcat
  - wireshark
  - tshark
  - openconnect
  - proxychains
  - socat
condition: 1 of selection_tool_* and selection_keyword
```

## False Positives

- Legitimate administration activities

## References

- https://gist.githubusercontent.com/MichaelKoczwara/12faba9c061c12b5814b711166de8c2f/raw/e2068486692897b620c25fde1ea258c8218fe3d3/history.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_install_suspicious_packages.yml)
