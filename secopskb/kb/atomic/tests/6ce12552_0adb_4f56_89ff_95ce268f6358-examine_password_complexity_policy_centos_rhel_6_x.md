---
atomic_guid: "6ce12552-0adb-4f56-89ff-95ce268f6358"
title: "Examine password complexity policy - CentOS/RHEL 6.x"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-27 19:12:27"
executor: "bash"
aliases:
  - "6ce12552-0adb-4f56-89ff-95ce268f6358"
  - "Examine password complexity policy - CentOS/RHEL 6.x"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Lists the password complexity policy to console on CentOS/RHEL 6.x Linux.

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201: Password Policy Discovery]]

## Dependencies

System must be CentOS or RHEL v6

### Prerequisite Check

```untitled
if [ $(rpm -q --queryformat '%{VERSION}') -eq "6" ]; then exit /b 0; else exit /b 1; fi;
```

### Get Prerequisite

```untitled
echo Please run from CentOS or RHEL v6
```

## Executor

- name: bash

### Command

```bash
cat /etc/pam.d/system-auth
cat /etc/security/pwquality.conf
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
