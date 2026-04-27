---
atomic_guid: "e544bbcb-c4e0-4bd0-b614-b92131635f59"
title: "Import Certificate Item(s) into Keychain"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.001"
attack_technique_name: "Credentials from Password Stores: Keychain"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.001/T1555.001.yaml"
build_date: "2026-04-27 19:12:28"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This command will import a certificate pem file into a keychain.

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores#^t1555001-keychain|T1555.001: Keychain]]

## Input Arguments

### cert_export

- description: Specify the path of the pem certificate file to import.
- type: path
- default: /tmp/certs.pem

## Executor

- elevation_required: False
- name: sh

### Command

```bash
security import #{cert_export} -k
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.001/T1555.001.yaml)
