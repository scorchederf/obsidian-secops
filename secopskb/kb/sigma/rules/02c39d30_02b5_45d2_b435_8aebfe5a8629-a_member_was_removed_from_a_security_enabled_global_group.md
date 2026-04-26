---
sigma_id: "02c39d30-02b5-45d2-b435-8aebfe5a8629"
title: "A Member Was Removed From a Security-Enabled Global Group"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_member_removed_security_enabled_global_group.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_member_removed_security_enabled_global_group.yml"
build_date: "2026-04-26 14:14:19"
status: "stable"
level: "low"
logsource: "windows / security"
aliases:
  - "02c39d30-02b5-45d2-b435-8aebfe5a8629"
  - "A Member Was Removed From a Security-Enabled Global Group"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# A Member Was Removed From a Security-Enabled Global Group

Detects activity when a member is removed from a security-enabled global group

## Metadata

- Rule ID: 02c39d30-02b5-45d2-b435-8aebfe5a8629
- Status: stable
- Level: low
- Author: Alexandr Yampolskyi, SOC Prime
- Date: 2023-04-26
- Source Path: rules/windows/builtin/security/account_management/win_security_member_removed_security_enabled_global_group.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  EventID:
  - 633
  - 4729
condition: selection
```

## False Positives

- Unknown

## References

- https://www.cisecurity.org/controls/cis-controls-list/
- https://www.pcisecuritystandards.org/documents/PCI_DSS_v3-2-1.pdf
- https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf
- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4729
- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=633

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_member_removed_security_enabled_global_group.yml)
