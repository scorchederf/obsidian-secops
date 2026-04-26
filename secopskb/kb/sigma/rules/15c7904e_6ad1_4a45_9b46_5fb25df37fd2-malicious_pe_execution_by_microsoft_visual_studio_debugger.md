---
sigma_id: "15c7904e-6ad1-4a45-9b46-5fb25df37fd2"
title: "Malicious PE Execution by Microsoft Visual Studio Debugger"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_use_of_vsjitdebugger_bin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_use_of_vsjitdebugger_bin.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "15c7904e-6ad1-4a45-9b46-5fb25df37fd2"
  - "Malicious PE Execution by Microsoft Visual Studio Debugger"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Malicious PE Execution by Microsoft Visual Studio Debugger

There is an option for a MS VS Just-In-Time Debugger "vsjitdebugger.exe" to launch specified executable and attach a debugger.
This option may be used adversaries to execute malicious code by signed verified binary.
The debugger is installed alongside with Microsoft Visual Studio package.

## Metadata

- Rule ID: 15c7904e-6ad1-4a45-9b46-5fb25df37fd2
- Status: test
- Level: medium
- Author: Agro (@agro_sev), Ensar Şamil (@sblmsrsn), oscd.community
- Date: 2020-10-14
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_susp_use_of_vsjitdebugger_bin.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ParentImage|endswith: \vsjitdebugger.exe
reduction1:
  Image|endswith: \vsimmersiveactivatehelper*.exe
reduction2:
  Image|endswith: \devenv.exe
condition: selection and not (reduction1 or reduction2)
```

## False Positives

- The process spawned by vsjitdebugger.exe is uncommon.

## References

- https://twitter.com/pabraeken/status/990758590020452353
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Vsjitdebugger/
- https://learn.microsoft.com/en-us/visualstudio/debugger/debug-using-the-just-in-time-debugger?view=vs-2019

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_use_of_vsjitdebugger_bin.yml)
