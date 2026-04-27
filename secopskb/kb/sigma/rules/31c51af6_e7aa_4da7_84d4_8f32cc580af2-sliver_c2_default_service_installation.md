---
sigma_id: "31c51af6-e7aa-4da7-84d4-8f32cc580af2"
title: "Sliver C2 Default Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_sliver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_sliver.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "31c51af6-e7aa-4da7-84d4-8f32cc580af2"
  - "Sliver C2 Default Service Installation"
attack_technique_ids:
  - "T1543.003"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects known malicious service installation that appear in cases in which a Sliver implants execute the PsExec commands

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

## Detection

```yaml
selection_eid:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_service_1:
  ImagePath|re: ^[a-zA-Z]:\\windows\\temp\\[a-zA-Z0-9]{10}\.exe
selection_service_2:
  ServiceName:
  - Sliver
  - Sliver implant
condition: selection_eid and 1 of selection_service_*
```

## False Positives

- Unknown

## References

- https://github.com/BishopFox/sliver/blob/79f2d48fcdfc2bee4713b78d431ea4b27f733f30/client/command/commands.go#L1231
- https://www.microsoft.com/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-for-emerging-command-and-control-frameworks/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_sliver.yml)
