---
sigma_id: "98c5aeef-32d5-492f-b174-64a691896d25"
title: "Service Security Descriptor Tampering Via Sc.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_sdset_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_sdset_modification.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "98c5aeef-32d5-492f-b174-64a691896d25"
  - "Service Security Descriptor Tampering Via Sc.EXE"
attack_technique_ids:
  - "T1574.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service Security Descriptor Tampering Via Sc.EXE

Detection of sc.exe utility adding a new service with special permission which hides that service.

## Metadata

- Rule ID: 98c5aeef-32d5-492f-b174-64a691896d25
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-28
- Source Path: rules/windows/process_creation/proc_creation_win_sc_sdset_modification.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Detection

```yaml
selection_img:
- Image|endswith: \sc.exe
- OriginalFileName: sc.exe
selection_cli:
  CommandLine|contains: sdset
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blog.talosintelligence.com/2021/10/threat-hunting-in-large-datasets-by.html
- https://www.sans.org/blog/red-team-tactics-hiding-windows-services/
- https://twitter.com/Alh4zr3d/status/1580925761996828672
- https://twitter.com/0gtweet/status/1628720819537936386
- https://itconnect.uw.edu/tools-services-support/it-systems-infrastructure/msinf/other-help/understanding-sddl-syntax/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_sdset_modification.yml)
