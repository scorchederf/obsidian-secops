---
sigma_id: "41f407b5-3096-44ea-a74f-96d04fbc41be"
title: "Remote Access Tool - AnyDesk Execution With Known Revoked Signing Certificate"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_revoked_cert.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_revoked_cert.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "41f407b5-3096-44ea-a74f-96d04fbc41be"
  - "Remote Access Tool - AnyDesk Execution With Known Revoked Signing Certificate"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - AnyDesk Execution With Known Revoked Signing Certificate

Detects the execution of an AnyDesk binary with a version prior to 8.0.8.
Prior to version 8.0.8, the Anydesk application used a signing certificate that got compromised by threat actors.
Use this rule to detect instances of older versions of Anydesk using the compromised certificate
This is recommended in order to avoid attackers leveraging the certificate and signing their binaries to bypass detections.

## Metadata

- Rule ID: 41f407b5-3096-44ea-a74f-96d04fbc41be
- Status: test
- Level: medium
- Author: Sai Prashanth Pulisetti, Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-02-08
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_revoked_cert.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \AnyDesk.exe
- Description: AnyDesk
- Product: AnyDesk
- Company: AnyDesk Software GmbH
selection_version:
  FileVersion|startswith:
  - 7.0.
  - 7.1.
  - 8.0.1
  - 8.0.2
  - 8.0.3
  - 8.0.4
  - 8.0.5
  - 8.0.6
  - 8.0.7
filter_main_uninstall:
  CommandLine|contains:
  - ' --remove'
  - ' --uninstall'
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://www.bleepingcomputer.com/news/security/anydesk-says-hackers-breached-its-production-servers-reset-passwords/
- https://anydesk.com/en/changelog/windows

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_revoked_cert.yml)
