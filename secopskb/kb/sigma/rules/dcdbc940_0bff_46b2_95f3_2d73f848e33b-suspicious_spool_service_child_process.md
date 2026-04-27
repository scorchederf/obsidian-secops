---
sigma_id: "dcdbc940-0bff-46b2-95f3-2d73f848e33b"
title: "Suspicious Spool Service Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_spoolsv_susp_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_spoolsv_susp_child_processes.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "dcdbc940-0bff-46b2-95f3-2d73f848e33b"
  - "Suspicious Spool Service Child Process"
attack_technique_ids:
  - "T1203"
  - "T1068"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Spool Service Child Process

Detects suspicious print spool service (spoolsv.exe) child processes.

## Metadata

- Rule ID: dcdbc940-0bff-46b2-95f3-2d73f848e33b
- Status: test
- Level: high
- Author: Justin C. (@endisphotic), @dreadphones (detection), Thomas Patzke (Sigma rule)
- Date: 2021-07-11
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_spoolsv_susp_child_processes.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203]]
- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068]]

## Detection

```yaml
spoolsv:
  ParentImage|endswith: \spoolsv.exe
  IntegrityLevel:
  - System
  - S-1-16-16384
suspicious_unrestricted:
  Image|endswith:
  - \gpupdate.exe
  - \whoami.exe
  - \nltest.exe
  - \taskkill.exe
  - \wmic.exe
  - \taskmgr.exe
  - \sc.exe
  - \findstr.exe
  - \curl.exe
  - \wget.exe
  - \certutil.exe
  - \bitsadmin.exe
  - \accesschk.exe
  - \wevtutil.exe
  - \bcdedit.exe
  - \fsutil.exe
  - \cipher.exe
  - \schtasks.exe
  - \write.exe
  - \wuauclt.exe
  - \systeminfo.exe
  - \reg.exe
  - \query.exe
suspicious_net:
  Image|endswith:
  - \net.exe
  - \net1.exe
suspicious_net_filter:
  CommandLine|contains: start
suspicious_cmd:
  Image|endswith: \cmd.exe
suspicious_cmd_filter:
  CommandLine|contains:
  - .spl
  - route add
  - program files
suspicious_netsh:
  Image|endswith: \netsh.exe
suspicious_netsh_filter:
  CommandLine|contains:
  - add portopening
  - rule name
suspicious_powershell:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
suspicious_powershell_filter:
  CommandLine|contains: .spl
suspicious_rundll32_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
suspicious_rundll32_cli:
  CommandLine|endswith: rundll32.exe
condition: spoolsv and ( suspicious_unrestricted or (suspicious_net and not suspicious_net_filter)
  or (suspicious_cmd and not suspicious_cmd_filter) or (suspicious_netsh and not suspicious_netsh_filter)
  or (suspicious_powershell and not suspicious_powershell_filter) or all of suspicious_rundll32_*
  )
```

## False Positives

- Unknown

## References

- https://github.com/microsoft/Microsoft-365-Defender-Hunting-Queries/blob/efa17a600b43c897b4b7463cc8541daa1987eeb4/Exploits/Print%20Spooler%20RCE/Suspicious%20Spoolsv%20Child%20Process.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_spoolsv_susp_child_processes.yml)
