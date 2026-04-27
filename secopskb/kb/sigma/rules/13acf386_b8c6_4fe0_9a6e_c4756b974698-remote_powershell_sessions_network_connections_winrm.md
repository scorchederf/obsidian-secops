---
sigma_id: "13acf386-b8c6-4fe0-9a6e-c4756b974698"
title: "Remote PowerShell Sessions Network Connections (WinRM)"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_remote_powershell_session.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_remote_powershell_session.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "13acf386-b8c6-4fe0-9a6e-c4756b974698"
  - "Remote PowerShell Sessions Network Connections (WinRM)"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects basic PowerShell Remoting (WinRM) by monitoring for network inbound connections to ports 5985 OR 5986

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection:
  EventID: 5156
  DestPort:
  - 5985
  - 5986
  LayerRTID: 44
condition: selection
```

## False Positives

- Legitimate use of remote PowerShell execution

## References

- https://threathunterplaybook.com/hunts/windows/190511-RemotePwshExecution/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_remote_powershell_session.yml)
