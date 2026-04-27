---
sigma_id: "f8a56cb7-a363-44ed-a82f-5926bb44cd05"
title: "BITS Transfer Job Download To Potential Suspicious Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/bits_client/win_bits_client_new_trasnfer_susp_local_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_trasnfer_susp_local_folder.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / bits-client"
aliases:
  - "f8a56cb7-a363-44ed-a82f-5926bb44cd05"
  - "BITS Transfer Job Download To Potential Suspicious Folder"
attack_technique_ids:
  - "T1197"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects new BITS transfer job where the LocalName/Saved file is stored in a potentially suspicious location

## Logsource

- product: windows
- service: bits-client

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1197-bits_jobs|T1197: BITS Jobs]]

## Detection

```yaml
selection:
  EventID: 16403
  LocalName|contains:
  - \Desktop\
  - C:\Users\Public\
  - C:\PerfLogs\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1197/T1197.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_trasnfer_susp_local_folder.yml)
