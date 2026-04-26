---
sigma_id: "96b9f619-aa91-478f-bacb-c3e50f8df575"
title: "Remote PowerShell Session (PS Module)"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_remote_powershell_session.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_remote_powershell_session.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "96b9f619-aa91-478f-bacb-c3e50f8df575"
  - "Remote PowerShell Session (PS Module)"
attack_technique_ids:
  - "T1059.001"
  - "T1021.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote PowerShell Session (PS Module)

Detects remote PowerShell sessions

## Metadata

- Rule ID: 96b9f619-aa91-478f-bacb-c3e50f8df575
- Status: test
- Level: high
- Author: Roberto Rodriguez @Cyb3rWard0g, Tim Shelton
- Date: 2019-08-10
- Modified: 2023-01-20
- Source Path: rules/windows/powershell/powershell_module/posh_pm_remote_powershell_session.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1021-remote_services|T1021.006]]

## Detection

```yaml
selection:
  ContextInfo|contains|all:
  - ' = ServerRemoteHost '
  - wsmprovhost.exe
filter_pwsh_archive:
  ContextInfo|contains: \Windows\system32\WindowsPowerShell\v1.0\Modules\Microsoft.PowerShell.Archive\Microsoft.PowerShell.Archive.psm1
condition: selection and not 1 of filter_*
```

## False Positives

- Legitimate use remote PowerShell sessions

## References

- https://threathunterplaybook.com/hunts/windows/190511-RemotePwshExecution/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_remote_powershell_session.yml)
