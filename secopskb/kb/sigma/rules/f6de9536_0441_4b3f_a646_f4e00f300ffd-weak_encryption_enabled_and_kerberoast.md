---
sigma_id: "f6de9536-0441-4b3f-a646-f4e00f300ffd"
title: "Weak Encryption Enabled and Kerberoast"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_alert_enable_weak_encryption.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_alert_enable_weak_encryption.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "f6de9536-0441-4b3f-a646-f4e00f300ffd"
  - "Weak Encryption Enabled and Kerberoast"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Weak Encryption Enabled and Kerberoast

Detects scenario where weak encryption is enabled for a user profile which could be used for hash/password cracking.

## Metadata

- Rule ID: f6de9536-0441-4b3f-a646-f4e00f300ffd
- Status: test
- Level: high
- Author: @neu5ron
- Date: 2017-07-30
- Modified: 2021-11-27
- Source Path: rules/windows/builtin/security/win_security_alert_enable_weak_encryption.yml

## Logsource

- definition: Requirements: Audit Policy : Account Management > Audit User Account Management, Group Policy : Computer Configuration\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Account Management\Audit User Account Management
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  EventID: 4738
olduac_des:
  OldUacValue|endswith:
  - 8???
  - 9???
  - A???
  - B???
  - C???
  - D???
  - E???
  - F???
newuac_des:
  NewUacValue|endswith:
  - 8???
  - 9???
  - A???
  - B???
  - C???
  - D???
  - E???
  - F???
olduac_preauth:
  OldUacValue|endswith:
  - 1????
  - 3????
  - 5????
  - 7????
  - 9????
  - B????
  - D????
  - F????
newuac_preauth:
  NewUacValue|endswith:
  - 1????
  - 3????
  - 5????
  - 7????
  - 9????
  - B????
  - D????
  - F????
olduac_encrypted:
  OldUacValue|endswith:
  - 8??
  - 9??
  - A??
  - B??
  - C??
  - D??
  - E??
  - F??
newuac_encrypted:
  NewUacValue|endswith:
  - 8??
  - 9??
  - A??
  - B??
  - C??
  - D??
  - E??
  - F??
condition: selection and ((newuac_des and not olduac_des) or (newuac_preauth and not
  olduac_preauth) or (newuac_encrypted and not olduac_encrypted))
```

## False Positives

- Unknown

## References

- https://adsecurity.org/?p=2053
- https://blog.harmj0y.net/redteaming/another-word-on-delegation/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_alert_enable_weak_encryption.yml)
