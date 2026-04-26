---
sigma_id: "46a68649-f218-4f86-aea1-16a759d81820"
title: "Windows Defender Exclusion List Modified"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_windows_defender_exclusions_registry_modified.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_windows_defender_exclusions_registry_modified.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "46a68649-f218-4f86-aea1-16a759d81820"
  - "Windows Defender Exclusion List Modified"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Exclusion List Modified

Detects modifications to the Windows Defender exclusion registry key. This could indicate a potentially suspicious or even malicious activity by an attacker trying to add a new exclusion in order to bypass security.

## Metadata

- Rule ID: 46a68649-f218-4f86-aea1-16a759d81820
- Status: test
- Level: medium
- Author: @BarryShooshooga
- Date: 2019-10-26
- Modified: 2023-11-11
- Source Path: rules/windows/builtin/security/win_security_windows_defender_exclusions_registry_modified.yml

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
  EventID: 4657
  ObjectName|contains: \Microsoft\Windows Defender\Exclusions\
condition: selection
```

## False Positives

- Intended exclusions by administrators

## References

- https://www.bleepingcomputer.com/news/security/gootkit-malware-bypasses-windows-defender-by-setting-path-exclusions/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_windows_defender_exclusions_registry_modified.yml)
