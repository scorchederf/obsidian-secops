---
atomic_guid: "f45df6be-2e1e-4136-a384-8f18ab3826fb"
title: "Decode base64 Data into Script"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027"
attack_technique_name: "Obfuscated Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml"
build_date: "2026-04-27 19:12:25"
executor: "sh"
aliases:
  - "f45df6be-2e1e-4136-a384-8f18ab3826fb"
  - "Decode base64 Data into Script"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a base64-encoded data file and decodes it into an executable shell script

Upon successful execution, sh will execute art.sh, which is a base64 encoded command, that echoes `Hello from the Atomic Red Team` 
and uname -v

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]

## Input Arguments

### shell_command

- description: command to encode
- type: string
- default: echo Hello from the Atomic Red Team && uname -v

## Dependencies

encode the command into base64 file

### Prerequisite Check

```bash
if [ -e "/tmp/encoded.dat" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
if [ "$(uname)" = 'FreeBSD' ]; then cmd="b64encode -r -"; else cmd="base64"; fi;
echo "#{shell_command}" | $cmd > /tmp/encoded.dat
```

## Executor

- name: sh

### Command

```bash
if [ "$(uname)" = 'FreeBSD' ]; then cmd="b64decode -r"; else cmd="base64 -d"; fi;
cat /tmp/encoded.dat | $cmd > /tmp/art.sh
chmod +x /tmp/art.sh
/tmp/art.sh
```

### Cleanup

```bash
rm /tmp/encoded.dat 
rm /tmp/art.sh
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml)
