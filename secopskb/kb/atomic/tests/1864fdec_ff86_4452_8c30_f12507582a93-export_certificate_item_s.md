---
atomic_guid: "1864fdec-ff86-4452-8c30-f12507582a93"
title: "Export Certificate Item(s)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.001"
attack_technique_name: "Credentials from Password Stores: Keychain"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.001/T1555.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "1864fdec-ff86-4452-8c30-f12507582a93"
  - "Export Certificate Item(s)"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Export Certificate Item(s)

This command finds all certificate items and sends the output to local file in pem format.

## Metadata

- Atomic GUID: 1864fdec-ff86-4452-8c30-f12507582a93
- Technique: T1555.001: Credentials from Password Stores: Keychain
- Platforms: macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1555.001/T1555.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.001]]

## Input Arguments

### cert_export

- description: Specify the path of the certificates to export.
- type: path
- default: /tmp/certs.pem

## Executor

- elevation_required: False
- name: sh

### Command

```bash
security find-certificate -a -p > #{cert_export}
```

### Cleanup

```bash
rm #{cert_export}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.001/T1555.001.yaml)
