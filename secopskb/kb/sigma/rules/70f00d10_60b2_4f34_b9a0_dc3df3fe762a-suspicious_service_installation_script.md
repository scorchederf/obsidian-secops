---
sigma_id: "70f00d10-60b2-4f34-b9a0-dc3df3fe762a"
title: "Suspicious Service Installation Script"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_susp_service_installation_script.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_susp_service_installation_script.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "70f00d10-60b2-4f34-b9a0-dc3df3fe762a"
  - "Suspicious Service Installation Script"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious service installation scripts

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]

## Detection

```yaml
selection_eid:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_cmd_flags:
  ImagePath|contains|windash:
  - ' -c '
  - ' -r '
  - ' -k '
selection_binaries:
  ImagePath|contains:
  - cscript
  - mshta
  - powershell
  - pwsh
  - regsvr32
  - rundll32
  - wscript
condition: all of selection_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_susp_service_installation_script.yml)
