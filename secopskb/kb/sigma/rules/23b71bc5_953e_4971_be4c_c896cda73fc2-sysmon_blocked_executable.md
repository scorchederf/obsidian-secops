---
sigma_id: "23b71bc5-953e-4971-be4c-c896cda73fc2"
title: "Sysmon Blocked Executable"
framework: "sigma"
generated: "true"
source_path: "rules/windows/sysmon/sysmon_file_block_executable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_file_block_executable.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / sysmon"
aliases:
  - "23b71bc5-953e-4971-be4c-c896cda73fc2"
  - "Sysmon Blocked Executable"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Sysmon Blocked Executable

Triggers on any Sysmon "FileBlockExecutable" event, which indicates a violation of the configured block policy

## Metadata

- Rule ID: 23b71bc5-953e-4971-be4c-c896cda73fc2
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-16
- Modified: 2023-09-16
- Source Path: rules/windows/sysmon/sysmon_file_block_executable.yml

## Logsource

- product: windows
- service: sysmon

## Detection

```yaml
selection:
  EventID: 27
condition: selection
```

## False Positives

- Unlikely

## References

- https://medium.com/@olafhartong/sysmon-14-0-fileblockexecutable-13d7ba3dff3e

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_file_block_executable.yml)
