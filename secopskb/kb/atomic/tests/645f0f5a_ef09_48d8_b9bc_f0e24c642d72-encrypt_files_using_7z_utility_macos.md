---
atomic_guid: "645f0f5a-ef09-48d8-b9bc-f0e24c642d72"
title: "Encrypt files using 7z utility - macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1486"
attack_technique_name: "Data Encrypted for Impact"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "645f0f5a-ef09-48d8-b9bc-f0e24c642d72"
  - "Encrypt files using 7z utility - macOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Encrypt files using 7z utility - macOS

This test encrypts the file(s) using the 7z utility

## Metadata

- Atomic GUID: 645f0f5a-ef09-48d8-b9bc-f0e24c642d72
- Technique: T1486: Data Encrypted for Impact
- Platforms: macos
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1486/T1486.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]

## Input Arguments

### encrypted_file_name

- description: Name of the archive to be created
- type: string
- default: ARTArchive.7z

### file_password

- description: Password to be provided for archiving the file
- type: string
- default: ARTPass

### input_file_path

- description: Path to the file that you want to encrypt
- type: path
- default: ~/test.txt

## Dependencies

Check if 7z command exists on the machine

### Prerequisite Check

```text
which 7z
```

### Get Prerequisite

```text
echo Installing 7z, using brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install p7zip
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
7z a -p #{file_password} -mhe=on #{encrypted_file_name} #{input_file_path}
```

### Cleanup

```sh
rm #{encrypted_file_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml)
