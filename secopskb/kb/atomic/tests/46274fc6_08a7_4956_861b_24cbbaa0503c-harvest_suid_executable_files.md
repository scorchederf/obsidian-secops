---
atomic_guid: "46274fc6-08a7-4956-861b-24cbbaa0503c"
title: "Harvest SUID executable files"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "46274fc6-08a7-4956-861b-24cbbaa0503c"
  - "Harvest SUID executable files"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Harvest SUID executable files

AutoSUID application is the Open-Source project, the main idea of which is to automate harvesting the SUID executable files and to find a way for further escalating the privileges.

## Metadata

- Atomic GUID: 46274fc6-08a7-4956-861b-24cbbaa0503c
- Technique: T1059.004: Command and Scripting Interpreter: Bash
- Platforms: linux
- Executor: sh
- Dependency Executor: bash
- Source Path: atomics/T1059.004/T1059.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Input Arguments

### autosuid

- description: Path to the autosuid shell script
- type: path
- default: PathToAtomicsFolder/T1059.004/src/AutoSUID.sh

### autosuid_url

- description: Path to download autosuid shell script
- type: url
- default: https://raw.githubusercontent.com/IvanGlinkin/AutoSUID/main/AutoSUID.sh

## Dependencies

AutoSUID must exist on disk at specified location (#{autosuid})

### Prerequisite Check

```bash
if [ -f #{autosuid} ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
curl --create-dirs #{autosuid_url} --output #{autosuid}
```

## Executor

- name: sh

### Command

```bash
chmod +x #{autosuid}
bash #{autosuid}
```

### Cleanup

```bash
rm -rf #{autosuid}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
