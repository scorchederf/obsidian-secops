---
atomic_guid: "cc99e772-4e18-4f1f-b422-c5cdd1bfd7b7"
title: "Azure - Dump Azure Instance Metadata from Virtual Machines"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.005"
attack_technique_name: "Unsecured Credentials: Cloud Instance Metadata API"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.005/T1552.005.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "cc99e772-4e18-4f1f-b422-c5cdd1bfd7b7"
  - "Azure - Dump Azure Instance Metadata from Virtual Machines"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Azure - Dump Azure Instance Metadata from Virtual Machines

This test invokes a web request to the default Instance Metadata API of 169.254.169.254 in order to dump the data contained within it to a file. 
See: https://www.sans.org/blog/cloud-instance-metadata-services-imds-/

## Metadata

- Atomic GUID: cc99e772-4e18-4f1f-b422-c5cdd1bfd7b7
- Technique: T1552.005: Unsecured Credentials: Cloud Instance Metadata API
- Platforms: iaas:azure
- Executor: powershell
- Source Path: atomics/T1552.005/T1552.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.005]]

## Input Arguments

### output_file

- description: File to output metadata to
- type: string
- default: $env:temp\T1552.005Test2.txt

## Executor

- name: powershell

### Command

```powershell
Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -Uri "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | ConvertTo-Json -Depth 64 > #{output_file}
```

### Cleanup

```powershell
remove-item #{output_file} -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.005/T1552.005.yaml)
