---
atomic_guid: "08cbf59f-85da-4369-a5f4-049cffd7709f"
title: "Encrypt files using ccrypt (FreeBSD/Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1486"
attack_technique_name: "Data Encrypted for Impact"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "08cbf59f-85da-4369-a5f4-049cffd7709f"
  - "Encrypt files using ccrypt (FreeBSD/Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Encrypt files using ccrypt (FreeBSD/Linux)

Attempts to encrypt data on target systems as root to simulate an interruption authentication to target system. If root permissions are not available then attempts to encrypt data within user's home directory.

## Metadata

- Atomic GUID: 08cbf59f-85da-4369-a5f4-049cffd7709f
- Technique: T1486: Data Encrypted for Impact
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1486/T1486.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]

## Input Arguments

### cped_file_path

- description: Path where you want your copied file to be
- type: path
- default: /tmp/passwd

### pwd_for_encrypted_file

- description: Password to use for encryption
- type: string
- default: passwd

### root_input_file_path

- description: Path the target file to be encrypted. File will be copied to /tmp/ before encrypting
- type: path
- default: /etc/passwd

## Dependencies

Finds where ccencrypt and ccdecrypt are located

### Prerequisite Check

```bash
which_ccencrypt=`which ccencrypt`
which_ccdecrypt=`which ccdecrypt`
```

### Get Prerequisite

```bash
(which pkg && pkg install -y ccript)||(which yum && yum -y install epel-release ccrypt)||(which apt-get && DEBIAN_FRONTEND=noninteractive apt-get install -y ccrypt)
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
which_ccencrypt=`which ccencrypt`
cp #{root_input_file_path} #{cped_file_path};
$which_ccencrypt -T -K #{pwd_for_encrypted_file} #{cped_file_path}
```

### Cleanup

```bash
rm #{cped_file_path}.cpt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml)
