---
sigma_id: "99b7460d-c9f1-40d7-a316-1f36f61d52ee"
title: "Cscript/Wscript Uncommon Script Extension Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wscript_cscript_uncommon_extension_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wscript_cscript_uncommon_extension_exec.yml"
build_date: "2026-04-27 19:13:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Wscript/Cscript executing a file with an uncommon (i.e. non-script) extension

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]]

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
