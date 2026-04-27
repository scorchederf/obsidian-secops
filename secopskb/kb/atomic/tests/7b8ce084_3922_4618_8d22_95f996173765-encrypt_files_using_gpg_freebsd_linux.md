---
atomic_guid: "7b8ce084-3922-4618-8d22-95f996173765"
title: "Encrypt files using gpg (FreeBSD/Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1486"
attack_technique_name: "Data Encrypted for Impact"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "7b8ce084-3922-4618-8d22-95f996173765"
  - "Encrypt files using gpg (FreeBSD/Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Uses gpg to encrypt a file

## ATT&CK Mapping

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]]

## Input Arguments

### encrypted_file_path

- description: path to the encrypted file
- type: path
- default: /tmp/passwd.gpg

### encryption_alg

- description: encryption algorithm of the file
- type: string
- default: AES-256

### input_file_path

- description: path to the file that you want to encrypt
- type: path
- default: /etc/passwd

### pwd_for_encrypted_file

- description: the password that you want for the encrypted file
- type: string
- default: passwd

## Dependencies

Finds where gpg is located

### Prerequisite Check

```bash
which_gpg=`which gpg`
```

### Get Prerequisite

```bash
(which pkg && pkg install -y gnupg)||(which yum && yum -y install epel-release gpg)||(which apt-get && DEBIAN_FRONTEND=noninteractive apt-get install -y gpg)
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
echo "#{pwd_for_encrypted_file}" | $which_gpg --batch --yes --passphrase-fd 0 --cipher-algo #{encryption_alg} -o #{encrypted_file_path} -c #{input_file_path}
```

### Cleanup

```bash
rm #{encrypted_file_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml)
