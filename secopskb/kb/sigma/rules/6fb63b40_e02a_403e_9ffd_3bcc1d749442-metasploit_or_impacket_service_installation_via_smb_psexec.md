---
sigma_id: "6fb63b40-e02a-403e-9ffd-3bcc1d749442"
title: "Metasploit Or Impacket Service Installation Via SMB PsExec"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_metasploit_or_impacket_smb_psexec_service_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_metasploit_or_impacket_smb_psexec_service_install.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "6fb63b40-e02a-403e-9ffd-3bcc1d749442"
  - "Metasploit Or Impacket Service Installation Via SMB PsExec"
attack_technique_ids:
  - "T1021.002"
  - "T1570"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects usage of Metasploit SMB PsExec (exploit/windows/smb/psexec) and Impacket psexec.py by triggering on specific service installation

## Logsource

- definition: The 'System Security Extension' audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
- [[kb/attack/techniques/T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]
- [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

## Detection

```yaml
selection:
  EventID: 4697
  ServiceFileName|re: ^%systemroot%\\[a-zA-Z]{8}\.exe$
  ServiceName|re: (^[a-zA-Z]{4}$)|(^[a-zA-Z]{8}$)|(^[a-zA-Z]{16}$)
  ServiceStartType: 3
  ServiceType: '0x10'
filter:
  ServiceName: PSEXESVC
condition: selection and not filter
```

## False Positives

- Possible, different agents with a 8 character binary and a 4, 8 or 16 character service name

## References

- https://bczyz1.github.io/2021/01/30/psexec.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_metasploit_or_impacket_smb_psexec_service_install.yml)
