---
atomic_guid: "41410c60-614d-4b9d-b66e-b0192dd9c597"
title: "Compress Data for Exfiltration With PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560"
attack_technique_name: "Archive Collected Data"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560/T1560.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "41410c60-614d-4b9d-b66e-b0192dd9c597"
  - "Compress Data for Exfiltration With PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may compress data (e.g., sensitive documents) that is collected prior to exfiltration.
When the test completes you should find the files from the $env:USERPROFILE directory compressed in a file called T1560-data-ps.zip in the $env:USERPROFILE directory

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data|T1560: Archive Collected Data]]

## Input Arguments

### input_file

- description: Path that should be compressed into our output file
- type: path
- default: $env:USERPROFILE

### output_file

- description: Path where resulting compressed data should be placed
- type: path
- default: $env:USERPROFILE\T1560-data-ps.zip

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
dir #{input_file} -Recurse | Compress-Archive -DestinationPath #{output_file}
```

### Cleanup

```powershell
Remove-Item -path #{output_file} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560/T1560.yaml)
