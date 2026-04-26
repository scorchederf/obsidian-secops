---
atomic_guid: "16f6374f-7600-459a-9b16-6a88fd96d310"
title: "Login as nobody (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "16f6374f-7600-459a-9b16-6a88fd96d310"
  - "Login as nobody (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Login as nobody (freebsd)

An adversary may try to re-purpose a system account to appear legitimate. In this test change the login shell of the nobody account, change its password to nobody, su to nobody, exit, then reset nobody's shell to /usr/sbin/nologin. Here is how the nobody entry should look like in `/etc/passwd` before the test is executed and right after the cleanup: `# -> nobody:x:65534:65534:Unprivileged user:/nonexistent:/usr/sbin/nologin`

## Metadata

- Atomic GUID: 16f6374f-7600-459a-9b16-6a88fd96d310
- Technique: T1078.003: Valid Accounts: Local Accounts
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1078.003/T1078.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
cat /etc/passwd |grep nobody
pw usermod nobody -s /bin/sh
echo $(openssl passwd -1 art) | pw mod user nobody -h 0
su nobody
whoami
exit
```

### Cleanup

```bash
pw usermod nobody -s /usr/sbin/nologin
cat /etc/passwd |grep nobody
# -> nobody:*:65534:65534:Unprivileged user:/nonexistent:/usr/sbin/nologin
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
