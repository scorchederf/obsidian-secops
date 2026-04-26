---
sigma_id: "f7644214-0eb0-4ace-9455-331ec4c09253"
title: "Kerberos Manipulation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_kerberos_manipulation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_kerberos_manipulation.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "f7644214-0eb0-4ace-9455-331ec4c09253"
  - "Kerberos Manipulation"
attack_technique_ids:
  - "T1212"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Kerberos Manipulation

Detects failed Kerberos TGT issue operation. This can be a sign of manipulations of TGT messages by an attacker.

## Metadata

- Rule ID: f7644214-0eb0-4ace-9455-331ec4c09253
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-02-10
- Modified: 2024-01-16
- Source Path: rules/windows/builtin/security/win_security_susp_kerberos_manipulation.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1212-exploitation_for_credential_access|T1212]]

## Detection

```yaml
selection:
  EventID:
  - 675
  - 4768
  - 4769
  - 4771
  Status:
  - '0x9'
  - '0xA'
  - '0xB'
  - '0xF'
  - '0x10'
  - '0x11'
  - '0x13'
  - '0x14'
  - '0x1A'
  - '0x1F'
  - '0x21'
  - '0x22'
  - '0x23'
  - '0x24'
  - '0x26'
  - '0x27'
  - '0x28'
  - '0x29'
  - '0x2C'
  - '0x2D'
  - '0x2E'
  - '0x2F'
  - '0x31'
  - '0x32'
  - '0x3E'
  - '0x3F'
  - '0x40'
  - '0x41'
  - '0x43'
  - '0x44'
condition: selection
```

## False Positives

- Faulty legacy applications

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4771

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_kerberos_manipulation.yml)
