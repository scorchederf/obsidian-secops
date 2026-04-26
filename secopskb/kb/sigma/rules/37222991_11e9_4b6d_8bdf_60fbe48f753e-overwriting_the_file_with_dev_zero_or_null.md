---
sigma_id: "37222991-11e9-4b6d-8bdf-60fbe48f753e"
title: "Overwriting the File with Dev Zero or Null"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_dd_delete_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_dd_delete_file.yml"
build_date: "2026-04-26 14:14:30"
status: "stable"
level: "low"
logsource: "linux / auditd"
aliases:
  - "37222991-11e9-4b6d-8bdf-60fbe48f753e"
  - "Overwriting the File with Dev Zero or Null"
attack_technique_ids:
  - "T1485"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Overwriting the File with Dev Zero or Null

Detects overwriting (effectively wiping/deleting) of a file.

## Metadata

- Rule ID: 37222991-11e9-4b6d-8bdf-60fbe48f753e
- Status: stable
- Level: low
- Author: Jakob Weinzettl, oscd.community
- Date: 2019-10-23
- Source Path: rules/linux/auditd/execve/lnx_auditd_dd_delete_file.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1485-data_destruction|T1485]]

## Detection

```yaml
selection:
  type: EXECVE
  a0|contains: dd
  a1|contains:
  - if=/dev/null
  - if=/dev/zero
condition: selection
```

## False Positives

- Appending null bytes to files.
- Legitimate overwrite of files.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1485/T1485.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_dd_delete_file.yml)
