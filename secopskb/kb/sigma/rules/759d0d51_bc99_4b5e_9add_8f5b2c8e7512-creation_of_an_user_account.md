---
sigma_id: "759d0d51-bc99-4b5e-9add-8f5b2c8e7512"
title: "Creation Of An User Account"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/syscall/lnx_auditd_create_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_create_account.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "759d0d51-bc99-4b5e-9add-8f5b2c8e7512"
  - "Creation Of An User Account"
attack_technique_ids:
  - "T1136.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Creation Of An User Account

Detects the creation of a new user account. Such accounts may be used for persistence that do not require persistent remote access tools to be deployed on the system.

## Metadata

- Rule ID: 759d0d51-bc99-4b5e-9add-8f5b2c8e7512
- Status: test
- Level: medium
- Author: Marie Euler, Pawel Mazur
- Date: 2020-05-18
- Modified: 2022-12-20
- Source Path: rules/linux/auditd/syscall/lnx_auditd_create_account.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Detection

```yaml
selection_syscall_record_type:
  type: SYSCALL
  exe|endswith: /useradd
selection_add_user_record_type:
  type: ADD_USER
condition: 1 of selection_*
```

## False Positives

- Admin activity

## References

- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-understanding_audit_log_files
- https://access.redhat.com/articles/4409591#audit-record-types-2
- https://www.youtube.com/watch?v=VmvY5SQm5-Y&ab_channel=M45C07

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_create_account.yml)
