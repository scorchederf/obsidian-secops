---
atomic_guid: "3d2cd093-ee05-41bd-a802-59ee5c301b85"
title: "Login as nobody (Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-27 19:12:26"
executor: "bash"
aliases:
  - "3d2cd093-ee05-41bd-a802-59ee5c301b85"
  - "Login as nobody (Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may try to re-purpose a system account to appear legitimate. In this test change the login shell of the nobody account, change its password to nobody, su to nobody, exit, then reset nobody's shell to /usr/sbin/nologin. Here is how the nobody entry should look like in `/etc/passwd` before the test is executed and right after the cleanup: `# -> nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin`

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
cat /etc/passwd |grep nobody
chsh --shell /bin/bash nobody
usermod --password $(openssl passwd -1 nobody) nobody
su -c "whoami" nobody
```

### Cleanup

```bash
chsh --shell /usr/sbin/nologin nobody
cat /etc/passwd |grep nobody
# -> nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
