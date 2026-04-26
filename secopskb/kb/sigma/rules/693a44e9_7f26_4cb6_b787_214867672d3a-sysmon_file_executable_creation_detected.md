---
sigma_id: "693a44e9-7f26-4cb6-b787-214867672d3a"
title: "Sysmon File Executable Creation Detected"
framework: "sigma"
generated: "true"
source_path: "rules/windows/sysmon/sysmon_file_executable_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_file_executable_detected.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / sysmon"
aliases:
  - "693a44e9-7f26-4cb6-b787-214867672d3a"
  - "Sysmon File Executable Creation Detected"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Sysmon File Executable Creation Detected

Triggers on any Sysmon "FileExecutableDetected" event, which triggers every time a PE that is monitored by the config is created.

## Metadata

- Rule ID: 693a44e9-7f26-4cb6-b787-214867672d3a
- Status: test
- Level: medium
- Author: frack113
- Date: 2023-07-20
- Source Path: rules/windows/sysmon/sysmon_file_executable_detected.yml

## Logsource

- product: windows
- service: sysmon

## Detection

```yaml
selection:
  EventID: 29
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
- https://medium.com/@olafhartong/sysmon-15-0-file-executable-detected-40fd64349f36

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/sysmon/sysmon_file_executable_detected.yml)
