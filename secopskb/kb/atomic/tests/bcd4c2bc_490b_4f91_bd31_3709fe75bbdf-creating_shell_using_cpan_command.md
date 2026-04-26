---
atomic_guid: "bcd4c2bc-490b-4f91-bd31-3709fe75bbdf"
title: "Creating shell using cpan command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "bcd4c2bc-490b-4f91-bd31-3709fe75bbdf"
  - "Creating shell using cpan command"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Creating shell using cpan command

cpan lets you execute perl commands with the ! command. It can be used to break out from restricted environments by spawning an interactive system shell.
Reference - https://gtfobins.github.io/gtfobins/cpan/

## Metadata

- Atomic GUID: bcd4c2bc-490b-4f91-bd31-3709fe75bbdf
- Technique: T1059.004: Command and Scripting Interpreter: Bash
- Platforms: linux, macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1059.004/T1059.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Executor

- elevation_required: False
- name: sh

### Command

```sh
echo '! exec "/bin/sh &"' | PERL_MM_USE_DEFAULT=1  cpan
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
