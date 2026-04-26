---
sigma_id: "460479f3-80b7-42da-9c43-2cc1d54dbccd"
title: "Creation of a Local Hidden User Account by Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_add_local_hidden_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_add_local_hidden_user.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "460479f3-80b7-42da-9c43-2cc1d54dbccd"
  - "Creation of a Local Hidden User Account by Registry"
attack_technique_ids:
  - "T1136.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Creation of a Local Hidden User Account by Registry

Sysmon registry detection of a local hidden user account.

## Metadata

- Rule ID: 460479f3-80b7-42da-9c43-2cc1d54dbccd
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-05-03
- Modified: 2025-10-31
- Source Path: rules/windows/registry/registry_event/registry_event_add_local_hidden_user.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Detection

```yaml
selection:
  TargetObject|contains: \SAM\SAM\Domains\Account\Users\Names\
  TargetObject|endswith: $\(Default)
  Image|endswith: \lsass.exe
condition: selection
```

## False Positives

- Unknown

## Simulation

### Create Hidden User in Registry

- Atomic Test: [[kb/atomic/tests/173126b7_afe4_45eb_8680_fa9f6400431c-create_hidden_user_in_registry|173126b7-afe4-45eb-8680-fa9f6400431c]]
- atomic_guid: 173126b7-afe4-45eb-8680-fa9f6400431c
- name: Create Hidden User in Registry
- technique: T1564.002
- type: atomic-red-team

## References

- https://twitter.com/SBousseaden/status/1387530414185664538

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_add_local_hidden_user.yml)
