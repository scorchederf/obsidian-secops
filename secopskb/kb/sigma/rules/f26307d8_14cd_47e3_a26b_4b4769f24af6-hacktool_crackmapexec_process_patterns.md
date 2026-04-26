---
sigma_id: "f26307d8-14cd-47e3-a26b-4b4769f24af6"
title: "HackTool - CrackMapExec Process Patterns"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_patterns.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f26307d8-14cd-47e3-a26b-4b4769f24af6"
  - "HackTool - CrackMapExec Process Patterns"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - CrackMapExec Process Patterns

Detects suspicious process patterns found in logs when CrackMapExec is used

## Metadata

- Rule ID: f26307d8-14cd-47e3-a26b-4b4769f24af6
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-12
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_patterns.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_lsass_dump1:
  CommandLine|contains|all:
  - 'tasklist /fi '
  - Imagename eq lsass.exe
  CommandLine|contains:
  - 'cmd.exe /c '
  - 'cmd.exe /r '
  - 'cmd.exe /k '
  - 'cmd /c '
  - 'cmd /r '
  - 'cmd /k '
  User|contains:
  - AUTHORI
  - AUTORI
selection_lsass_dump2:
  CommandLine|contains|all:
  - do rundll32.exe C:\windows\System32\comsvcs.dll, MiniDump
  - \Windows\Temp\
  - ' full'
  - '%%B'
selection_procdump:
  CommandLine|contains|all:
  - tasklist /v /fo csv
  - findstr /i "lsass"
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://mpgn.gitbook.io/crackmapexec/smb-protocol/obtaining-credentials/dump-lsass

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_patterns.yml)
