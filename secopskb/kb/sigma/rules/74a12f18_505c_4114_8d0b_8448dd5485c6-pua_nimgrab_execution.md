---
sigma_id: "74a12f18-505c-4114-8d0b-8448dd5485c6"
title: "PUA - Nimgrab Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_nimgrab.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nimgrab.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "74a12f18-505c-4114-8d0b-8448dd5485c6"
  - "PUA - Nimgrab Execution"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the usage of nimgrab, a tool bundled with the Nim programming framework and used for downloading files.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detection

```yaml
selection_name:
  Image|endswith: \nimgrab.exe
selection_hashes:
  Hashes|contains:
  - MD5=2DD44C3C29D667F5C0EF5F9D7C7FFB8B
  - SHA256=F266609E91985F0FE3E31C5E8FAEEEC4FFA5E0322D8B6F15FE69F4C5165B9559
  - IMPHASH=C07FDDD21D123EA9B3A08EEF44AAAC45
condition: 1 of selection_*
```

## False Positives

- Legitimate use of Nim on a developer systems

## References

- https://github.com/redcanaryco/atomic-red-team/blob/28d190330fe44de6ff4767fc400cc10fa7cd6540/atomics/T1105/T1105.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nimgrab.yml)
