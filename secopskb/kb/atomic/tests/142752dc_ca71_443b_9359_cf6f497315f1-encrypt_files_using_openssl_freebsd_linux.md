---
atomic_guid: "142752dc-ca71-443b-9359-cf6f497315f1"
title: "Encrypt files using openssl (FreeBSD/Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1486"
attack_technique_name: "Data Encrypted for Impact"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "142752dc-ca71-443b-9359-cf6f497315f1"
  - "Encrypt files using openssl (FreeBSD/Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Encrypt files using openssl (FreeBSD/Linux)

Uses openssl to encrypt a file

## Metadata

- Atomic GUID: 142752dc-ca71-443b-9359-cf6f497315f1
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

### encryption_bit_size

- description: size of the bit of encryption
- type: integer
- default: 2048

### input_file_path

- description: path to the file that you want to encrypt
- type: path
- default: /etc/passwd

### private_key_path

- description: path to the private key
- type: path
- default: /tmp/key.pem

### public_key_path

- description: path to the public key
- type: path
- default: /tmp/pub.pem

## Dependencies

Finds where openssl is located

### Prerequisite Check

```text
which_openssl=`which openssl`
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
which_openssl=`which openssl`
$which_openssl genrsa -out #{private_key_path} #{encryption_bit_size}
$which_openssl rsa -in #{private_key_path} -pubout -out #{public_key_path}
$which_openssl rsautl -encrypt -inkey #{public_key_path} -pubin -in #{input_file_path} -out #{encrypted_file_path}
```

### Cleanup

```sh
$which_openssl rsautl -decrypt -inkey #{private_key_path} -in #{encrypted_file_path}
rm #{encrypted_file_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml)
