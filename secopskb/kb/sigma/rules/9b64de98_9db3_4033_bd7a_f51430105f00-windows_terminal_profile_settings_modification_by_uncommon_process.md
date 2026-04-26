---
sigma_id: "9b64de98-9db3-4033-bd7a-f51430105f00"
title: "Windows Terminal Profile Settings Modification By Uncommon Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_windows_terminal_profile.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_windows_terminal_profile.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "9b64de98-9db3-4033-bd7a-f51430105f00"
  - "Windows Terminal Profile Settings Modification By Uncommon Process"
attack_technique_ids:
  - "T1547.015"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Terminal Profile Settings Modification By Uncommon Process

Detects the creation or modification of the Windows Terminal Profile settings file "settings.json" by an uncommon process.

## Metadata

- Rule ID: 9b64de98-9db3-4033-bd7a-f51430105f00
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-22
- Source Path: rules/windows/file/file_event/file_event_win_susp_windows_terminal_profile.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.015]]

## Detection

```yaml
selection:
  Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \wscript.exe
  TargetFilename|endswith: \AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
condition: selection
```

## False Positives

- Some false positives may occur with admin scripts that set WT settings.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/74438b0237d141ee9c99747976447dc884cb1a39/atomics/T1547.015/T1547.015.md#atomic-test-1---persistence-by-modifying-windows-terminal-profile
- https://twitter.com/nas_bench/status/1550836225652686848

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_windows_terminal_profile.yml)
