---
atomic_guid: "f4568003-1438-44ab-a234-b3252ea7e7a3"
title: "Install root CA on FreeBSD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.004"
attack_technique_name: "Subvert Trust Controls: Install Root Certificate"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "f4568003-1438-44ab-a234-b3252ea7e7a3"
  - "Install root CA on FreeBSD"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Install root CA on FreeBSD

Creates a root CA with openssl

## Metadata

- Atomic GUID: f4568003-1438-44ab-a234-b3252ea7e7a3
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

```sh
openssl genrsa -out #{key_filename} 4096
openssl req -x509 -new -nodes -key #{key_filename} -sha256 -days 365 -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=www.example.com" -out #{cert_filename}
cp #{cert_filename} /usr/local/share/certs/
certctl rehash
```

### Cleanup

```sh
rm /usr/local/share/certs/#{cert_filename}
certctl rehash
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml)
