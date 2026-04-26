---
sigma_id: "d08a2711-ee8b-4323-bdec-b7d85e892b31"
title: "PUA - CsExec Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_csexec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_csexec.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d08a2711-ee8b-4323-bdec-b7d85e892b31"
  - "PUA - CsExec Execution"
attack_technique_ids:
  - "T1587.001"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - CsExec Execution

Detects the use of the lesser known remote execution tool named CsExec a PsExec alternative

## Metadata

- Rule ID: d08a2711-ee8b-4323-bdec-b7d85e892b31
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-08-22
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_pua_csexec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1587-develop_capabilities|T1587.001]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection:
  Image|endswith: \csexec.exe
selection_pe:
  Description: csexec
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://github.com/malcomvetter/CSExec
- https://www.microsoft.com/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_csexec.yml)
