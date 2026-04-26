---
sigma_id: "968eef52-9cff-4454-8992-1e74b9cbad6c"
title: "Reconnaissance Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_net_recon_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_net_recon_activity.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "968eef52-9cff-4454-8992-1e74b9cbad6c"
  - "Reconnaissance Activity"
attack_technique_ids:
  - "T1087.002"
  - "T1069.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Reconnaissance Activity

Detects activity as "net user administrator /domain" and "net group domain admins /domain"

## Metadata

- Rule ID: 968eef52-9cff-4454-8992-1e74b9cbad6c
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Jack Croock (method), Jonhnathan Ribeiro (improvements), oscd.community
- Date: 2017-03-07
- Modified: 2022-08-22
- Source Path: rules/windows/builtin/security/win_security_susp_net_recon_activity.yml

## Logsource

- definition: The volume of Event ID 4661 is high on Domain Controllers and therefore "Audit SAM" and "Audit Kernel Object" advanced audit policy settings are not configured in the recommendations for server systems
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]
- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]

### Software Tags

- S0039

## Detection

```yaml
selection:
  EventID: 4661
  AccessMask: '0x2d'
  ObjectType:
  - SAM_USER
  - SAM_GROUP
  ObjectName|startswith: S-1-5-21-
  ObjectName|endswith:
  - '-500'
  - '-512'
condition: selection
```

## False Positives

- Administrator activity

## References

- https://findingbad.blogspot.de/2017/01/hunting-what-does-it-look-like.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_net_recon_activity.yml)
