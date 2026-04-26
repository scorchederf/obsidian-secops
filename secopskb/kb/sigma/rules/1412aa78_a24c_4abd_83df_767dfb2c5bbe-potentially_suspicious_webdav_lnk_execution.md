---
sigma_id: "1412aa78-a24c-4abd-83df-767dfb2c5bbe"
title: "Potentially Suspicious WebDAV LNK Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_webdav_lnk_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webdav_lnk_execution.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1412aa78-a24c-4abd-83df-767dfb2c5bbe"
  - "Potentially Suspicious WebDAV LNK Execution"
attack_technique_ids:
  - "T1059.001"
  - "T1204"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious WebDAV LNK Execution

Detects possible execution via LNK file accessed on a WebDAV server.

## Metadata

- Rule ID: 1412aa78-a24c-4abd-83df-767dfb2c5bbe
- Status: test
- Level: medium
- Author: Micah Babinski
- Date: 2023-08-21
- Source Path: rules/windows/process_creation/proc_creation_win_webdav_lnk_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1204-user_execution|T1204]]

## Detection

```yaml
selection:
  ParentImage|endswith: \explorer.exe
  Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \wscript.exe
  CommandLine|contains: \DavWWWRoot\
condition: selection
```

## False Positives

- Unknown

## References

- https://www.trellix.com/en-us/about/newsroom/stories/research/beyond-file-search-a-novel-method.html
- https://micahbabinski.medium.com/search-ms-webdav-and-chill-99c5b23ac462

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webdav_lnk_execution.yml)
