---
sigma_id: "b6457d63-d2a2-4e29-859d-4e7affc153d1"
title: "Potential Discovery Activity Via Dnscmd.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dnscmd_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dnscmd_discovery.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b6457d63-d2a2-4e29-859d-4e7affc153d1"
  - "Potential Discovery Activity Via Dnscmd.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Discovery Activity Via Dnscmd.EXE

Detects an attempt to leverage dnscmd.exe to enumerate the DNS zones of a domain. DNS zones used to host the DNS records for a particular domain.

## Metadata

- Rule ID: b6457d63-d2a2-4e29-859d-4e7affc153d1
- Status: test
- Level: medium
- Author: @gott_cyber
- Date: 2022-07-31
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_dnscmd_discovery.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
  Image|endswith: \dnscmd.exe
selection_cli:
  CommandLine|contains:
  - /enumrecords
  - /enumzones
  - /ZonePrint
  - /info
condition: all of selection_*
```

## False Positives

- Legitimate administration use

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/dnscmd
- https://learn.microsoft.com/en-us/azure/dns/dns-zones-records
- https://lolbas-project.github.io/lolbas/Binaries/Dnscmd/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dnscmd_discovery.yml)
