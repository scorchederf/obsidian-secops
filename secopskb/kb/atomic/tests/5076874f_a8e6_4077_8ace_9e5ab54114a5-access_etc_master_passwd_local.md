---
atomic_guid: "5076874f-a8e6-4077-8ace-9e5ab54114a5"
title: "Access /etc/master.passwd (Local)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.008"
attack_technique_name: "OS Credential Dumping: /etc/passwd, /etc/master.passwd and /etc/shadow"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.008/T1003.008.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "5076874f-a8e6-4077-8ace-9e5ab54114a5"
  - "Access /etc/master.passwd (Local)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Access /etc/master.passwd (Local)

/etc/master.passwd file is accessed in FreeBSD environments

## Metadata

- Atomic GUID: 5076874f-a8e6-4077-8ace-9e5ab54114a5
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
sudo cat /etc/master.passwd > #{output_file}
cat #{output_file}
```

### Cleanup

```bash
rm -f #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.008/T1003.008.yaml)
