---
sigma_id: "850d55f9-6eeb-4492-ad69-a72338f65ba4"
title: "C# IL Code Compilation Via Ilasm.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ilasm_il_code_compilation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ilasm_il_code_compilation.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "850d55f9-6eeb-4492-ad69-a72338f65ba4"
  - "C# IL Code Compilation Via Ilasm.EXE"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# C# IL Code Compilation Via Ilasm.EXE

Detects the use of "Ilasm.EXE" in order to compile C# intermediate (IL) code to EXE or DLL.

## Metadata

- Rule ID: 850d55f9-6eeb-4492-ad69-a72338f65ba4
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-05-07
- Modified: 2022-05-16
- Source Path: rules/windows/process_creation/proc_creation_win_ilasm_il_code_compilation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection_img:
- Image|endswith: \ilasm.exe
- OriginalFileName: ilasm.exe
selection_cli:
  CommandLine|contains:
  - ' /dll'
  - ' /exe'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Ilasm/
- https://www.echotrail.io/insights/search/ilasm.exe

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ilasm_il_code_compilation.yml)
