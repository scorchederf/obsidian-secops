---
sigma_id: "252902e3-5830-4cf6-bf21-c22083dfd5cf"
title: "Possible Impacket SecretDump Remote Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_impacket_secretdump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_impacket_secretdump.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "252902e3-5830-4cf6-bf21-c22083dfd5cf"
  - "Possible Impacket SecretDump Remote Activity"
attack_technique_ids:
  - "T1003.002"
  - "T1003.004"
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Possible Impacket SecretDump Remote Activity

Detect AD credential dumping using impacket secretdump HKTL

## Metadata

- Rule ID: 252902e3-5830-4cf6-bf21-c22083dfd5cf
- Status: test
- Level: high
- Author: Samir Bousseaden, wagga
- Date: 2019-04-03
- Modified: 2022-08-11
- Source Path: rules/windows/builtin/security/win_security_impacket_secretdump.yml

## Logsource

- definition: The advanced audit policy setting "Object Access > Audit Detailed File Share" must be configured for Success/Failure
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.004]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection:
  EventID: 5145
  ShareName: \\\\\*\\ADMIN$
  RelativeTargetName|contains|all:
  - SYSTEM32\
  - .tmp
condition: selection
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20230329153811/https://blog.menasec.net/2019/02/threat-huting-10-impacketsecretdump.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_impacket_secretdump.yml)
