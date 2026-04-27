---
sigma_id: "9f50fe98-fe5c-4a2d-86c7-fad7f63ed622"
title: "Potentially Suspicious ASP.NET Compilation Via AspNetCompiler"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_aspnet_compiler_susp_paths.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_aspnet_compiler_susp_paths.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9f50fe98-fe5c-4a2d-86c7-fad7f63ed622"
  - "Potentially Suspicious ASP.NET Compilation Via AspNetCompiler"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potentially Suspicious ASP.NET Compilation Via AspNetCompiler

Detects execution of "aspnet_compiler.exe" with potentially suspicious paths for compilation.

## Metadata

- Rule ID: 9f50fe98-fe5c-4a2d-86c7-fad7f63ed622
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-14
- Modified: 2025-02-24
- Source Path: rules/windows/process_creation/proc_creation_win_aspnet_compiler_susp_paths.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection:
  Image|contains:
  - :\Windows\Microsoft.NET\Framework\
  - :\Windows\Microsoft.NET\Framework64\
  - :\Windows\Microsoft.NET\FrameworkArm\
  - :\Windows\Microsoft.NET\FrameworkArm64\
  Image|endswith: \aspnet_compiler.exe
  CommandLine|contains:
  - \Users\Public\
  - \AppData\Local\Temp\
  - \AppData\Local\Roaming\
  - :\Temp\
  - :\Windows\Temp\
  - :\Windows\System32\Tasks\
  - :\Windows\Tasks\
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Aspnet_Compiler/
- https://ijustwannared.team/2020/08/01/the-curious-case-of-aspnet_compiler-exe/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_aspnet_compiler_susp_paths.yml)
