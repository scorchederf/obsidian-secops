---
sigma_id: "b237c54b-0f15-4612-a819-44b735e0de27"
title: "A Security-Enabled Global Group Was Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_security_enabled_global_group_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_security_enabled_global_group_deleted.yml"
build_date: "2026-04-26 14:14:19"
status: "stable"
level: "low"
logsource: "windows / security"
aliases:
  - "b237c54b-0f15-4612-a819-44b735e0de27"
  - "A Security-Enabled Global Group Was Deleted"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# A Security-Enabled Global Group Was Deleted

Detects activity when a security-enabled global group is deleted

## Metadata

- Rule ID: b237c54b-0f15-4612-a819-44b735e0de27
- Status: stable
- Level: low
- Author: Alexandr Yampolskyi, SOC Prime
- Date: 2023-04-26
- Source Path: rules/windows/builtin/security/account_management/win_security_security_enabled_global_group_deleted.yml

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
  - 4730
  - 634
condition: selection
```

## False Positives

- Unknown

## References

- https://www.cisecurity.org/controls/cis-controls-list/
- https://www.pcisecuritystandards.org/documents/PCI_DSS_v3-2-1.pdf
- https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf
- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4730
- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=634

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_security_enabled_global_group_deleted.yml)
