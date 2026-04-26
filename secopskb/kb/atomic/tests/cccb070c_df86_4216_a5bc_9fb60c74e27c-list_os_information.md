---
atomic_guid: "cccb070c-df86-4216-a5bc-9fb60c74e27c"
title: "List OS Information"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "cccb070c-df86-4216-a5bc-9fb60c74e27c"
  - "List OS Information"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# List OS Information

Identify System Info

## Metadata

- Atomic GUID: cccb070c-df86-4216-a5bc-9fb60c74e27c
- Technique: T1082: System Information Discovery
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Input Arguments

### output_file

- description: Output file used to store the results.
- type: path
- default: /tmp/T1082.txt

## Executor

- name: sh

### Command

```bash
uname -a >> #{output_file}
if [ -f /etc/lsb-release ]; then cat /etc/lsb-release >> #{output_file}; fi
if [ -f /etc/redhat-release ]; then cat /etc/redhat-release >> #{output_file}; fi   
if [ -f /etc/issue ]; then cat /etc/issue >> #{output_file}; fi
if [ -f /etc/os-release ]; then cat /etc/os-release >> #{output_file}; fi
uptime >> #{output_file}
cat #{output_file} 2>/dev/null
```

### Cleanup

```bash
rm #{output_file} 2>/dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
