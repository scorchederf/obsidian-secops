---
sigma_id: "869b9ca7-9ea2-4a5a-8325-e80e62f75445"
title: "Suspicious Child Process Of SQL Server"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mssql_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mssql_susp_child_process.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "869b9ca7-9ea2-4a5a-8325-e80e62f75445"
  - "Suspicious Child Process Of SQL Server"
attack_technique_ids:
  - "T1505.003"
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Child Process Of SQL Server

Detects suspicious child processes of the SQLServer process. This could indicate potential RCE or SQL Injection.

## Metadata

- Rule ID: 869b9ca7-9ea2-4a5a-8325-e80e62f75445
- Status: test
- Level: high
- Author: FPT.EagleEye Team, wagga
- Date: 2020-12-11
- Modified: 2023-05-04
- Source Path: rules/windows/process_creation/proc_creation_win_mssql_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]
- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection:
  ParentImage|endswith: \sqlservr.exe
  Image|endswith:
  - \bash.exe
  - \bitsadmin.exe
  - \cmd.exe
  - \netstat.exe
  - \nltest.exe
  - \ping.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \sh.exe
  - \systeminfo.exe
  - \tasklist.exe
  - \wsl.exe
filter_optional_datev:
  ParentImage|startswith: C:\Program Files\Microsoft SQL Server\
  ParentImage|endswith: DATEV_DBENGINE\MSSQL\Binn\sqlservr.exe
  Image: C:\Windows\System32\cmd.exe
  CommandLine|startswith: '"C:\Windows\system32\cmd.exe" '
condition: selection and not 1 of filter_optional_*
```

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mssql_susp_child_process.yml)
