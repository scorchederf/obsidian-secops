---
sigma_id: "84b1706c-932a-44c4-ae28-892b28a25b94"
title: "OneNote.EXE Execution of Malicious Embedded Scripts"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_onenote_embedded_script_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_onenote_embedded_script_execution.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "84b1706c-932a-44c4-ae28-892b28a25b94"
  - "OneNote.EXE Execution of Malicious Embedded Scripts"
attack_technique_ids:
  - "T1218.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# OneNote.EXE Execution of Malicious Embedded Scripts

Detects the execution of malicious OneNote documents that contain embedded scripts.
When a user clicks on a OneNote attachment and then on the malicious link inside the ".one" file, it exports and executes the malicious embedded script from specific directories.

## Metadata

- Rule ID: 84b1706c-932a-44c4-ae28-892b28a25b94
- Status: test
- Level: high
- Author: @kostastsale
- Date: 2023-02-02
- Source Path: rules/windows/process_creation/proc_creation_win_office_onenote_embedded_script_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.001]]

## Detection

```yaml
selection:
  ParentImage|endswith: \onenote.exe
  Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \wscript.exe
  CommandLine|contains:
  - \exported\
  - \onenoteofflinecache_files\
condition: selection
```

## False Positives

- Unlikely

## References

- https://bazaar.abuse.ch/browse/tag/one/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_onenote_embedded_script_execution.yml)
