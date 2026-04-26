---
sigma_id: "fe3a2d49-f255-4d10-935c-bda7391108eb"
title: "New BITS Job Created Via PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/bits_client/win_bits_client_new_job_via_powershell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_job_via_powershell.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "windows / bits-client"
aliases:
  - "fe3a2d49-f255-4d10-935c-bda7391108eb"
  - "New BITS Job Created Via PowerShell"
attack_technique_ids:
  - "T1197"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New BITS Job Created Via PowerShell

Detects the creation of a new bits job by PowerShell

## Metadata

- Rule ID: fe3a2d49-f255-4d10-935c-bda7391108eb
- Status: test
- Level: low
- Author: frack113
- Date: 2022-03-01
- Modified: 2023-03-27
- Source Path: rules/windows/builtin/bits_client/win_bits_client_new_job_via_powershell.yml

## Logsource

- product: windows
- service: bits-client

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]

## Detection

```yaml
selection:
  EventID: 3
  processPath|endswith:
  - \powershell.exe
  - \pwsh.exe
condition: selection
```

## False Positives

- Administrator PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1197/T1197.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_job_via_powershell.yml)
