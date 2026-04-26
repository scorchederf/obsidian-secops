---
sigma_id: "89c42960-f244-4dad-9151-ae9b1a3287a2"
title: "Suspicious File Write to Webapps Root Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_file_write_in_webapps_root.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_file_write_in_webapps_root.yml"
build_date: "2026-04-26 14:14:36"
status: "experimental"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "89c42960-f244-4dad-9151-ae9b1a3287a2"
  - "Suspicious File Write to Webapps Root Directory"
attack_technique_ids:
  - "T1505.003"
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious File Write to Webapps Root Directory

Detects suspicious file writes to the root directory of web applications, particularly Apache web servers or Tomcat servers.
This may indicate an attempt to deploy malicious files such as web shells or other unauthorized scripts.

## Metadata

- Rule ID: 89c42960-f244-4dad-9151-ae9b1a3287a2
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-10-20
- Source Path: rules/windows/file/file_event/file_event_win_susp_file_write_in_webapps_root.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]
- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection_susp_img:
  Image|endswith:
  - \dotnet.exe
  - \w3wp.exe
  - \java.exe
selection_servers:
  TargetFilename|contains:
  - \apache
  - \tomcat
selection_path:
  TargetFilename|contains: \webapps\ROOT\
selection_susp_extensions:
  TargetFilename|endswith: .jsp
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://labs.watchtowr.com/guess-who-would-be-stupid-enough-to-rob-the-same-vault-twice-pre-auth-rce-chains-in-commvault/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_file_write_in_webapps_root.yml)
