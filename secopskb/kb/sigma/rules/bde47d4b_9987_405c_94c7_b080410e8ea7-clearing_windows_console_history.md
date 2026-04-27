---
sigma_id: "bde47d4b-9987-405c-94c7-b080410e8ea7"
title: "Clearing Windows Console History"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_clearing_windows_console_history.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_clearing_windows_console_history.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "bde47d4b-9987-405c-94c7-b080410e8ea7"
  - "Clearing Windows Console History"
attack_technique_ids:
  - "T1070"
  - "T1070.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Clearing Windows Console History

Identifies when a user attempts to clear console history. An adversary may clear the command history of a compromised account to conceal the actions undertaken during an intrusion.

## Metadata

- Rule ID: bde47d4b-9987-405c-94c7-b080410e8ea7
- Status: test
- Level: high
- Author: Austin Songer @austinsonger
- Date: 2021-11-25
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_clearing_windows_console_history.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]
- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Detection

```yaml
selection1:
  ScriptBlockText|contains: Clear-History
selection2a:
  ScriptBlockText|contains:
  - Remove-Item
  - rm
selection2b:
  ScriptBlockText|contains:
  - ConsoleHost_history.txt
  - (Get-PSReadlineOption).HistorySavePath
condition: selection1 or selection2a and selection2b
```

## False Positives

- Unknown

## References

- https://stefanos.cloud/blog/kb/how-to-clear-the-powershell-command-history/
- https://www.shellhacks.com/clear-history-powershell/
- https://community.sophos.com/sophos-labs/b/blog/posts/powershell-command-history-forensics

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_clearing_windows_console_history.yml)
