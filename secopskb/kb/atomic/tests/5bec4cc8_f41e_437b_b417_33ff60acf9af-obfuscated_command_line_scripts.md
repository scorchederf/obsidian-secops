---
atomic_guid: "5bec4cc8-f41e-437b-b417-33ff60acf9af"
title: "Obfuscated command line scripts"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "5bec4cc8-f41e-437b-b417-33ff60acf9af"
  - "Obfuscated command line scripts"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Obfuscated command line scripts

An adversary may pre-compute the base64 representations of the terminal commands that they wish to execute in an attempt to avoid or frustrate detection. The following commands base64 encodes the text string id, then base64 decodes the string, then pipes it as a command to bash, which results in the id command being executed.

## Metadata

- Atomic GUID: 5bec4cc8-f41e-437b-b417-33ff60acf9af
- Technique: T1059.004: Command and Scripting Interpreter: Bash
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1059.004/T1059.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
[ "$(uname)" = 'FreeBSD' ] && encodecmd="b64encode -r -" && decodecmd="b64decode -r" || encodecmd="base64 -w 0" && decodecmd="base64 -d"
ART=$(echo -n "id" | $encodecmd)
echo "\$ART=$ART"
echo -n "$ART" | $decodecmd |/bin/bash
unset ART
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
