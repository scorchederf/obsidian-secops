---
atomic_guid: "e544bbcb-c4e0-4bd0-b614-b92131635f59"
title: "Import Certificate Item(s) into Keychain"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.001"
attack_technique_name: "Credentials from Password Stores: Keychain"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.001/T1555.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "e544bbcb-c4e0-4bd0-b614-b92131635f59"
  - "Import Certificate Item(s) into Keychain"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Import Certificate Item(s) into Keychain

This command will import a certificate pem file into a keychain.

## Metadata

- Atomic GUID: e544bbcb-c4e0-4bd0-b614-b92131635f59
- Technique: T1555.001: Credentials from Password Stores: Keychain
- Platforms: macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1555.001/T1555.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.001]]

## Input Arguments

### cert_export

- description: Specify the path of the pem certificate file to import.
- type: path
- default: /tmp/certs.pem

## Executor

- elevation_required: False
- name: sh

### Command

```sh
security import #{cert_export} -k
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.001/T1555.001.yaml)
