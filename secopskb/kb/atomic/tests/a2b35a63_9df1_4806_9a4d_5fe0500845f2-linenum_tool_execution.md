---
atomic_guid: "a2b35a63-9df1-4806-9a4d-5fe0500845f2"
title: "LinEnum tool execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "a2b35a63-9df1-4806-9a4d-5fe0500845f2"
  - "LinEnum tool execution"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

LinEnum is a bash script that performs discovery commands for accounts,processes, kernel version, applications, services, and uses the information from these commands to present operator with ways of escalating privileges or further exploitation of targeted host.

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]

## Input Arguments

### linenum

- description: Path to the LinEnum shell script
- type: path
- default: PathToAtomicsFolder/T1059.004/src/LinEnum.sh

### linenum_url

- description: Path to download LinEnum shell script
- type: url
- default: https://raw.githubusercontent.com/rebootuser/LinEnum/c47f9b226d3ce2848629f25fe142c1b2986bc427/LinEnum.sh

## Dependencies

LinnEnum must exist on disk at specified location (#{linenum})

### Prerequisite Check

```bash
if [ -f #{linenum} ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
curl --create-dirs #{linenum_url} --output #{linenum}
```

## Executor

- name: sh

### Command

```bash
chmod +x #{linenum}
bash #{linenum}
```

### Cleanup

```bash
rm -rf #{linenum}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
