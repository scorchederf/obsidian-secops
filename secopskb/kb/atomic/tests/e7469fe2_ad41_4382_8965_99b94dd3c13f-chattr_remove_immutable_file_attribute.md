---
atomic_guid: "e7469fe2-ad41-4382-8965-99b94dd3c13f"
title: "chattr - Remove immutable file attribute"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.002"
attack_technique_name: "File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "e7469fe2-ad41-4382-8965-99b94dd3c13f"
  - "chattr - Remove immutable file attribute"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# chattr - Remove immutable file attribute

Remove's a file's `immutable` attribute using `chattr`.
This technique was used by the threat actor Rocke during the compromise of Linux web servers.

## Metadata

- Atomic GUID: e7469fe2-ad41-4382-8965-99b94dd3c13f
- Technique: T1222.002: File and Directory Permissions Modification: FreeBSD, Linux and Mac File and Directory Permissions Modification
- Platforms: macos, linux
- Executor: sh
- Source Path: atomics/T1222.002/T1222.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.002]]

## Input Arguments

### file_to_modify

- description: Path of the file
- type: path
- default: /var/spool/cron/root

## Executor

- name: sh

### Command

```bash
chattr -i #{file_to_modify}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.002/T1222.002.yaml)
