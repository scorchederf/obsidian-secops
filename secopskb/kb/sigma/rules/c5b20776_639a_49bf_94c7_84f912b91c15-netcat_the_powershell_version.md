---
sigma_id: "c5b20776-639a-49bf-94c7-84f912b91c15"
title: "Netcat The Powershell Version"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_powercat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_powercat.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / ps_classic_start"
aliases:
  - "c5b20776-639a-49bf-94c7-84f912b91c15"
  - "Netcat The Powershell Version"
attack_technique_ids:
  - "T1095"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Netcat The Powershell Version

Adversaries may use a non-application layer protocol for communication between host and C2 server or among infected hosts within a network

## Metadata

- Rule ID: c5b20776-639a-49bf-94c7-84f912b91c15
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-21
- Modified: 2023-10-27
- Source Path: rules/windows/powershell/powershell_classic/posh_pc_powercat.yml

## Logsource

- category: ps_classic_start
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1095-non-application_layer_protocol|T1095]]

## Detection

```yaml
selection:
  Data|contains:
  - 'powercat '
  - powercat.ps1
condition: selection
```

## False Positives

- Unknown

## References

- https://nmap.org/ncat/
- https://github.com/besimorhino/powercat
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1095/T1095.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_powercat.yml)
