---
sigma_id: "edc2f8ae-2412-4dfd-b9d5-0c57727e70be"
title: "Potential Powershell ReverseShell Connection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_reverse_shell_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_reverse_shell_connection.yml"
build_date: "2026-04-27 19:13:54"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "edc2f8ae-2412-4dfd-b9d5-0c57727e70be"
  - "Potential Powershell ReverseShell Connection"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects usage of the "TcpClient" class. Which can be abused to establish remote connections and reverse-shells. As seen used by the Nishang "Invoke-PowerShellTcpOneLine" reverse shell and other.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection_img:
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
selection_cli:
  CommandLine|contains|all:
  - ' Net.Sockets.TCPClient'
  - .GetStream(
  - .Write(
condition: all of selection_*
```

## False Positives

- In rare administrative cases, this function might be used to check network connectivity

## References

- https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/
- https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/
- https://github.com/samratashok/nishang/blob/414ee1104526d7057f9adaeee196d91ae447283e/Shells/Invoke-PowerShellTcpOneLine.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_reverse_shell_connection.yml)
