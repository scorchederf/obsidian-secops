---
sigma_id: "6c0ce3b6-85e2-49d4-9c3f-6e008ce9796e"
title: "Suspicious Deno File Written from Remote Source"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_creation_deno.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_creation_deno.yml"
build_date: "2026-04-26 14:14:36"
status: "experimental"
level: "low"
logsource: "windows / file_event"
aliases:
  - "6c0ce3b6-85e2-49d4-9c3f-6e008ce9796e"
  - "Suspicious Deno File Written from Remote Source"
attack_technique_ids:
  - "T1204"
  - "T1059.007"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Deno File Written from Remote Source

Detects Deno writing a file from a direct HTTP(s) call and writing to the appdata folder or bringing it's own malicious DLL.
This behavior may indicate an attempt to execute remotely hosted, potentially malicious files through deno.

## Metadata

- Rule ID: 6c0ce3b6-85e2-49d4-9c3f-6e008ce9796e
- Status: experimental
- Level: low
- Author: Josh Nickels, Michael Taggart
- Date: 2025-05-22
- Source Path: rules/windows/file/file_event/file_event_win_creation_deno.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_path:
  TargetFilename|contains:
  - \deno\gen\
  - \deno\remote\https\
  TargetFilename|contains|all:
  - :\Users\
  - \AppData\
condition: selection_path
```

## False Positives

- Legitimate usage of deno to request a file or bring a DLL to a host

## References

- https://taggart-tech.com/evildeno/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_creation_deno.yml)
