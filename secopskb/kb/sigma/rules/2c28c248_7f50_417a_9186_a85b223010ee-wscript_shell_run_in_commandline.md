---
sigma_id: "2c28c248-7f50-417a-9186-a85b223010ee"
title: "Wscript Shell Run In CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mshta_inline_vbscript.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_inline_vbscript.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "2c28c248-7f50-417a-9186-a85b223010ee"
  - "Wscript Shell Run In CommandLine"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Wscript Shell Run In CommandLine

Detects the presence of the keywords "Wscript", "Shell" and "Run" in the command, which could indicate a suspicious activity

## Metadata

- Rule ID: 2c28c248-7f50-417a-9186-a85b223010ee
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-31
- Modified: 2023-05-15
- Source Path: rules/windows/process_creation/proc_creation_win_mshta_inline_vbscript.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - Wscript.
  - .Shell
  - .Run
condition: selection
```

## False Positives

- Inline scripting can be used by some rare third party applications or administrators. Investigate and apply additional filters accordingly

## References

- https://web.archive.org/web/20220830122045/http://blog.talosintelligence.com/2022/08/modernloader-delivers-multiple-stealers.html
- https://blog.talosintelligence.com/modernloader-delivers-multiple-stealers-cryptominers-and-rats/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_inline_vbscript.yml)
