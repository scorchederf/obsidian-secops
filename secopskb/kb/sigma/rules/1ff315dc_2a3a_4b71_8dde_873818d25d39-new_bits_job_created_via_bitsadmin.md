---
sigma_id: "1ff315dc-2a3a-4b71-8dde-873818d25d39"
title: "New BITS Job Created Via Bitsadmin"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/bits_client/win_bits_client_new_job_via_bitsadmin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_job_via_bitsadmin.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "windows / bits-client"
aliases:
  - "1ff315dc-2a3a-4b71-8dde-873818d25d39"
  - "New BITS Job Created Via Bitsadmin"
attack_technique_ids:
  - "T1197"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New BITS Job Created Via Bitsadmin

Detects the creation of a new bits job by Bitsadmin

## Metadata

- Rule ID: 1ff315dc-2a3a-4b71-8dde-873818d25d39
- Status: test
- Level: low
- Author: frack113
- Date: 2022-03-01
- Modified: 2023-03-27
- Source Path: rules/windows/builtin/bits_client/win_bits_client_new_job_via_bitsadmin.yml

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
  processPath|endswith: \bitsadmin.exe
condition: selection
```

## False Positives

- Many legitimate applications or scripts could leverage "bitsadmin". This event is best correlated with EID 16403 via the JobID field

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1197/T1197.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_job_via_bitsadmin.yml)
