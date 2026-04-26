---
sigma_id: "5f60740a-f57b-4e76-82a1-15b6ff2cb134"
title: "Registry Modification Via Regini.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regini_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regini_execution.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "5f60740a-f57b-4e76-82a1-15b6ff2cb134"
  - "Registry Modification Via Regini.EXE"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Registry Modification Via Regini.EXE

Detects the execution of regini.exe which can be used to modify registry keys, the changes are imported from one or more text files.

## Metadata

- Rule ID: 5f60740a-f57b-4e76-82a1-15b6ff2cb134
- Status: test
- Level: low
- Author: Eli Salem, Sander Wiebing, oscd.community
- Date: 2020-10-08
- Modified: 2023-02-08
- Source Path: rules/windows/process_creation/proc_creation_win_regini_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
- Image|endswith: \regini.exe
- OriginalFileName: REGINI.EXE
filter:
  CommandLine|re: :[^ \\]
condition: selection and not filter
```

## False Positives

- Legitimate modification of keys

## References

- https://lolbas-project.github.io/lolbas/Binaries/Regini/
- https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/regini

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regini_execution.yml)
