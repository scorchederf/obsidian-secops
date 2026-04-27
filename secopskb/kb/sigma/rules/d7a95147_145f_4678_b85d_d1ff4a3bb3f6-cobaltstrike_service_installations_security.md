---
sigma_id: "d7a95147-145f-4678-b85d-d1ff4a3bb3f6"
title: "CobaltStrike Service Installations - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_cobaltstrike_service_installs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_cobaltstrike_service_installs.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "d7a95147-145f-4678-b85d-d1ff4a3bb3f6"
  - "CobaltStrike Service Installations - Security"
attack_technique_ids:
  - "T1021.002"
  - "T1543.003"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects known malicious service installs that appear in cases in which a Cobalt Strike beacon elevates privileges or lateral movement

## Logsource

- definition: The 'System Security Extension' audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

## Detection

```yaml
event_id:
  EventID: 4697
selection1:
  ServiceFileName|contains|all:
  - ADMIN$
  - .exe
selection2:
  ServiceFileName|contains|all:
  - '%COMSPEC%'
  - start
  - powershell
selection3:
  ServiceFileName|contains: powershell -nop -w hidden -encodedcommand
selection4:
  ServiceFileName|base64offset|contains: 'IEX (New-Object Net.Webclient).DownloadString(''http://127.0.0.1:'
condition: event_id and 1 of selection*
```

## False Positives

- Unknown

## References

- https://www.sans.org/webcasts/119395
- https://www.crowdstrike.com/blog/getting-the-bacon-from-cobalt-strike-beacon/
- https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_cobaltstrike_service_installs.yml)
