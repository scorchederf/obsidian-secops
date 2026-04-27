---
atomic_guid: "5c32102a-c508-49d3-978f-288f8a9f6617"
title: "Copy Keychain using cat utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.001"
attack_technique_name: "Credentials from Password Stores: Keychain"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.001/T1555.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "5c32102a-c508-49d3-978f-288f8a9f6617"
  - "Copy Keychain using cat utility"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This command will copy the keychain using the cat utility in a manner similar to Atomic Stealer.

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores#^t1555001-keychain|T1555.001: Keychain]]

## Input Arguments

### keychain_export

- description: Specify the path to copy they keychain into.
- type: path
- default: /tmp/keychain

## Executor

- elevation_required: False
- name: sh

### Command

```bash
cat ~/Library/Keychains/login.keychain-db > #{keychain_export}
```

### Cleanup

```bash
rm #{keychain_export}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.001/T1555.001.yaml)
