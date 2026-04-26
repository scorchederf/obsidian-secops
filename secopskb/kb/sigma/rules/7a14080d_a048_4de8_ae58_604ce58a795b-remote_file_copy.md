---
sigma_id: "7a14080d-a048-4de8-ae58-604ce58a795b"
title: "Remote File Copy"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_file_copy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_file_copy.yml"
build_date: "2026-04-26 14:14:34"
status: "stable"
level: "low"
logsource: "linux"
aliases:
  - "7a14080d-a048-4de8-ae58-604ce58a795b"
  - "Remote File Copy"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote File Copy

Detects the use of tools that copy files from or to remote systems

## Metadata

- Rule ID: 7a14080d-a048-4de8-ae58-604ce58a795b
- Status: stable
- Level: low
- Author: Ömer Günal
- Date: 2020-06-18
- Source Path: rules/linux/builtin/lnx_file_copy.yml

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
tools:
- 'scp '
- 'rsync '
- 'sftp '
filter:
- '@'
- ':'
condition: tools and filter
```

## False Positives

- Legitimate administration activities

## References

- https://www.cisa.gov/stopransomware/ransomware-guide

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_file_copy.yml)
