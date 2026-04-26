---
sigma_id: "6419afd1-3742-47a5-a7e6-b50386cd15f8"
title: "Chmod Suspicious Directory"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_chmod_directories.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_chmod_directories.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "6419afd1-3742-47a5-a7e6-b50386cd15f8"
  - "Chmod Suspicious Directory"
attack_technique_ids:
  - "T1222.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Chmod Suspicious Directory

Detects chmod targeting files in abnormal directory paths.

## Metadata

- Rule ID: 6419afd1-3742-47a5-a7e6-b50386cd15f8
- Status: test
- Level: medium
- Author: Christopher Peacock @SecurePeacock, SCYTHE @scythe_io
- Date: 2022-06-03
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_chmod_directories.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.002]]

## Detection

```yaml
selection:
  Image|endswith: /chmod
  CommandLine|contains:
  - /tmp/
  - /.Library/
  - /etc/
  - /opt/
condition: selection
```

## False Positives

- Admin changing file permissions.

## References

- https://www.intezer.com/blog/malware-analysis/new-backdoor-sysjoker/
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1222.002/T1222.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_chmod_directories.yml)
