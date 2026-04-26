---
atomic_guid: "c2ca068a-eb1e-498f-9f93-3d554c455916"
title: "Password-Protected ZIP Payload Extraction and Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.013"
attack_technique_name: "Obfuscated Files or Information: Encrypted/Encoded File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.013/T1027.013.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "c2ca068a-eb1e-498f-9f93-3d554c455916"
  - "Password-Protected ZIP Payload Extraction and Execution"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password-Protected ZIP Payload Extraction and Execution

Extracts and executes a script from a password-protected ZIP archive.
This technique is commonly used by malware families like Emotet and QBot to deliver payloads
via email attachments where the password is provided in the message body.
The encrypted ZIP evades static file analysis until extracted at runtime.
Upon successful execution, displays confirmation and system information.

## Metadata

- Atomic GUID: c2ca068a-eb1e-498f-9f93-3d554c455916
- Technique: T1027.013: Obfuscated Files or Information: Encrypted/Encoded File
- Platforms: linux, macos
- Executor: bash
- Dependency Executor: bash
- Source Path: atomics/T1027.013/T1027.013.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.013]]

## Input Arguments

### zip_password

- description: Password used to protect the ZIP archive
- type: String
- default: infected

## Dependencies

zip and unzip must be installed

### Prerequisite Check

```text
which zip && which unzip
```

### Get Prerequisite

```text
echo "Install zip and unzip using your package manager (apt-get, yum, or brew)"
```

## Executor

- name: bash

### Command

```bash
echo '#!/bin/bash' > /tmp/art_payload.sh
echo 'echo "T1027.013: Payload extracted from encrypted ZIP"' >> /tmp/art_payload.sh
echo 'echo "Hostname: $(hostname)"' >> /tmp/art_payload.sh
echo 'echo "User: $(whoami)"' >> /tmp/art_payload.sh
echo 'uname -a' >> /tmp/art_payload.sh
cd /tmp && zip -P "#{zip_password}" art_encrypted.zip art_payload.sh
rm /tmp/art_payload.sh
echo "Encrypted ZIP created. Extracting with password..."
unzip -P "#{zip_password}" -o /tmp/art_encrypted.zip -d /tmp/
echo "Executing extracted payload:"
bash /tmp/art_payload.sh
```

### Cleanup

```bash
rm -f /tmp/art_payload.sh
rm -f /tmp/art_encrypted.zip
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.013/T1027.013.yaml)
