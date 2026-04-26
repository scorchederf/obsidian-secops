---
sigma_id: "ee63c85c-6d51-4d12-ad09-04e25877a947"
title: "New Custom Shim Database Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_creation_new_shim_database.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_creation_new_shim_database.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "ee63c85c-6d51-4d12-ad09-04e25877a947"
  - "New Custom Shim Database Created"
attack_technique_ids:
  - "T1547.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Custom Shim Database Created

Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by application shims.
The Microsoft Windows Application Compatibility Infrastructure/Framework (Application Shim) was created to allow for backward compatibility of software as the operating system codebase changes over time.

## Metadata

- Rule ID: ee63c85c-6d51-4d12-ad09-04e25877a947
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-12-29
- Modified: 2023-12-06
- Source Path: rules/windows/file/file_event/file_event_win_creation_new_shim_database.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.009]]

## Detection

```yaml
selection:
  TargetFilename|contains:
  - :\Windows\apppatch\Custom\
  - :\Windows\apppatch\CustomSDB\
condition: selection
```

## False Positives

- Legitimate custom SHIM installations will also trigger this rule

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.011/T1546.011.md#atomic-test-2---new-shim-database-files-created-in-the-default-shim-database-directory
- https://www.mandiant.com/resources/blog/fin7-shim-databases-persistence
- https://liberty-shell.com/sec/2020/02/25/shim-persistence/
- https://andreafortuna.org/2018/11/12/process-injection-and-persistence-using-application-shimming/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_creation_new_shim_database.yml)
