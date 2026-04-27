---
atomic_guid: "c01cad7f-7a4c-49df-985e-b190dcf6a279"
title: "iwr or Invoke Web-Request download"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "c01cad7f-7a4c-49df-985e-b190dcf6a279"
  - "iwr or Invoke Web-Request download"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use 'iwr' or "Invoke-WebRequest" -URI argument to download a file from the web. Note: without -URI also works in some versions.

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Input Arguments

### local_path

- description: Local path to place file
- type: path
- default: %temp%\Atomic-license.txt

### remote_file

- description: URL of file to copy
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/LICENSE.txt

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
powershell.exe iwr -URI #{remote_file} -Outfile #{local_path}
```

### Cleanup

```cmd
del %temp%\Atomic-license.txt >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
