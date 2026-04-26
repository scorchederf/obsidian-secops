---
sigma_id: "3eb8c339-a765-48cc-a150-4364c04652bf"
title: "IIS WebServer Access Logs Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_delete_iis_access_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_iis_access_logs.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / file_delete"
aliases:
  - "3eb8c339-a765-48cc-a150-4364c04652bf"
  - "IIS WebServer Access Logs Deleted"
attack_technique_ids:
  - "T1070"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# IIS WebServer Access Logs Deleted

Detects the deletion of IIS WebServer access logs which may indicate an attempt to destroy forensic evidence

## Metadata

- Rule ID: 3eb8c339-a765-48cc-a150-4364c04652bf
- Status: test
- Level: medium
- Author: Tim Rauch (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-16
- Modified: 2023-02-15
- Source Path: rules/windows/file/file_delete/file_delete_win_delete_iis_access_logs.yml

## Logsource

- category: file_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]

## Detection

```yaml
selection:
  TargetFilename|contains: \inetpub\logs\LogFiles\
  TargetFilename|endswith: .log
condition: selection
```

## False Positives

- During uninstallation of the IIS service
- During log rotation

## References

- https://www.elastic.co/guide/en/security/current/webserver-access-logs-deleted.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_iis_access_logs.yml)
