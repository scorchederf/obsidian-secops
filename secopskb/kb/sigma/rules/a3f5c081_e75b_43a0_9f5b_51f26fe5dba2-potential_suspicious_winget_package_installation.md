---
sigma_id: "a3f5c081-e75b-43a0-9f5b-51f26fe5dba2"
title: "Potential Suspicious Winget Package Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_stream_hash/create_stream_hash_winget_susp_package_source.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_winget_susp_package_source.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / create_stream_hash"
aliases:
  - "a3f5c081-e75b-43a0-9f5b-51f26fe5dba2"
  - "Potential Suspicious Winget Package Installation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential suspicious winget package installation from a suspicious source.

## Logsource

- category: create_stream_hash
- product: windows

## Detection

```yaml
selection:
  Contents|startswith: '[ZoneTransfer]  ZoneId=3'
  Contents|contains:
  - ://1
  - ://2
  - ://3
  - ://4
  - ://5
  - ://6
  - ://7
  - ://8
  - ://9
  TargetFilename|endswith: :Zone.Identifier
  TargetFilename|contains: \AppData\Local\Temp\WinGet\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/nasbench/Misc-Research/tree/b9596e8109dcdb16ec353f316678927e507a5b8d/LOLBINs/Winget

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_winget_susp_package_source.yml)
