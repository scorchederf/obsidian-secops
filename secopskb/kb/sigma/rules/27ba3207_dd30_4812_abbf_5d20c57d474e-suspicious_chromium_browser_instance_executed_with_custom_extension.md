---
sigma_id: "27ba3207-dd30-4812-abbf-5d20c57d474e"
title: "Suspicious Chromium Browser Instance Executed With Custom Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_browsers_chromium_susp_load_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_susp_load_extension.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "27ba3207-dd30-4812-abbf-5d20c57d474e"
  - "Suspicious Chromium Browser Instance Executed With Custom Extension"
attack_technique_ids:
  - "T1176.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Chromium Browser Instance Executed With Custom Extension

Detects a suspicious process spawning a Chromium based browser process with the 'load-extension' flag to start an instance with a custom extension

## Metadata

- Rule ID: 27ba3207-dd30-4812-abbf-5d20c57d474e
- Status: test
- Level: high
- Author: Aedan Russell, frack113, X__Junior (Nextron Systems)
- Date: 2022-06-19
- Modified: 2023-11-28
- Source Path: rules/windows/process_creation/proc_creation_win_browsers_chromium_susp_load_extension.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1176-software_extensions|T1176.001]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
  Image|endswith:
  - \brave.exe
  - \chrome.exe
  - \msedge.exe
  - \opera.exe
  - \vivaldi.exe
  CommandLine|contains: --load-extension=
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/chromeloader/
- https://emkc.org/s/RJjuLa
- https://www.mandiant.com/resources/blog/lnk-between-browsers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_browsers_chromium_susp_load_extension.yml)
