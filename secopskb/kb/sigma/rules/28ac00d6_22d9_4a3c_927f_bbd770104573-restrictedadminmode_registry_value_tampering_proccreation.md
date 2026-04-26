---
sigma_id: "28ac00d6-22d9-4a3c-927f-bbd770104573"
title: "RestrictedAdminMode Registry Value Tampering - ProcCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_lsa_disable_restricted_admin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_lsa_disable_restricted_admin.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "28ac00d6-22d9-4a3c-927f-bbd770104573"
  - "RestrictedAdminMode Registry Value Tampering - ProcCreation"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# RestrictedAdminMode Registry Value Tampering - ProcCreation

Detects changes to the "DisableRestrictedAdmin" registry value in order to disable or enable RestrictedAdmin mode.
RestrictedAdmin mode prevents the transmission of reusable credentials to the remote system to which you connect using Remote Desktop.
This prevents your credentials from being harvested during the initial connection process if the remote server has been compromise

## Metadata

- Rule ID: 28ac00d6-22d9-4a3c-927f-bbd770104573
- Status: test
- Level: high
- Author: frack113
- Date: 2023-01-13
- Modified: 2025-08-28
- Source Path: rules/windows/process_creation/proc_creation_win_reg_lsa_disable_restricted_admin.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \System\CurrentControlSet\Control\Lsa
  - DisableRestrictedAdmin
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/a8e3cf63e97b973a25903d3df9fd55da6252e564/atomics/T1112/T1112.md
- https://social.technet.microsoft.com/wiki/contents/articles/32905.remote-desktop-services-enable-restricted-admin-mode.aspx
- https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_lsa_disable_restricted_admin.yml)
