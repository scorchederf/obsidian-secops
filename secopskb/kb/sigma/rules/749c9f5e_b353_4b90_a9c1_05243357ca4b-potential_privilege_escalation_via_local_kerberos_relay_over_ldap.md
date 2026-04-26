---
sigma_id: "749c9f5e-b353-4b90-a9c1-05243357ca4b"
title: "Potential Privilege Escalation via Local Kerberos Relay over LDAP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_susp_privesc_kerberos_relay_over_ldap.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_susp_privesc_kerberos_relay_over_ldap.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "749c9f5e-b353-4b90-a9c1-05243357ca4b"
  - "Potential Privilege Escalation via Local Kerberos Relay over LDAP"
attack_technique_ids:
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Privilege Escalation via Local Kerberos Relay over LDAP

Detects a suspicious local successful logon event where the Logon Package is Kerberos, the remote address is set to localhost, and the target user SID is the built-in local Administrator account.
This may indicate an attempt to leverage a Kerberos relay attack variant that can be used to elevate privilege locally from a domain joined limited user to local System privileges.

## Metadata

- Rule ID: 749c9f5e-b353-4b90-a9c1-05243357ca4b
- Status: test
- Level: high
- Author: Elastic, @SBousseaden
- Date: 2022-04-27
- Modified: 2024-08-13
- Source Path: rules/windows/builtin/security/account_management/win_security_susp_privesc_kerberos_relay_over_ldap.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]

## Detection

```yaml
selection:
  EventID: 4624
  LogonType: 3
  AuthenticationPackageName: Kerberos
  IpAddress: 127.0.0.1
  TargetUserSid|startswith: S-1-5-21-
  TargetUserSid|endswith: '-500'
filter_main_ip_null:
  IpPort: '0'
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/sbousseaden/status/1518976397364056071?s=12&t=qKO5eKHvWhAP19a50FTZ7g
- https://github.com/elastic/detection-rules/blob/5fe7833312031a4787e07893e27e4ea7a7665745/rules/_deprecated/privilege_escalation_krbrelayup_suspicious_logon.toml#L38

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_susp_privesc_kerberos_relay_over_ldap.yml)
