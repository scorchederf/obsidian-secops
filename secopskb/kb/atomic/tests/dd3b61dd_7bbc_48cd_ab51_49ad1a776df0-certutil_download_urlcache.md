---
atomic_guid: "dd3b61dd-7bbc-48cd-ab51-49ad1a776df0"
title: "certutil download (urlcache)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "dd3b61dd-7bbc-48cd-ab51-49ad1a776df0"
  - "certutil download (urlcache)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# certutil download (urlcache)

Use certutil -urlcache argument to download a file from the web. Note - /urlcache also works!

## Metadata

- Atomic GUID: dd3b61dd-7bbc-48cd-ab51-49ad1a776df0
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### local_path

- description: Local path to place file
- type: path
- default: Atomic-license.txt

### remote_file

- description: URL of file to copy
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/LICENSE.txt

## Executor

- name: command_prompt

### Command

```cmd
cmd /c certutil -urlcache -split -f #{remote_file} #{local_path}
```

### Cleanup

```cmd
del #{local_path} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
