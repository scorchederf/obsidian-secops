---
atomic_guid: "361fe49d-0c19-46ec-a483-ccb92d38e88e"
title: "Identifying Network Shares - Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1083"
attack_technique_name: "File and Directory Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "361fe49d-0c19-46ec-a483-ccb92d38e88e"
  - "Identifying Network Shares - Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Identifying Network Shares - Linux

If the system uses network file systems (e.g., NFS, CIFS), findmnt can help locate paths to remote shares.
Attackers may then attempt to access these shares for lateral movement or data exfiltration.

## Metadata

- Atomic GUID: 361fe49d-0c19-46ec-a483-ccb92d38e88e
- Technique: T1083: File and Directory Discovery
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1083/T1083.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Executor

- name: sh

### Command

```bash
findmnt -t nfs
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml)
