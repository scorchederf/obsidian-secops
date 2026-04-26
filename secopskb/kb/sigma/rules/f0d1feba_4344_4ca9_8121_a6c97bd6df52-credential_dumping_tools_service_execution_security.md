---
sigma_id: "f0d1feba-4344-4ca9-8121-a6c97bd6df52"
title: "Credential Dumping Tools Service Execution - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_mal_creddumper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_mal_creddumper.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "f0d1feba-4344-4ca9-8121-a6c97bd6df52"
  - "Credential Dumping Tools Service Execution - Security"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Credential Dumping Tools Service Execution - Security

Detects well-known credential dumping tools execution via service execution events

## Metadata

- Rule ID: f0d1feba-4344-4ca9-8121-a6c97bd6df52
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Teymur Kheirkhabarov, Daniil Yugoslavskiy, oscd.community
- Date: 2017-03-05
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/security/win_security_mal_creddumper.yml

## Logsource

- definition: The 'System Security Extension' audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.004]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.005]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.006]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

### Software Tags

- S0005

## Detection

```yaml
selection:
  EventID: 4697
  ServiceFileName|contains:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_mal_creddumper.yml)
