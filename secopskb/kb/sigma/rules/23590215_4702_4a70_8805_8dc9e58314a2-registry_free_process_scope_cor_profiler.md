---
sigma_id: "23590215-4702-4a70-8805-8dc9e58314a2"
title: "Registry-Free Process Scope COR_PROFILER"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_cor_profiler.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_cor_profiler.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "23590215-4702-4a70-8805-8dc9e58314a2"
  - "Registry-Free Process Scope COR_PROFILER"
attack_technique_ids:
  - "T1574.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Registry-Free Process Scope COR_PROFILER

Adversaries may leverage the COR_PROFILER environment variable to hijack the execution flow of programs that load the .NET CLR.
The COR_PROFILER is a .NET Framework feature which allows developers to specify an unmanaged (or external of .NET) profiling DLL to be loaded into each .NET process that loads the Common Language Runtime (CLR).
These profiliers are designed to monitor, troubleshoot, and debug managed code executed by the .NET CLR.
(Citation: Microsoft Profiling Mar 2017)
(Citation: Microsoft COR_PROFILER Feb 2013)

## Metadata

- Rule ID: 23590215-4702-4a70-8805-8dc9e58314a2
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-30
- Source Path: rules/windows/powershell/powershell_script/posh_ps_cor_profiler.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.012]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - $env:COR_ENABLE_PROFILING
  - $env:COR_PROFILER
  - $env:COR_PROFILER_PATH
condition: selection
```

## False Positives

- Legitimate administrative script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1574.012/T1574.012.md#atomic-test-3---registry-free-process-scope-cor_profiler

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_cor_profiler.yml)
