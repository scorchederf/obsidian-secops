---
sigma_id: "d3b70aad-097e-409c-9df2-450f80dc476b"
title: "PUA - DIT Snapshot Viewer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_ditsnap.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_ditsnap.yml"
build_date: "2026-04-27 19:13:53"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of Ditsnap tool, an inspection tool for Active Directory database, ntds.dit.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

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
