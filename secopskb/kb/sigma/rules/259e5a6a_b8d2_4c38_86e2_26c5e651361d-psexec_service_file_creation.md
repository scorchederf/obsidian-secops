---
sigma_id: "259e5a6a-b8d2-4c38-86e2-26c5e651361d"
title: "PsExec Service File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_sysinternals_psexec_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_psexec_service.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "windows / file_event"
aliases:
  - "259e5a6a-b8d2-4c38-86e2-26c5e651361d"
  - "PsExec Service File Creation"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PsExec Service File Creation

Detects default PsExec service filename which indicates PsExec service installation and execution

## Metadata

- Rule ID: 259e5a6a-b8d2-4c38-86e2-26c5e651361d
- Status: test
- Level: low
- Author: Thomas Patzke
- Date: 2017-06-12
- Modified: 2022-10-26
- Source Path: rules/windows/file/file_event/file_event_win_sysinternals_psexec_service.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

### Software Tags

- S0029

## Detection

```yaml
selection:
  TargetFilename|endswith: \PSEXESVC.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.jpcert.or.jp/english/pub/sr/ir_research.html
- https://jpcertcc.github.io/ToolAnalysisResultSheet

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_psexec_service.yml)
