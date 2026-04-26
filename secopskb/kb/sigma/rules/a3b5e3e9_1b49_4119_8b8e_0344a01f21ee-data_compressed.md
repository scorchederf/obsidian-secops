---
sigma_id: "a3b5e3e9-1b49-4119-8b8e-0344a01f21ee"
title: "Data Compressed"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_data_compressed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_data_compressed.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "a3b5e3e9-1b49-4119-8b8e-0344a01f21ee"
  - "Data Compressed"
attack_technique_ids:
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Data Compressed

An adversary may compress data (e.g., sensitive documents) that is collected prior to exfiltration in order to make it portable and minimize the amount of data sent over the network.

## Metadata

- Rule ID: a3b5e3e9-1b49-4119-8b8e-0344a01f21ee
- Status: test
- Level: low
- Author: Timur Zinniatullin, oscd.community
- Date: 2019-10-21
- Modified: 2023-07-28
- Source Path: rules/linux/auditd/execve/lnx_auditd_data_compressed.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Detection

```yaml
selection1:
  type: execve
  a0: zip
selection2:
  type: execve
  a0: gzip
  a1: -k
selection3:
  type: execve
  a0: tar
  a1|contains: -c
condition: 1 of selection*
```

## False Positives

- Legitimate use of archiving tools by legitimate user.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/a78b9ed805ab9ea2e422e1aa7741e9407d82d7b1/atomics/T1560.001/T1560.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_data_compressed.yml)
