---
sigma_id: "ca94a6db-8106-4737-9ed2-3e3bb826af0a"
title: "Password Policy Discovery - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/lnx_auditd_password_policy_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_password_policy_discovery.yml"
build_date: "2026-04-26 14:14:30"
status: "stable"
level: "low"
logsource: "linux / auditd"
aliases:
  - "ca94a6db-8106-4737-9ed2-3e3bb826af0a"
  - "Password Policy Discovery - Linux"
attack_technique_ids:
  - "T1201"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Password Policy Discovery - Linux

Detects password policy discovery commands

## Metadata

- Rule ID: ca94a6db-8106-4737-9ed2-3e3bb826af0a
- Status: stable
- Level: low
- Author: Ömer Günal, oscd.community, Pawel Mazur
- Date: 2020-10-08
- Modified: 2024-12-01
- Source Path: rules/linux/auditd/lnx_auditd_password_policy_discovery.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201]]

## Detection

```yaml
selection_files:
  type: PATH
  name:
  - /etc/login.defs
  - /etc/pam.d/auth
  - /etc/pam.d/common-account
  - /etc/pam.d/common-auth
  - /etc/pam.d/common-password
  - /etc/pam.d/system-auth
  - /etc/security/pwquality.conf
selection_chage:
  type: EXECVE
  a0: chage
  a1:
  - --list
  - -l
selection_passwd:
  type: EXECVE
  a0: passwd
  a1:
  - -S
  - --status
condition: 1 of selection_*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1201/T1201.md
- https://linux.die.net/man/1/chage
- https://man7.org/linux/man-pages/man1/passwd.1.html
- https://superuser.com/questions/150675/how-to-display-password-policy-information-for-a-user-ubuntu

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_password_policy_discovery.yml)
