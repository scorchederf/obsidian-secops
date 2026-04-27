---
atomic_guid: "c3b65cd5-ee51-4e98-b6a3-6cbdec138efc"
title: "XOR decoding and command execution using Python"
framework: "atomic"
generated: "true"
attack_technique_id: "T1140"
attack_technique_name: "Deobfuscate/Decode Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml"
build_date: "2026-04-27 19:12:27"
executor: "bash"
aliases:
  - "c3b65cd5-ee51-4e98-b6a3-6cbdec138efc"
  - "XOR decoding and command execution using Python"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary can obfuscate malicious commands or payloads using XOR and execute them on the victim's machine. This test uses Python to decode and execute commands on the machine.

## ATT&CK Mapping

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]

## Input Arguments

### encrypted_command

- description: Encrypted command that will be executed
- type: string
- default: AAkqKQEM

### xor_key

- description: Key used to decrypt the command 
- type: string
- default: waEHleblxiQjoxFJQaIMLdHKz

## Dependencies

Python3 must be installed

### Prerequisite Check

```bash
which python3
```

### Get Prerequisite

```bash
echo "Install Python3"
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
python3 -c 'import base64; import subprocess; xor_decrypt = lambda text, key: "".join([chr(c ^ ord(k)) for c, k in zip(base64.b64decode(text.encode()), key)]); command = "#{encrypted_command}"; key = "#{xor_key}"; exec = xor_decrypt(command, key); subprocess.call(exec, shell=True)'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml)
