---
atomic_guid: "5f8abd62-f615-43c5-b6be-f780f25790a1"
title: "Disable Bash History Logging with SSH -T"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "5f8abd62-f615-43c5-b6be-f780f25790a1"
  - "Disable Bash History Logging with SSH -T"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Bash History Logging with SSH -T

Keeps history clear and stays out of lastlog,wtmp,btmp ssh -T keeps the ssh client from catching a proper TTY, which is what usually gets logged on lastlog

## Metadata

- Atomic GUID: 5f8abd62-f615-43c5-b6be-f780f25790a1
- Technique: T1070.003: Indicator Removal on Host: Clear Command History
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1070.003/T1070.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Dependencies

Install sshpass and create user account used for excuting

### Prerequisite Check

```text
$(getent passwd testuser1 >/dev/null) && $(which sshpass >/dev/null)
```

### Get Prerequisite

```text
[ "$(uname)" = 'FreeBSD' ] && pw useradd testuser1 -g wheel -s /bin/sh || /usr/sbin/useradd testuser1
[ "$(uname)" = 'FreeBSD' ] && echo 'pwd101!' | pw mod user testuser1 -h 0 || echo -e 'pwd101!\npwd101!' | passwd testuser1
(which yum && yum -y install epel-release sshpass)||(which apt-get && DEBIAN_FRONTEND=noninteractive apt-get install -y sshpass)||(which pkg && pkg install -y sshpass)
```

## Executor

- name: sh

### Command

```sh
sshpass -p 'pwd101!' ssh testuser1@localhost -T hostname
```

### Cleanup

```sh
[ "$(uname)" = 'FreeBSD' ] && rmuser -y testuser1 || userdel -f testuser1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
