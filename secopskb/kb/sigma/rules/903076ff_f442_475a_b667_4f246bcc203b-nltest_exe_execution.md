---
sigma_id: "903076ff-f442-475a-b667-4f246bcc203b"
title: "Nltest.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_nltest_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_nltest_execution.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "903076ff-f442-475a-b667-4f246bcc203b"
  - "Nltest.EXE Execution"
attack_technique_ids:
  - "T1016"
  - "T1018"
  - "T1482"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Nltest.EXE Execution

Detects nltest commands that can be used for information discovery

## Metadata

- Rule ID: 903076ff-f442-475a-b667-4f246bcc203b
- Status: test
- Level: low
- Author: Arun Chauhan
- Date: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_nltest_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]
- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]
- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Detection

```yaml
selection:
- Image|endswith: \nltest.exe
- OriginalFileName: nltestrk.exe
condition: selection
```

## False Positives

- Legitimate administration activity

## References

- https://jpcertcc.github.io/ToolAnalysisResultSheet/details/nltest.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_nltest_execution.yml)
