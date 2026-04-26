---
sigma_id: "d3b70aad-097e-409c-9df2-450f80dc476b"
title: "PUA - DIT Snapshot Viewer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_ditsnap.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_ditsnap.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d3b70aad-097e-409c-9df2-450f80dc476b"
  - "PUA - DIT Snapshot Viewer"
attack_technique_ids:
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - DIT Snapshot Viewer

Detects the use of Ditsnap tool, an inspection tool for Active Directory database, ntds.dit.

## Metadata

- Rule ID: d3b70aad-097e-409c-9df2-450f80dc476b
- Status: test
- Level: high
- Author: Furkan Caliskan (@caliskanfurkan_)
- Date: 2020-07-04
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_pua_ditsnap.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection:
- Image|endswith: \ditsnap.exe
- CommandLine|contains: ditsnap.exe
condition: selection
```

## False Positives

- Legitimate admin usage

## References

- https://thedfirreport.com/2020/06/21/snatch-ransomware/
- https://web.archive.org/web/20201124182207/https://github.com/yosqueoy/ditsnap

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_ditsnap.yml)
