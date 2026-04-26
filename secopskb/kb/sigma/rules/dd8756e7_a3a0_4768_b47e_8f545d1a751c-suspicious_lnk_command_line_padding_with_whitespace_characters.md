---
sigma_id: "dd8756e7-a3a0-4768-b47e-8f545d1a751c"
title: "Suspicious LNK Command-Line Padding with Whitespace Characters"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_lnk_exec_hidden_cmd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_lnk_exec_hidden_cmd.yml"
build_date: "2026-04-26 17:03:23"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "dd8756e7-a3a0-4768-b47e-8f545d1a751c"
  - "Suspicious LNK Command-Line Padding with Whitespace Characters"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious LNK Command-Line Padding with Whitespace Characters

Detects exploitation of LNK file command-line length discrepancy, where attackers hide malicious commands beyond the 260-character UI limit while the actual command-line argument field supports 4096 characters using whitespace padding (e.g., 0x20, 0x09-0x0D).
Adversaries insert non-printable whitespace characters (e.g., Line Feed \x0A, Carriage Return \x0D) to pad the visible section of the LNK file, pushing malicious commands past the UI-visible boundary.
The hidden payload, executed at runtime but invisible in Windows Explorer properties, enables stealthy execution and evasion—commonly used for social engineering attacks.
This rule flags suspicious use of such padding observed in real-world attacks.

## Metadata

- Rule ID: dd8756e7-a3a0-4768-b47e-8f545d1a751c
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-03-19
- Source Path: rules/windows/process_creation/proc_creation_win_susp_lnk_exec_hidden_cmd.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Detection

```yaml
selection_img:
- ParentImage|endswith: \explorer.exe
- ParentCommandLine|contains: .lnk
selection_cmd:
- CommandLine|contains:
  - '                 '
  - \u0009
  - \u000A
  - \u0011
  - \u0012
  - \u0013
  - \u000B
  - \u000C
  - \u000D
- CommandLine|re: \n\n\n\n\n\n
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://syedhasan010.medium.com/forensics-analysis-of-an-lnk-file-da68a98b8415
- https://thehackernews.com/2025/03/unpatched-windows-zero-day-flaw.html
- https://www.trendmicro.com/en_us/research/25/c/windows-shortcut-zero-day-exploit.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_lnk_exec_hidden_cmd.yml)
