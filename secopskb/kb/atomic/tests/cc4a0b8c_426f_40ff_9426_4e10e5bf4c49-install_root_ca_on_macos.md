---
atomic_guid: "cc4a0b8c-426f-40ff-9426-4e10e5bf4c49"
title: "Install root CA on macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.004"
attack_technique_name: "Subvert Trust Controls: Install Root Certificate"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "cc4a0b8c-426f-40ff-9426-4e10e5bf4c49"
  - "Install root CA on macOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Install root CA on macOS

Creates a root CA with openssl

## Metadata

- Atomic GUID: cc4a0b8c-426f-40ff-9426-4e10e5bf4c49
- Technique: T1553.004: Subvert Trust Controls: Install Root Certificate
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1553.004/T1553.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Input Arguments

### cert_filename

- description: CA file name
- type: path
- default: rootCA.crt

### key_filename

- description: Key we create that is used to create the CA certificate
- type: path
- default: rootCA.key

## Dependencies

Verify the certificate exists. It generates if not on disk.

### Prerequisite Check

```bash
if [ -f #{cert_filename} ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
if [ ! -f #{key_filename} ]; then openssl genrsa -out #{key_filename} 4096; fi;
openssl req -x509 -new -nodes -key #{key_filename} -sha256 -days 365 -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=www.example.com" -out #{cert_filename}
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo security add-trusted-cert -d -r trustRoot -k "/Library/Keychains/System.keychain" "#{cert_filename}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml)
