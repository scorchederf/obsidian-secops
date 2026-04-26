---
atomic_guid: "3723ab77-c546-403c-8fb4-bb577033b235"
title: "Access /etc/shadow (Local)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.008"
attack_technique_name: "OS Credential Dumping: /etc/passwd, /etc/master.passwd and /etc/shadow"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.008/T1003.008.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "3723ab77-c546-403c-8fb4-bb577033b235"
  - "Access /etc/shadow (Local)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Access /etc/shadow (Local)

/etc/shadow file is accessed in Linux environments

## Metadata

- Atomic GUID: 3723ab77-c546-403c-8fb4-bb577033b235
- Technique: T1003.008: OS Credential Dumping: /etc/passwd, /etc/master.passwd and /etc/shadow
- Platforms: linux
- Executor: bash
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
- name: bash

### Command

```bash
sudo cat /etc/shadow > #{output_file}
cat #{output_file}
```

### Cleanup

```bash
rm -f #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.008/T1003.008.yaml)
