---
sigma_id: "c21c4eaa-ba2e-419a-92b2-8371703cbe21"
title: "Setuid and Setgid"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_setgid_setuid.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_setgid_setuid.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "c21c4eaa-ba2e-419a-92b2-8371703cbe21"
  - "Setuid and Setgid"
attack_technique_ids:
  - "T1548.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Setuid and Setgid

Detects suspicious change of file privileges with chown and chmod commands

## Metadata

- Rule ID: c21c4eaa-ba2e-419a-92b2-8371703cbe21
- Status: test
- Level: low
- Author: Ömer Günal
- Date: 2020-06-16
- Modified: 2022-10-05
- Source Path: rules/linux/process_creation/proc_creation_lnx_setgid_setuid.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.001]]

## Detection

```yaml
selection_root:
  CommandLine|contains: chown root
selection_perm:
  CommandLine|contains:
  - ' chmod u+s'
  - ' chmod g+s'
condition: all of selection_*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1548.001/T1548.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_setgid_setuid.yml)
