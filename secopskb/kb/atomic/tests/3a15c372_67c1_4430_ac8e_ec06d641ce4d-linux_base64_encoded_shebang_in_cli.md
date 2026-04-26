---
atomic_guid: "3a15c372-67c1-4430-ac8e-ec06d641ce4d"
title: "Linux Base64 Encoded Shebang in CLI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1140"
attack_technique_name: "Deobfuscate/Decode Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "3a15c372-67c1-4430-ac8e-ec06d641ce4d"
  - "Linux Base64 Encoded Shebang in CLI"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Linux Base64 Encoded Shebang in CLI

Using Linux Base64 Encoded shell scripts that have Shebang in them. This is commonly how attackers obfuscate passing and executing a shell script. Seen [here](https://www.trendmicro.com/pl_pl/research/20/i/the-evolution-of-malicious-shell-scripts.html) by TrendMicro, as well as [LinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS). Also a there is a great Sigma rule [here](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_base64_shebang_cli.yml) for it.

## Metadata

- Atomic GUID: 3a15c372-67c1-4430-ac8e-ec06d641ce4d
- Technique: T1140: Deobfuscate/Decode Files or Information
- Platforms: linux, macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1140/T1140.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]

## Input Arguments

### bash_encoded

- description: Encoded
- type: string
- default: IyEvYmluL2Jhc2gKZWNobyAiaHR0cHM6Ly93d3cueW91dHViZS5jb20vQGF0b21pY3NvbmFmcmlkYXkgRlRXIgo=

### dash_encoded

- description: Encoded
- type: string
- default: IyEvYmluL2Rhc2gKZWNobyAiaHR0cHM6Ly93d3cueW91dHViZS5jb20vQGF0b21pY3NvbmFmcmlkYXkgRlRXIgo=

### fish_encoded

- description: Encoded
- type: string
- default: IyEvYmluL2Rhc2gKZWNobyAiaHR0cHM6Ly93d3cueW91dHViZS5jb20vQGF0b21pY3NvbmFmcmlkYXkgRlRXIgo=

### sh_encoded

- description: Encoded
- type: string
- default: IyEvYmluL3NoCmVjaG8gImh0dHBzOi8vd3d3LnlvdXR1YmUuY29tL0BhdG9taWNzb25hZnJpZGF5IEZUVyIK

## Dependencies

base64 must be present

### Prerequisite Check

```text
which base64
```

### Get Prerequisite

```text
echo "please install base64"
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
echo #{bash_encoded} | base64 -d | bash
echo #{dash_encoded} | base64 -d | bash
echo #{fish_encoded} | base64 -d | bash
echo #{sh_encoded} | base64 -d | bash
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml)
