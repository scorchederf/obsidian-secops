---
sigma_id: "e4ed6030-ffe5-4e6a-8a8a-ab3c1ab9d94e"
title: "Disable Windows IIS HTTP Logging"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_iis_appcmd_http_logging.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_appcmd_http_logging.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e4ed6030-ffe5-4e6a-8a8a-ab3c1ab9d94e"
  - "Disable Windows IIS HTTP Logging"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Disables HTTP logging on a Windows IIS web server as seen by Threat Group 3390 (Bronze Union)

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Detection

```yaml
selection_img:
- Image|endswith: \appcmd.exe
- OriginalFileName: appcmd.exe
selection_cli:
  CommandLine|contains|all:
  - set
  - config
  - section:httplogging
  - dontLog:true
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.002/T1562.002.md#atomic-test-1---disable-windows-iis-http-logging

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_appcmd_http_logging.yml)
