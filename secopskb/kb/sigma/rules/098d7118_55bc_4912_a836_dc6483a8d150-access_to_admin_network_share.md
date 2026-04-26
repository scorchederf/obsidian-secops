---
sigma_id: "098d7118-55bc-4912-a836-dc6483a8d150"
title: "Access To ADMIN$ Network Share"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_admin_share_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_admin_share_access.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "low"
logsource: "windows / security"
aliases:
  - "098d7118-55bc-4912-a836-dc6483a8d150"
  - "Access To ADMIN$ Network Share"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Access To ADMIN$ Network Share

Detects access to ADMIN$ network share

## Metadata

- Rule ID: 098d7118-55bc-4912-a836-dc6483a8d150
- Status: test
- Level: low
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-04
- Modified: 2024-01-16
- Source Path: rules/windows/builtin/security/win_security_admin_share_access.yml

## Logsource

- definition: Requirements: The advanced audit policy setting "Object Access > Audit File Share" must be configured for Success/Failure
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection:
  EventID: 5140
  ShareName: Admin$
filter_main_computer_account:
  SubjectUserName|endswith: $
condition: selection and not 1 of filter_*
```

## False Positives

- Legitimate administrative activity

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-5140

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_admin_share_access.yml)
