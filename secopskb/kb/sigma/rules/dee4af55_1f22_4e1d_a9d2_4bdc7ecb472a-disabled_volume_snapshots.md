---
sigma_id: "dee4af55-1f22-4e1d-a9d2-4bdc7ecb472a"
title: "Disabled Volume Snapshots"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_volsnap_disable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_volsnap_disable.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "dee4af55-1f22-4e1d-a9d2-4bdc7ecb472a"
  - "Disabled Volume Snapshots"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disabled Volume Snapshots

Detects commands that temporarily turn off Volume Snapshots

## Metadata

- Rule ID: dee4af55-1f22-4e1d-a9d2-4bdc7ecb472a
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-01-28
- Modified: 2023-12-15
- Source Path: rules/windows/process_creation/proc_creation_win_reg_volsnap_disable.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \Services\VSS\Diag
  - /d Disabled
condition: selection
```

## False Positives

- Legitimate administration

## References

- https://twitter.com/0gtweet/status/1354766164166115331

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_volsnap_disable.yml)
