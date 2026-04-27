---
sigma_id: "4ac1f50b-3bd0-4968-902d-868b4647937e"
title: "DPAPI Domain Backup Key Extraction"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_dpapi_domain_backupkey_extraction.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_dpapi_domain_backupkey_extraction.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "4ac1f50b-3bd0-4968-902d-868b4647937e"
  - "DPAPI Domain Backup Key Extraction"
attack_technique_ids:
  - "T1003.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects tools extracting LSA secret DPAPI domain backup key from Domain Controllers

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]

## Detection

```yaml
selection:
  EventID: 4662
  ObjectType: SecretObject
  AccessMask: '0x2'
  ObjectName|contains: BCKUPKEY
condition: selection
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_dpapi_domain_backupkey_extraction.yml)
