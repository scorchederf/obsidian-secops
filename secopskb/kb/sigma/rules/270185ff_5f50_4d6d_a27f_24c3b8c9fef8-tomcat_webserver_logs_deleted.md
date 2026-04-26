---
sigma_id: "270185ff-5f50-4d6d-a27f-24c3b8c9fef8"
title: "Tomcat WebServer Logs Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_delete_tomcat_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_tomcat_logs.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / file_delete"
aliases:
  - "270185ff-5f50-4d6d-a27f-24c3b8c9fef8"
  - "Tomcat WebServer Logs Deleted"
attack_technique_ids:
  - "T1070"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Tomcat WebServer Logs Deleted

Detects the deletion of tomcat WebServer logs which may indicate an attempt to destroy forensic evidence

## Metadata

- Rule ID: 270185ff-5f50-4d6d-a27f-24c3b8c9fef8
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-16
- Source Path: rules/windows/file/file_delete/file_delete_win_delete_tomcat_logs.yml

## Logsource

- category: file_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]

## Detection

```yaml
selection:
  TargetFilename|contains|all:
  - \Tomcat
  - \logs\
  TargetFilename|contains:
  - catalina.
  - _access_log.
  - localhost.
condition: selection
```

## False Positives

- During uninstallation of the tomcat server
- During log rotation

## References

- Internal Research
- https://linuxhint.com/view-tomcat-logs-windows/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_tomcat_logs.yml)
