---
sigma_id: "60167e5c-84b2-4c95-a7ac-86281f27c445"
title: "Remote PowerShell Session (PS Classic)"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_remote_powershell_session.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_remote_powershell_session.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "windows / ps_classic_start"
aliases:
  - "60167e5c-84b2-4c95-a7ac-86281f27c445"
  - "Remote PowerShell Session (PS Classic)"
attack_technique_ids:
  - "T1059.001"
  - "T1021.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote PowerShell Session (PS Classic)

Detects remote PowerShell sessions

## Metadata

- Rule ID: 60167e5c-84b2-4c95-a7ac-86281f27c445
- Status: test
- Level: low
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-08-10
- Modified: 2024-01-03
- Source Path: rules/windows/powershell/powershell_classic/posh_pc_remote_powershell_session.yml

## Logsource

- category: ps_classic_start
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1021-remote_services|T1021.006]]

## Detection

```yaml
selection:
  Data|contains|all:
  - HostName=ServerRemoteHost
  - wsmprovhost.exe
condition: selection
```

## False Positives

- Legitimate use remote PowerShell sessions

## References

- https://threathunterplaybook.com/hunts/windows/190511-RemotePwshExecution/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_remote_powershell_session.yml)
