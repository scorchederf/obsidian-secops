---
sigma_id: "9e4b7d3a-6f2c-4e9a-8d1b-3c5e7a9f2b4d"
title: "Potentially Suspicious File Creation by OpenEDR's ITSMService"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_comodo_itsm_potentially_suspicious_file_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_comodo_itsm_potentially_suspicious_file_creation.yml"
build_date: "2026-04-26 14:14:33"
status: "experimental"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "9e4b7d3a-6f2c-4e9a-8d1b-3c5e7a9f2b4d"
  - "Potentially Suspicious File Creation by OpenEDR's ITSMService"
attack_technique_ids:
  - "T1105"
  - "T1570"
  - "T1219"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious File Creation by OpenEDR's ITSMService

Detects the creation of potentially suspicious files by OpenEDR's ITSMService process.
The ITSMService is responsible for remote management operations and can create files on the system through the Process Explorer or file management features.
While legitimate for IT operations, creation of executable or script files could indicate unauthorized file uploads, data staging, or malicious file deployment.

## Metadata

- Rule ID: 9e4b7d3a-6f2c-4e9a-8d1b-3c5e7a9f2b4d
- Status: experimental
- Level: medium
- Author: @kostastsale
- Date: 2026-02-19
- Source Path: rules/windows/file/file_event/file_event_win_comodo_itsm_potentially_suspicious_file_creation.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]
- [[kb/attack/techniques/T1570-lateral_tool_transfer|T1570]]
- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Detection

```yaml
selection_process:
  Image|endswith: \COMODO\Endpoint Manager\ITSMService.exe
selection_suspicious_extensions:
  TargetFilename|endswith:
  - .7z
  - .bat
  - .cmd
  - .com
  - .dll
  - .exe
  - .hta
  - .js
  - .pif
  - .ps1
  - .rar
  - .scr
  - .vbe
  - .vbs
  - .zip
condition: all of selection_*
```

## False Positives

- Legitimate OpenEDR file management operations
- Authorized remote file uploads by IT administrators
- Software deployment through OpenEDR console

## References

- https://kostas-ts.medium.com/detecting-abuse-of-openedrs-permissive-edr-trial-a-security-researcher-s-perspective-fc55bf53972c

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_comodo_itsm_potentially_suspicious_file_creation.yml)
