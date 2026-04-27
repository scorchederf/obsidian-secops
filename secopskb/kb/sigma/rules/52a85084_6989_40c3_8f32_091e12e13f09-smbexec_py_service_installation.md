---
sigma_id: "52a85084-6989-40c3-8f32-091e12e13f09"
title: "smbexec.py Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_hack_smbexec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_hack_smbexec.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "52a85084-6989-40c3-8f32-091e12e13f09"
  - "smbexec.py Service Installation"
attack_technique_ids:
  - "T1021.002"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of smbexec.py tool by detecting a specific service installation

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
- [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

## Detection

```yaml
selection_eid:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_service_name:
  ServiceName: BTOBTO
selection_service_image:
  ImagePath|contains:
  - '.bat & del '
  - __output 2^>^&1 >
condition: selection_eid and 1 of selection_service_*
```

## False Positives

- Unknown

## References

- https://blog.ropnop.com/using-credentials-to-own-windows-boxes-part-2-psexec-and-services/
- https://github.com/fortra/impacket/blob/33058eb2fde6976ea62e04bc7d6b629d64d44712/examples/smbexec.py#L286-L296
- https://github.com/fortra/impacket/blob/edef71f17bc1240f9f8c957bbda98662951ac3ec/examples/smbexec.py#L60

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_hack_smbexec.yml)
