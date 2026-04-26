---
sigma_id: "7efd2c8d-8b18-45b7-947d-adfe9ed04f61"
title: "AgentExecutor PowerShell Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_agentexecutor_potential_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_agentexecutor_potential_abuse.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7efd2c8d-8b18-45b7-947d-adfe9ed04f61"
  - "AgentExecutor PowerShell Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AgentExecutor PowerShell Execution

Detects execution of the AgentExecutor.exe binary. Which can be abused as a LOLBIN to execute powershell scripts with the ExecutionPolicy "Bypass" or any binary named "powershell.exe" located in the path provided by 6th positional argument

## Metadata

- Rule ID: 7efd2c8d-8b18-45b7-947d-adfe9ed04f61
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), memory-shards
- Date: 2022-12-24
- Modified: 2024-08-07
- Source Path: rules/windows/process_creation/proc_creation_win_agentexecutor_potential_abuse.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image: \AgentExecutor.exe
- OriginalFileName: AgentExecutor.exe
selection_cli:
  CommandLine|contains:
  - ' -powershell'
  - ' -remediationScript'
filter_main_intune:
  ParentImage|endswith: \Microsoft.Management.Services.IntuneWindowsAgent.exe
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Legitimate use via Intune management. You exclude script paths and names to reduce FP rate

## References

- https://twitter.com/lefterispan/status/1286259016436514816
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Agentexecutor/
- https://learn.microsoft.com/en-us/mem/intune/apps/intune-management-extension
- https://twitter.com/jseerden/status/1247985304667066373/photo/1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_agentexecutor_potential_abuse.yml)
