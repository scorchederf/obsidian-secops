---
sigma_id: "ba3874b9-0fae-465f-836c-eb5d071a1789"
title: "NodeJS Execution of JavaScript File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_security_susp_node_js_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_security_susp_node_js_execution.yml"
build_date: "2026-04-26 14:14:30"
status: "experimental"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "ba3874b9-0fae-465f-836c-eb5d071a1789"
  - "NodeJS Execution of JavaScript File"
attack_technique_ids:
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# NodeJS Execution of JavaScript File

Detects execution of JavaScript or JSC files using NodeJs binary node.exe, that could be potentially suspicious.
Node.js is a popular open-source JavaScript runtime that runs code outside browsers and is widely used for both frontend and backend development.
Adversaries have been observed abusing Node.js to disguise malware as legitimate processes, evade security defenses, and maintain persistence within target systems.
Because Node.js is commonly used, this rule may generate false positives in some environments. However, if such activity is unusual in your environment, it is highly suspicious and warrants immediate investigation.

## Metadata

- Rule ID: ba3874b9-0fae-465f-836c-eb5d071a1789
- Status: experimental
- Level: low
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-04-21
- Source Path: rules/windows/process_creation/proc_creation_win_security_susp_node_js_execution.yml

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
  CommandLine|contains: .js
condition: all of selection_*
```

## False Positives

- Legitimate use of node.exe to execute JavaScript or JSC files on your environment

## References

- https://www.microsoft.com/en-us/security/blog/2025/04/15/threat-actors-misuse-node-js-to-deliver-malware-and-other-malicious-payloads/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_security_susp_node_js_execution.yml)
