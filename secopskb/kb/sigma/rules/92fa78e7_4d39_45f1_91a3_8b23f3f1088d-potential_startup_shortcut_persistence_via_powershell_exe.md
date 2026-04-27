---
sigma_id: "92fa78e7-4d39-45f1-91a3-8b23f3f1088d"
title: "Potential Startup Shortcut Persistence Via PowerShell.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_powershell_startup_shortcuts.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_startup_shortcuts.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "92fa78e7-4d39-45f1-91a3-8b23f3f1088d"
  - "Potential Startup Shortcut Persistence Via PowerShell.EXE"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects PowerShell writing startup shortcuts.
This procedure was highlighted in Red Canary Intel Insights Oct. 2021, "We frequently observe adversaries using PowerShell to write malicious .lnk files into the startup directory to establish persistence.
Accordingly, this detection opportunity is likely to identify persistence mechanisms in multiple threats.
In the context of Yellow Cockatoo, this persistence mechanism eventually launches the command-line script that leads to the installation of a malicious DLL"

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]

## Detection

```yaml
selection:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  TargetFilename|contains: \start menu\programs\startup\
  TargetFilename|endswith: .lnk
condition: selection
```

## False Positives

- Depending on your environment accepted applications may leverage this at times. It is recommended to search for anomalies inidicative of malware.

## References

- https://redcanary.com/blog/intelligence-insights-october-2021/
- https://github.com/redcanaryco/atomic-red-team/blob/36d49de4c8b00bf36054294b4a1fcbab3917d7c5/atomics/T1547.001/T1547.001.md#atomic-test-7---add-executable-shortcut-link-to-user-startup-folder

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_startup_shortcuts.yml)
