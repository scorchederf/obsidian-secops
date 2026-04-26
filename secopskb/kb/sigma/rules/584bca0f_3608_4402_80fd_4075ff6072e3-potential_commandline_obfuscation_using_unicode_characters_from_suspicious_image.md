---
sigma_id: "584bca0f-3608-4402-80fd-4075ff6072e3"
title: "Potential CommandLine Obfuscation Using Unicode Characters From Suspicious Image"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_cli_obfuscation_unicode_img.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_cli_obfuscation_unicode_img.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "584bca0f-3608-4402-80fd-4075ff6072e3"
  - "Potential CommandLine Obfuscation Using Unicode Characters From Suspicious Image"
attack_technique_ids:
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential CommandLine Obfuscation Using Unicode Characters From Suspicious Image

Detects potential commandline obfuscation using unicode characters.
Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the system or in transit.

## Metadata

- Rule ID: 584bca0f-3608-4402-80fd-4075ff6072e3
- Status: test
- Level: high
- Author: frack113, Florian Roth (Nextron Systems), Josh Nickels
- Date: 2024-09-02
- Modified: 2025-05-30
- Source Path: rules/windows/process_creation/proc_creation_win_susp_cli_obfuscation_unicode_img.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \powershell.exe
  - \powershell_ise.exe
  - \pwsh.exe
  - \wscript.exe
  OriginalFileName:
  - Cmd.EXE
  - cscript.exe
  - PowerShell.EXE
  - PowerShell_ISE.EXE
  - pwsh.dll
  - wscript.exe
selection_special_chars:
  CommandLine|contains:
  - ˣ
  - ˪
  - ˢ
  - ∕
  - ⁄
  - ―
  - —
  -  
  - ¯
  - ®
  - ¶
  - ⠀
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.wietzebeukema.nl/blog/windows-command-line-obfuscation
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1027/T1027.md#atomic-test-6---dlp-evasion-via-sensitive-data-in-vba-macro-over-http

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_cli_obfuscation_unicode_img.yml)
