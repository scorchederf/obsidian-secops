---
sigma_id: "52788a70-f1da-40dd-8fbd-73b5865d6568"
title: "JScript Compiler Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_jsc_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_jsc_execution.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "52788a70-f1da-40dd-8fbd-73b5865d6568"
  - "JScript Compiler Execution"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# JScript Compiler Execution

Detects the execution of the "jsc.exe" (JScript Compiler).
Attacker might abuse this in order to compile JScript files on the fly and bypassing application whitelisting.

## Metadata

- Rule ID: 52788a70-f1da-40dd-8fbd-73b5865d6568
- Status: test
- Level: low
- Author: frack113
- Date: 2022-05-02
- Modified: 2024-04-24
- Source Path: rules/windows/process_creation/proc_creation_win_jsc_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection:
- Image|endswith: \jsc.exe
- OriginalFileName: jsc.exe
condition: selection
```

## False Positives

- Legitimate use to compile JScript by developers.

## References

- https://lolbas-project.github.io/lolbas/Binaries/Jsc/
- https://www.phpied.com/make-your-javascript-a-windows-exe/
- https://twitter.com/DissectMalware/status/998797808907046913

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_jsc_execution.yml)
