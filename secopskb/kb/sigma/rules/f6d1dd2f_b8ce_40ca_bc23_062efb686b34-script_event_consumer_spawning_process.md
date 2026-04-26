---
sigma_id: "f6d1dd2f-b8ce-40ca-bc23-062efb686b34"
title: "Script Event Consumer Spawning Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_scrcons_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_scrcons_susp_child_process.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f6d1dd2f-b8ce-40ca-bc23-062efb686b34"
  - "Script Event Consumer Spawning Process"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Script Event Consumer Spawning Process

Detects a suspicious child process of Script Event Consumer (scrcons.exe).

## Metadata

- Rule ID: f6d1dd2f-b8ce-40ca-bc23-062efb686b34
- Status: test
- Level: high
- Author: Sittikorn S
- Date: 2021-06-21
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_scrcons_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection:
  ParentImage|endswith: \scrcons.exe
  Image|endswith:
  - \svchost.exe
  - \dllhost.exe
  - \powershell.exe
  - \pwsh.exe
  - \wscript.exe
  - \cscript.exe
  - \schtasks.exe
  - \regsvr32.exe
  - \mshta.exe
  - \rundll32.exe
  - \msiexec.exe
  - \msbuild.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/child-processes/
- https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-analytics-alert-reference/cortex-xdr-analytics-alert-reference/scrcons-exe-rare-child-process.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_scrcons_susp_child_process.yml)
