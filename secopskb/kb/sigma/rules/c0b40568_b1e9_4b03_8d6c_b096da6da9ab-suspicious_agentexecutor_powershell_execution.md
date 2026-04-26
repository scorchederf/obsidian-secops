---
sigma_id: "c0b40568-b1e9-4b03-8d6c-b096da6da9ab"
title: "Suspicious AgentExecutor PowerShell Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_agentexecutor_susp_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_agentexecutor_susp_usage.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c0b40568-b1e9-4b03-8d6c-b096da6da9ab"
  - "Suspicious AgentExecutor PowerShell Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious AgentExecutor PowerShell Execution

Detects execution of the AgentExecutor.exe binary. Which can be abused as a LOLBIN to execute powershell scripts with the ExecutionPolicy "Bypass" or any binary named "powershell.exe" located in the path provided by 6th positional argument

## Metadata

- Rule ID: c0b40568-b1e9-4b03-8d6c-b096da6da9ab
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), memory-shards
- Date: 2022-12-24
- Modified: 2024-08-07
- Source Path: rules/windows/process_creation/proc_creation_win_agentexecutor_susp_usage.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \AgentExecutor.exe
- OriginalFileName: AgentExecutor.exe
selection_cli:
  CommandLine|contains:
  - ' -powershell'
  - ' -remediationScript'
filter_main_pwsh:
  CommandLine|contains:
  - C:\Windows\System32\WindowsPowerShell\v1.0\
  - C:\Windows\SysWOW64\WindowsPowerShell\v1.0\
filter_main_intune:
  ParentImage|endswith: \Microsoft.Management.Services.IntuneWindowsAgent.exe
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/lefterispan/status/1286259016436514816
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Agentexecutor/
- https://learn.microsoft.com/en-us/mem/intune/apps/intune-management-extension
- https://twitter.com/jseerden/status/1247985304667066373/photo/1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_agentexecutor_susp_usage.yml)
