---
sigma_id: "8f88e3f6-2a49-48f5-a5c4-2f7eedf78710"
title: "Java Running with Remote Debugging"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_java_remote_debugging.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_remote_debugging.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "8f88e3f6-2a49-48f5-a5c4-2f7eedf78710"
  - "Java Running with Remote Debugging"
attack_technique_ids:
  - "T1203"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Java Running with Remote Debugging

Detects a JAVA process running with remote debugging allowing more than just localhost to connect

## Metadata

- Rule ID: 8f88e3f6-2a49-48f5-a5c4-2f7eedf78710
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2019-01-16
- Modified: 2023-02-01
- Source Path: rules/windows/process_creation/proc_creation_win_java_remote_debugging.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203]]

## Detection

```yaml
selection_jdwp_transport:
  CommandLine|contains: transport=dt_socket,address=
selection_old_jvm_version:
  CommandLine|contains:
  - jre1.
  - jdk1.
exclusion:
  CommandLine|contains:
  - address=127.0.0.1
  - address=localhost
condition: all of selection_* and not exclusion
```

## False Positives

- Unknown

## References

- https://dzone.com/articles/remote-debugging-java-applications-with-jdwp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_remote_debugging.yml)
