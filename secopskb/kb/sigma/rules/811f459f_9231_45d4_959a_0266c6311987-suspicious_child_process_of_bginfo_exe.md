---
sigma_id: "811f459f-9231-45d4-959a-0266c6311987"
title: "Suspicious Child Process Of BgInfo.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bginfo_suspicious_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bginfo_suspicious_child_process.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "811f459f-9231-45d4-959a-0266c6311987"
  - "Suspicious Child Process Of BgInfo.EXE"
attack_technique_ids:
  - "T1059.005"
  - "T1218"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Child Process Of BgInfo.EXE

Detects suspicious child processes of "BgInfo.exe" which could be a sign of potential abuse of the binary to proxy execution via external VBScript

## Metadata

- Rule ID: 811f459f-9231-45d4-959a-0266c6311987
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-16
- Source Path: rules/windows/process_creation/proc_creation_win_bginfo_suspicious_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \bginfo.exe
  - \bginfo64.exe
selection_child:
- Image|endswith:
  - \calc.exe
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \notepad.exe
  - \powershell.exe
  - \pwsh.exe
  - \wscript.exe
- Image|contains:
  - \AppData\Local\
  - \AppData\Roaming\
  - :\Users\Public\
  - :\Temp\
  - :\Windows\Temp\
  - :\PerfLogs\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Bginfo/
- https://oddvar.moe/2017/05/18/bypassing-application-whitelisting-with-bginfo/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bginfo_suspicious_child_process.yml)
