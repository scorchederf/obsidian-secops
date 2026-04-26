---
sigma_id: "8537c866-072e-460d-bfff-aaf39cbd73d3"
title: "Potentially Suspicious Inline JavaScript Execution via NodeJS Binary"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_inline_node_js_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_inline_node_js_execution.yml"
build_date: "2026-04-26 14:14:33"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "8537c866-072e-460d-bfff-aaf39cbd73d3"
  - "Potentially Suspicious Inline JavaScript Execution via NodeJS Binary"
attack_technique_ids:
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Inline JavaScript Execution via NodeJS Binary

Detects potentially suspicious inline JavaScript execution using Node.js with specific keywords in the command line.

## Metadata

- Rule ID: 8537c866-072e-460d-bfff-aaf39cbd73d3
- Status: experimental
- Level: medium
- Author: Microsoft (idea), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-04-21
- Source Path: rules/windows/process_creation/proc_creation_win_susp_inline_node_js_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Detection

```yaml
selection_img:
- Image|endswith: \node.exe
- OriginalFileName: node.exe
- Product: Node.js
selection_cmd:
  CommandLine|contains|all:
  - http
  - execSync
  - spawn
  - fs
  - path
  - zlib
condition: all of selection_*
```

## False Positives

- Legitimate scripts using Node.js with these modules

## References

- https://www.microsoft.com/en-us/security/blog/2025/04/15/threat-actors-misuse-node-js-to-deliver-malware-and-other-malicious-payloads/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_inline_node_js_execution.yml)
