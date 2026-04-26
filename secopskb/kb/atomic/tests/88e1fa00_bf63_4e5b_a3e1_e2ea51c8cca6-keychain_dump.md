---
atomic_guid: "88e1fa00-bf63-4e5b-a3e1-e2ea51c8cca6"
title: "Keychain Dump"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.001"
attack_technique_name: "Credentials from Password Stores: Keychain"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.001/T1555.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "88e1fa00-bf63-4e5b-a3e1-e2ea51c8cca6"
  - "Keychain Dump"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Keychain Dump

This command will dump keychain credential information from login.keychain. 
Source: https://www.loobins.io/binaries/security/

### Keychain File path
  ~/Library/Keychains/
  /Library/Keychains/
  /Network/Library/Keychains/
  [Security Reference](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/security.1.html)

## Metadata

- Atomic GUID: 88e1fa00-bf63-4e5b-a3e1-e2ea51c8cca6
- Technique: T1555.001: Credentials from Password Stores: Keychain
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1555.001/T1555.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.001]]

## Executor

- elevation_required: True
- name: sh

### Command

```sh
sudo security dump-keychain -d login.keychain
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.001/T1555.001.yaml)
