---
atomic_guid: "a743e3a6-e8b2-4a30-abe7-ca85d201b5d3"
title: "Encrypts collected data with AES-256 and Base64"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "a743e3a6-e8b2-4a30-abe7-ca85d201b5d3"
  - "Encrypts collected data with AES-256 and Base64"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Encrypts collected data with AES-256 and Base64

An adversary may compress all the collected data, encrypt and send them to a C2 server using base64 encoding. 
This atomic test tries to emulate the behaviour of the FLEXIROOT backdoor to archive the collected data. FLEXIROOT typically utilizes AES encryption and base64 encoding to transfer the encrypted data to the C2 server. 
In this test, standard zip compression and the OpenSSL library are used to encrypt the compressed data.
https://attack.mitre.org/versions/v7/software/S0267/

## Metadata

- Atomic GUID: a743e3a6-e8b2-4a30-abe7-ca85d201b5d3
- Technique: T1560.001: Archive Collected Data: Archive via Utility
- Platforms: linux, macos
- Executor: bash
- Elevation Required: False
- Dependency Executor: bash
- Source Path: atomics/T1560.001/T1560.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Input Arguments

### enc_pass

- description: Password used to encrypt the data
- type: string
- default: atomic_enc_pass

### input_file

- description: Name of the compressed and encrypted files
- type: string
- default: t1560_data

### input_folder

- description: Path to the folder used to store the test files
- type: path
- default: /tmp/t1560

## Dependencies

The folder and test files must exist

### Prerequisite Check

```bash
if [ ! -d #{input_folder} ]; then exit 1; else exit 0; fi;
```

### Get Prerequisite

```bash
if [ ! -d #{input_folder} ]; then mkdir -p #{input_folder}; cd #{input_folder}; touch {a..z}.data; fi;
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
zip -r  #{input_folder}/#{input_file}.zip #{input_folder}
openssl enc -aes-256-cbc -pass pass:#{enc_pass} -p -in #{input_folder}/#{input_file}.zip -out #{input_folder}/#{input_file}.enc 
cat #{input_folder}/#{input_file}.enc | base64
```

### Cleanup

```bash
rm -rf #{input_folder}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
