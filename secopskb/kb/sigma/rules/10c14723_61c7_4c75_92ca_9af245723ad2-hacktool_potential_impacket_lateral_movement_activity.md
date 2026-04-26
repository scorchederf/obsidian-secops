---
sigma_id: "10c14723-61c7-4c75-92ca-9af245723ad2"
title: "HackTool - Potential Impacket Lateral Movement Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_impacket_lateral_movement.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_impacket_lateral_movement.yml"
build_date: "2026-04-26 15:01:45"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "10c14723-61c7-4c75-92ca-9af245723ad2"
  - "HackTool - Potential Impacket Lateral Movement Activity"
attack_technique_ids:
  - "T1047"
  - "T1021.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Potential Impacket Lateral Movement Activity

Detects wmiexec/dcomexec/atexec/smbexec from Impacket framework

## Metadata

- Rule ID: 10c14723-61c7-4c75-92ca-9af245723ad2
- Status: stable
- Level: high
- Author: Ecco, oscd.community, Jonhnathan Ribeiro, Tim Rauch
- Date: 2019-09-03
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_impacket_lateral_movement.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1021-remote_services|T1021.003]]

## Detection

```yaml
selection_other:
  ParentImage|endswith:
  - \wmiprvse.exe
  - \mmc.exe
  - \explorer.exe
  - \services.exe
  CommandLine|contains|all:
  - cmd.exe
  - /Q
  - /c
  - \\\\127.0.0.1\\
  - '&1'
selection_atexec:
  ParentCommandLine|contains:
  - svchost.exe -k netsvcs
  - taskeng.exe
  CommandLine|contains|all:
  - cmd.exe
  - /C
  - Windows\Temp\
  - '&1'
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/SecureAuthCorp/impacket/blob/8b1a99f7c715702eafe3f24851817bb64721b156/examples/wmiexec.py
- https://github.com/SecureAuthCorp/impacket/blob/8b1a99f7c715702eafe3f24851817bb64721b156/examples/atexec.py
- https://github.com/SecureAuthCorp/impacket/blob/8b1a99f7c715702eafe3f24851817bb64721b156/examples/smbexec.py
- https://github.com/SecureAuthCorp/impacket/blob/8b1a99f7c715702eafe3f24851817bb64721b156/examples/dcomexec.py
- https://www.elastic.co/guide/en/security/current/suspicious-cmd-execution-via-wmi.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_impacket_lateral_movement.yml)
