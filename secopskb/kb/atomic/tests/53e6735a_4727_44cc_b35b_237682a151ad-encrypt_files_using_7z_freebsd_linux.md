---
atomic_guid: "53e6735a-4727-44cc-b35b-237682a151ad"
title: "Encrypt files using 7z (FreeBSD/Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1486"
attack_technique_name: "Data Encrypted for Impact"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "53e6735a-4727-44cc-b35b-237682a151ad"
  - "Encrypt files using 7z (FreeBSD/Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Encrypt files using 7z (FreeBSD/Linux)

Uses 7z to encrypt a file

## Metadata

- Atomic GUID: 53e6735a-4727-44cc-b35b-237682a151ad
- Technique: T1486: Data Encrypted for Impact
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Dependency Executor: bash
- Source Path: atomics/T1486/T1486.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]

## Input Arguments

### encrypted_file_path

- description: path to the encrypted file
- type: path
- default: /tmp/passwd.zip

### input_file_path

- description: path to the file that you want to encrypt
- type: path
- default: /etc/passwd

### pwd_for_encrypted_file

- description: the password that you want for the encrypted file
- type: string
- default: passwd

## Dependencies

Finds where 7z is located

### Prerequisite Check

```text
which_7z=`which 7z`
```

### Get Prerequisite

```text
(which pkg && pkg install -y 7-zip)
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
$which_7z a -p#{pwd_for_encrypted_file} #{encrypted_file_path} #{input_file_path}
```

### Cleanup

```sh
$which_7z e #{encrypted_file_path}
rm #{encrypted_file_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml)
