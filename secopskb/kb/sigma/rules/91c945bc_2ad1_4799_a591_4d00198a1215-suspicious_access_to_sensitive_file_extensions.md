---
sigma_id: "91c945bc-2ad1-4799-a591-4d00198a1215"
title: "Suspicious Access to Sensitive File Extensions"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_raccess_sensitive_fext.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_raccess_sensitive_fext.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "91c945bc-2ad1-4799-a591-4d00198a1215"
  - "Suspicious Access to Sensitive File Extensions"
attack_technique_ids:
  - "T1039"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Access to Sensitive File Extensions

Detects known sensitive file extensions accessed on a network share

## Metadata

- Rule ID: 91c945bc-2ad1-4799-a591-4d00198a1215
- Status: test
- Level: medium
- Author: Samir Bousseaden
- Date: 2019-04-03
- Modified: 2025-10-17
- Source Path: rules/windows/builtin/security/win_security_susp_raccess_sensitive_fext.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1039-data_from_network_shared_drive|T1039]]

## Detection

```yaml
selection:
  EventID: 5145
  RelativeTargetName|endswith:
  - .bak
  - .dmp
  - .edb
  - .kirbi
  - .msg
  - .nsf
  - .nst
  - .oab
  - .ost
  - .pst
  - .rdp
condition: selection
```

## False Positives

- Help Desk operator doing backup or re-imaging end user machine or backup software
- Users working with these data types or exchanging message files

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_raccess_sensitive_fext.yml)
