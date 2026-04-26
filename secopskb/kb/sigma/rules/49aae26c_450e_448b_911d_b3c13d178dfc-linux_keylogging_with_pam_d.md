---
sigma_id: "49aae26c-450e-448b-911d-b3c13d178dfc"
title: "Linux Keylogging with Pam.d"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/lnx_auditd_keylogging_with_pam_d.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_keylogging_with_pam_d.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "linux / auditd"
aliases:
  - "49aae26c-450e-448b-911d-b3c13d178dfc"
  - "Linux Keylogging with Pam.d"
attack_technique_ids:
  - "T1003"
  - "T1056.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Linux Keylogging with Pam.d

Detect attempt to enable auditing of TTY input

## Metadata

- Rule ID: 49aae26c-450e-448b-911d-b3c13d178dfc
- Status: test
- Level: high
- Author: Pawel Mazur
- Date: 2021-05-24
- Modified: 2022-12-18
- Source Path: rules/linux/auditd/lnx_auditd_keylogging_with_pam_d.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]
- [[kb/attack/techniques/T1056-input_capture|T1056.001]]

## Detection

```yaml
selection_path_events:
  type: PATH
  name:
  - /etc/pam.d/system-auth
  - /etc/pam.d/password-auth
selection_tty_events:
  type:
  - TTY
  - USER_TTY
condition: 1 of selection_*
```

## False Positives

- Administrative work

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1056.001/T1056.001.md
- https://linux.die.net/man/8/pam_tty_audit
- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/sec-configuring_pam_for_auditing
- https://access.redhat.com/articles/4409591#audit-record-types-2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_keylogging_with_pam_d.yml)
