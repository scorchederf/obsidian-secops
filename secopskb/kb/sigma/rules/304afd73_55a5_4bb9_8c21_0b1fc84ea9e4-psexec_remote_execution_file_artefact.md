---
sigma_id: "304afd73-55a5-4bb9-8c21-0b1fc84ea9e4"
title: "PSEXEC Remote Execution File Artefact"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_sysinternals_psexec_service_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_psexec_service_key.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "304afd73-55a5-4bb9-8c21-0b1fc84ea9e4"
  - "PSEXEC Remote Execution File Artefact"
attack_technique_ids:
  - "T1136.002"
  - "T1543.003"
  - "T1570"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PSEXEC Remote Execution File Artefact

Detects creation of the PSEXEC key file. Which is created anytime a PsExec command is executed. It gets written to the file system and will be recorded in the USN Journal on the target system

## Metadata

- Rule ID: 304afd73-55a5-4bb9-8c21-0b1fc84ea9e4
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-21
- Modified: 2023-02-23
- Source Path: rules/windows/file/file_event/file_event_win_sysinternals_psexec_service_key.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.002]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]
- [[kb/attack/techniques/T1570-lateral_tool_transfer|T1570]]

### Software Tags

- S0029

## Detection

```yaml
selection:
  TargetFilename|startswith: C:\Windows\PSEXEC-
  TargetFilename|endswith: .key
condition: selection
```

## False Positives

- Unlikely

## References

- https://aboutdfir.com/the-key-to-identify-psexec/
- https://twitter.com/davisrichardg/status/1616518800584704028

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_psexec_service_key.yml)
