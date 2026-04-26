---
atomic_guid: "9c096ec4-fd42-419d-a762-d64cc950627e"
title: "Install root CA on CentOS/RHEL"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.004"
attack_technique_name: "Subvert Trust Controls: Install Root Certificate"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "9c096ec4-fd42-419d-a762-d64cc950627e"
  - "Install root CA on CentOS/RHEL"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Install root CA on CentOS/RHEL

Creates a root CA with openssl

## Metadata

- Atomic GUID: 9c096ec4-fd42-419d-a762-d64cc950627e
- Technique: T1553.004: Subvert Trust Controls: Install Root Certificate
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1553.004/T1553.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Input Arguments

### cert_filename

- description: Path of the CA certificate we create
- type: path
- default: rootCA.crt

### key_filename

- description: Key we create that is used to create the CA certificate
- type: path
- default: rootCA.key

## Executor

- elevation_required: True
- name: sh

### Command

```bash
openssl genrsa -out #{key_filename} 4096
openssl req -x509 -new -nodes -key #{key_filename} -sha256 -days 365 -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=www.example.com" -out #{cert_filename}
cp #{cert_filename} /etc/pki/ca-trust/source/anchors/
update-ca-trust
```

### Cleanup

```bash
rm /etc/pki/ca-trust/source/anchors/#{cert_filename}
update-ca-trust
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml)
