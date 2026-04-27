---
sigma_id: "aa1697b7-d611-4f9a-9cb2-5125b4ccfd5c"
title: "Password Dumper Activity on LSASS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_lsass_dump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_lsass_dump.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "aa1697b7-d611-4f9a-9cb2-5125b4ccfd5c"
  - "Password Dumper Activity on LSASS"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects process handle on LSASS process with certain access mask and object type SAM_DOMAIN

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection:
  EventID: 4656
  ProcessName|endswith: \lsass.exe
  AccessMask: '0x705'
  ObjectType: SAM_DOMAIN
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/jackcr/status/807385668833968128

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_lsass_dump.yml)
