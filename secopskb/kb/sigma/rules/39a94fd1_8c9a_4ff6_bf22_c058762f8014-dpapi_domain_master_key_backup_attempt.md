---
sigma_id: "39a94fd1-8c9a-4ff6-bf22-c058762f8014"
title: "DPAPI Domain Master Key Backup Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_dpapi_domain_masterkey_backup_attempt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_dpapi_domain_masterkey_backup_attempt.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "39a94fd1-8c9a-4ff6-bf22-c058762f8014"
  - "DPAPI Domain Master Key Backup Attempt"
attack_technique_ids:
  - "T1003.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DPAPI Domain Master Key Backup Attempt

Detects anyone attempting a backup for the DPAPI Master Key. This events gets generated at the source and not the Domain Controller.

## Metadata

- Rule ID: 39a94fd1-8c9a-4ff6-bf22-c058762f8014
- Status: test
- Level: medium
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-08-10
- Modified: 2023-03-15
- Source Path: rules/windows/builtin/security/win_security_dpapi_domain_masterkey_backup_attempt.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.004]]

## Detection

```yaml
selection:
  EventID: 4692
condition: selection
```

## False Positives

- If a computer is a member of a domain, DPAPI has a backup mechanism to allow unprotection of the data. Which will trigger this event.

## References

- https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_dpapi_domain_masterkey_backup_attempt.yml)
