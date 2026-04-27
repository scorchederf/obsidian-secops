---
atomic_guid: "0286eb44-e7ce-41a0-b109-3da516e05a5f"
title: "Data Encrypted with zip and gpg symmetric"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "0286eb44-e7ce-41a0-b109-3da516e05a5f"
  - "Data Encrypted with zip and gpg symmetric"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Encrypt data for exiltration

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]

## Input Arguments

### encryption_password

- description: Password used to encrypt data.
- type: string
- default: InsertPasswordHere

### test_file

- description: Temp file used to store encrypted data.
- type: path
- default: T1560

### test_folder

- description: Path used to store files.
- type: path
- default: /tmp/T1560

## Dependencies

gpg and zip are required to run the test.

### Prerequisite Check

```bash
if [ ! -x "$(command -v gpg)" ] || [ ! -x "$(command -v zip)" ]; then exit 1; fi;
```

### Get Prerequisite

```bash
(which pkg && pkg install -y gnupg zip)||(which yum && yum -y install epel-release zip gpg)||(which apt-get && apt-get install -y zip gpg)
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
mkdir -p #{test_folder}
cd #{test_folder}; touch a b c d e f g
zip --password "#{encryption_password}" #{test_folder}/#{test_file} ./*
echo "#{encryption_password}" | gpg --batch --yes --passphrase-fd 0 --output #{test_folder}/#{test_file}.zip.gpg -c #{test_folder}/#{test_file}.zip
ls -l #{test_folder}
```

### Cleanup

```bash
rm -Rf #{test_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
