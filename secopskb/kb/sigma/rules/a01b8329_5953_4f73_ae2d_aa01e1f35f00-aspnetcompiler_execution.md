---
sigma_id: "a01b8329-5953-4f73-ae2d-aa01e1f35f00"
title: "AspNetCompiler Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_aspnet_compiler_exectuion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_aspnet_compiler_exectuion.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a01b8329-5953-4f73-ae2d-aa01e1f35f00"
  - "AspNetCompiler Execution"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AspNetCompiler Execution

Detects execution of "aspnet_compiler.exe" which can be abused to compile and execute C# code.

## Metadata

- Rule ID: a01b8329-5953-4f73-ae2d-aa01e1f35f00
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-11-24
- Modified: 2025-02-24
- Source Path: rules/windows/process_creation/proc_creation_win_aspnet_compiler_exectuion.yml

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
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Aspnet_Compiler/
- https://ijustwannared.team/2020/08/01/the-curious-case-of-aspnet_compiler-exe/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_aspnet_compiler_exectuion.yml)
