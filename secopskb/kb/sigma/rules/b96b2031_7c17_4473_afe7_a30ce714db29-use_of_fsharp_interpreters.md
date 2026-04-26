---
sigma_id: "b96b2031-7c17-4473-afe7-a30ce714db29"
title: "Use of FSharp Interpreters"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_fsi_fsharp_code_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fsi_fsharp_code_execution.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b96b2031-7c17-4473-afe7-a30ce714db29"
  - "Use of FSharp Interpreters"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use of FSharp Interpreters

Detects the execution of FSharp Interpreters "FsiAnyCpu.exe" and "FSi.exe"
Both can be used for AWL bypass and to execute F# code via scripts or inline.

## Metadata

- Rule ID: b96b2031-7c17-4473-afe7-a30ce714db29
- Status: test
- Level: medium
- Author: Christopher Peacock @SecurePeacock, SCYTHE @scythe_io
- Date: 2022-06-02
- Modified: 2024-04-23
- Source Path: rules/windows/process_creation/proc_creation_win_fsi_fsharp_code_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
- Image|endswith:
  - \fsi.exe
  - \fsianycpu.exe
- OriginalFileName:
  - fsi.exe
  - fsianycpu.exe
condition: selection
```

## False Positives

- Legitimate use by a software developer.

## References

- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/design/applications-that-can-bypass-wdac
- https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/FsiAnyCpu/
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Fsi/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fsi_fsharp_code_execution.yml)
