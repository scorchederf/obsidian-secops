---
sigma_id: "42a993dd-bb3e-48c8-b372-4d6684c4106c"
title: "HackTool - CrackMapExec Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_execution.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "42a993dd-bb3e-48c8-b372-4d6684c4106c"
  - "HackTool - CrackMapExec Execution"
attack_technique_ids:
  - "T1047"
  - "T1053"
  - "T1059.003"
  - "T1059.001"
  - "T1110"
  - "T1201"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This rule detect common flag combinations used by CrackMapExec in order to detect its use even if the binary has been replaced.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[kb/attack/techniques/T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[kb/attack/techniques/T1110-brute_force|T1110: Brute Force]]
- [[kb/attack/techniques/T1201-password_policy_discovery|T1201: Password Policy Discovery]]

## Detection

```yaml
selection_binary:
  Image|endswith: \crackmapexec.exe
selection_special:
  CommandLine|contains: ' -M pe_inject '
selection_execute:
  CommandLine|contains|all:
  - ' --local-auth'
  - ' -u '
  - ' -x '
selection_hash:
  CommandLine|contains|all:
  - ' --local-auth'
  - ' -u '
  - ' -p '
  - ' -H ''NTHASH'''
selection_module_mssql:
  CommandLine|contains|all:
  - ' mssql '
  - ' -u '
  - ' -p '
  - ' -M '
  - ' -d '
selection_module_smb1:
  CommandLine|contains|all:
  - ' smb '
  - ' -u '
  - ' -H '
  - ' -M '
  - ' -o '
selection_module_smb2:
  CommandLine|contains|all:
  - ' smb '
  - ' -u '
  - ' -p '
  - ' --local-auth'
part_localauth_1:
  CommandLine|contains|all:
  - ' --local-auth'
  - ' -u '
  - ' -p '
part_localauth_2:
  CommandLine|contains|all:
  - ' 10.'
  - ' 192.168.'
  - '/24 '
condition: 1 of selection_* or all of part_localauth*
```

## False Positives

- Unknown

## References

- https://mpgn.gitbook.io/crackmapexec/smb-protocol/authentication/checking-credentials-local
- https://www.mandiant.com/resources/telegram-malware-iranian-espionage
- https://www.infosecmatter.com/crackmapexec-module-library/?cmem=mssql-mimikatz
- https://www.infosecmatter.com/crackmapexec-module-library/?cmem=smb-pe_inject

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_execution.yml)
