---
atomic_guid: "c7ac59cb-13cc-4622-81dc-6d2fee9bfac7"
title: "Change login shell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "bash"
aliases:
  - "c7ac59cb-13cc-4622-81dc-6d2fee9bfac7"
  - "Change login shell"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may want to use a different login shell. The chsh command changes the user login shell. The following test, creates an art user with a /bin/bash shell, changes the users shell to sh, then deletes the art user.

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]

## Dependencies

chsh - change login shell, must be installed

### Prerequisite Check

```untitled
if [ -f /usr/bin/chsh ]; then echo "exit 0"; else echo "exit 1"; exit 1; fi
```

### Get Prerequisite

```untitled
echo "Automated installer not implemented yet, please install chsh manually"
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
[ "$(uname)" = 'FreeBSD' ] && pw useradd art -g wheel -s /bin/csh || useradd -s /bin/bash art
cat /etc/passwd |grep ^art
chsh -s /bin/sh art
cat /etc/passwd |grep ^art
```

### Cleanup

```bash
[ "$(uname)" = 'FreeBSD' ] && rmuser -y art || userdel art
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
