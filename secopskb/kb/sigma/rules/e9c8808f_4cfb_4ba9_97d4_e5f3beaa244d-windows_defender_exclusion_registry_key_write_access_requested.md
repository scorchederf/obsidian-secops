---
sigma_id: "e9c8808f-4cfb-4ba9-97d4-e5f3beaa244d"
title: "Windows Defender Exclusion Registry Key - Write Access Requested"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_windows_defender_exclusions_write_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_windows_defender_exclusions_write_access.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "e9c8808f-4cfb-4ba9-97d4-e5f3beaa244d"
  - "Windows Defender Exclusion Registry Key - Write Access Requested"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Exclusion Registry Key - Write Access Requested

Detects write access requests to the Windows Defender exclusions registry keys. This could be an indication of an attacker trying to request a handle or access the object to write new exclusions in order to bypass security.

## Metadata

- Rule ID: e9c8808f-4cfb-4ba9-97d4-e5f3beaa244d
- Status: test
- Level: medium
- Author: @BarryShooshooga, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-10-26
- Modified: 2023-11-11
- Source Path: rules/windows/builtin/security/win_security_windows_defender_exclusions_write_access.yml

## Logsource

- definition: Requirements: Audit Policy : Security Settings/Local Policies/Audit Policy, Registry System Access Control (SACL): Auditing/User
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  AccessList|contains:
  - '%%4417'
  - '%%4418'
  EventID:
  - 4656
  - 4663
  ObjectName|contains: \Microsoft\Windows Defender\Exclusions\
condition: selection
```

## False Positives

- Unknown

## References

- https://www.bleepingcomputer.com/news/security/gootkit-malware-bypasses-windows-defender-by-setting-path-exclusions/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_windows_defender_exclusions_write_access.yml)
