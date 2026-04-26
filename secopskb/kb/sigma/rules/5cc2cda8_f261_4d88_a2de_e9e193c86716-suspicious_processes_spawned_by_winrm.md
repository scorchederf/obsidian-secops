---
sigma_id: "5cc2cda8-f261-4d88-a2de-e9e193c86716"
title: "Suspicious Processes Spawned by WinRM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winrm_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrm_susp_child_process.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5cc2cda8-f261-4d88-a2de-e9e193c86716"
  - "Suspicious Processes Spawned by WinRM"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Processes Spawned by WinRM

Detects suspicious processes including shells spawnd from WinRM host process

## Metadata

- Rule ID: 5cc2cda8-f261-4d88-a2de-e9e193c86716
- Status: test
- Level: high
- Author: Andreas Hunkeler (@Karneades), Markus Neis
- Date: 2021-05-20
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_winrm_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection:
  ParentImage|endswith: \wsmprovhost.exe
  Image|endswith:
  - \cmd.exe
  - \sh.exe
  - \bash.exe
  - \powershell.exe
  - \pwsh.exe
  - \wsl.exe
  - \schtasks.exe
  - \certutil.exe
  - \whoami.exe
  - \bitsadmin.exe
condition: selection
```

## False Positives

- Legitimate WinRM usage

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrm_susp_child_process.yml)
