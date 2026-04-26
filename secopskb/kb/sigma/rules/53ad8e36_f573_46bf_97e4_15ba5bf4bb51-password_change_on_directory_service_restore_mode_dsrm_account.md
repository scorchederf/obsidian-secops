---
sigma_id: "53ad8e36-f573-46bf-97e4-15ba5bf4bb51"
title: "Password Change on Directory Service Restore Mode (DSRM) Account"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_dsrm_password_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_dsrm_password_change.yml"
build_date: "2026-04-26 17:03:20"
status: "stable"
level: "high"
logsource: "windows / security"
aliases:
  - "53ad8e36-f573-46bf-97e4-15ba5bf4bb51"
  - "Password Change on Directory Service Restore Mode (DSRM) Account"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password Change on Directory Service Restore Mode (DSRM) Account

Detects potential attempts made to set the Directory Services Restore Mode administrator password.
The Directory Service Restore Mode (DSRM) account is a local administrator account on Domain Controllers.
Attackers may change the password in order to obtain persistence.

## Metadata

- Rule ID: 53ad8e36-f573-46bf-97e4-15ba5bf4bb51
- Status: stable
- Level: high
- Author: Thomas Patzke
- Date: 2017-02-19
- Modified: 2020-08-23
- Source Path: rules/windows/builtin/security/win_security_susp_dsrm_password_change.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  EventID: 4794
condition: selection
```

## False Positives

- Initial installation of a domain controller.

## References

- https://adsecurity.org/?p=1714
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4794

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_dsrm_password_change.yml)
