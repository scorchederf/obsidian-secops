---
sigma_id: "4976aa50-8f41-45c6-8b15-ab3fc10e79ed"
title: "Credential Dumping Tools Service Execution - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_mal_creddumper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_mal_creddumper.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "4976aa50-8f41-45c6-8b15-ab3fc10e79ed"
  - "Credential Dumping Tools Service Execution - System"
attack_technique_ids:
  - "T1003.001"
  - "T1003.002"
  - "T1003.004"
  - "T1003.005"
  - "T1003.006"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects well-known credential dumping tools execution via service execution events

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003005-cached-domain-credentials|T1003.005: Cached Domain Credentials]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003006-dcsync|T1003.006: DCSync]]
- [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

### Software Tags

- S0005

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7045
  ImagePath|contains:
  - cachedump
  - dumpsvc
  - fgexec
  - gsecdump
  - mimidrv
  - pwdump
  - servpw
condition: selection
```

## False Positives

- Legitimate Administrator using credential dumping tool for password recovery

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_mal_creddumper.yml)
