---
sigma_id: "d6ce7ebd-260b-4323-9768-a9631c8d4db2"
title: "RestrictedAdminMode Registry Value Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_lsa_disablerestrictedadmin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_lsa_disablerestrictedadmin.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "d6ce7ebd-260b-4323-9768-a9631c8d4db2"
  - "RestrictedAdminMode Registry Value Tampering"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects changes to the "DisableRestrictedAdmin" registry value in order to disable or enable RestrictedAdmin mode.
RestrictedAdmin mode prevents the transmission of reusable credentials to the remote system to which you connect using Remote Desktop.
This prevents your credentials from being harvested during the initial connection process if the remote server has been compromise

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Detection

```yaml
selection:
  TargetObject|endswith: System\CurrentControlSet\Control\Lsa\DisableRestrictedAdmin
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/a8e3cf63e97b973a25903d3df9fd55da6252e564/atomics/T1112/T1112.md
- https://social.technet.microsoft.com/wiki/contents/articles/32905.remote-desktop-services-enable-restricted-admin-mode.aspx

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_lsa_disablerestrictedadmin.yml)
