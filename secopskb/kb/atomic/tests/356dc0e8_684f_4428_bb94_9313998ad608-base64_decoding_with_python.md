---
atomic_guid: "356dc0e8-684f-4428-bb94-9313998ad608"
title: "Base64 decoding with Python"
framework: "atomic"
generated: "true"
attack_technique_id: "T1140"
attack_technique_name: "Deobfuscate/Decode Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "356dc0e8-684f-4428-bb94-9313998ad608"
  - "Base64 decoding with Python"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use Python to decode a base64-encoded text string and echo it to the console

## ATT&CK Mapping

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]

## Input Arguments

### encoded_file

- description: File to temporarily save encoded text
- type: path
- default: /tmp/T1140.encoded

### message

- description: Message to print to the screen
- type: string
- default: Hello from Atomic Red Team test T1140!

## Dependencies

Python must be present

### Prerequisite Check

```untitled
which python3
```

### Get Prerequisite

```untitled
echo "Please install Python 3"
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
ENCODED=$(python3 -c 'import base64;enc=base64.b64encode("#{message}".encode());print(enc.decode())')
python3 -c "import base64;dec=base64.b64decode(\"$ENCODED\");print(dec.decode())"
python3 -c "import base64 as d;dec=d.b64decode(\"$ENCODED\");print(dec.decode())"
python3 -c "from base64 import b64decode;dec=b64decode(\"$ENCODED\");print(dec.decode())"
python3 -c "from base64 import b64decode as d;dec=d(\"$ENCODED\");print(dec.decode())"
echo $ENCODED | python3 -c "import base64,sys;dec=base64.b64decode(sys.stdin.read());print(dec.decode())"
echo $ENCODED > #{encoded_file} && python3 -c "import base64;dec=base64.b64decode(open('#{encoded_file}').read());print(dec.decode())"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml)
