---
sigma_id: "c43c26be-2e87-46c7-8661-284588c5a53e"
title: "A Member Was Added to a Security-Enabled Global Group"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_member_added_security_enabled_global_group.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_member_added_security_enabled_global_group.yml"
build_date: "2026-04-26 14:14:19"
status: "stable"
level: "low"
logsource: "windows / security"
aliases:
  - "c43c26be-2e87-46c7-8661-284588c5a53e"
  - "A Member Was Added to a Security-Enabled Global Group"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# A Member Was Added to a Security-Enabled Global Group

Detects activity when a member is added to a security-enabled global group

## Metadata

- Rule ID: c43c26be-2e87-46c7-8661-284588c5a53e
- Status: stable
- Level: low
- Author: Alexandr Yampolskyi, SOC Prime
- Date: 2023-04-26
- Source Path: rules/windows/builtin/security/account_management/win_security_member_added_security_enabled_global_group.yml

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
  - 4728
  - 632
condition: selection
```

## False Positives

- Unknown

## References

- https://www.cisecurity.org/controls/cis-controls-list/
- https://www.pcisecuritystandards.org/documents/PCI_DSS_v3-2-1.pdf
- https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf
- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4728
- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=632

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_member_added_security_enabled_global_group.yml)
