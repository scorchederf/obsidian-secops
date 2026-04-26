---
sigma_id: "71d65515-c436-43c0-841b-236b1f32c21e"
title: "Cisco File Deletion"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_file_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_file_deletion.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "cisco / aaa"
aliases:
  - "71d65515-c436-43c0-841b-236b1f32c21e"
  - "Cisco File Deletion"
attack_technique_ids:
  - "T1070.004"
  - "T1561.001"
  - "T1561.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cisco File Deletion

See what files are being deleted from flash file systems

## Metadata

- Rule ID: 71d65515-c436-43c0-841b-236b1f32c21e
- Status: test
- Level: medium
- Author: Austin Clark
- Date: 2019-08-12
- Modified: 2023-01-04
- Source Path: rules/network/cisco/aaa/cisco_cli_file_deletion.yml

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]
- [[kb/attack/techniques/T1561-disk_wipe|T1561.001]]
- [[kb/attack/techniques/T1561-disk_wipe|T1561.002]]

## Detection

```yaml
keywords:
- erase
- delete
- format
condition: keywords
```

## False Positives

- Will be used sometimes by admins to clean up local flash space

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_file_deletion.yml)
