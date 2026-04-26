---
sigma_id: "99b7460d-c9f1-40d7-a316-1f36f61d52ee"
title: "Cscript/Wscript Uncommon Script Extension Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wscript_cscript_uncommon_extension_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wscript_cscript_uncommon_extension_exec.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "99b7460d-c9f1-40d7-a316-1f36f61d52ee"
  - "Cscript/Wscript Uncommon Script Extension Execution"
attack_technique_ids:
  - "T1059.005"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cscript/Wscript Uncommon Script Extension Execution

Detects Wscript/Cscript executing a file with an uncommon (i.e. non-script) extension

## Metadata

- Rule ID: 99b7460d-c9f1-40d7-a316-1f36f61d52ee
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-15
- Modified: 2023-06-19
- Source Path: rules/windows/process_creation/proc_creation_win_wscript_cscript_uncommon_extension_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Detection

```yaml
selection_img:
- OriginalFileName:
  - wscript.exe
  - cscript.exe
- Image|endswith:
  - \wscript.exe
  - \cscript.exe
selection_extension:
  CommandLine|contains:
  - .csv
  - .dat
  - .doc
  - .gif
  - .jpeg
  - .jpg
  - .png
  - .ppt
  - .txt
  - .xls
  - .xml
condition: all of selection_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wscript_cscript_uncommon_extension_exec.yml)
