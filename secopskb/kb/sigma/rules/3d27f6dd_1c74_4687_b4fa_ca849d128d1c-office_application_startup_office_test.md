---
sigma_id: "3d27f6dd-1c74-4687-b4fa-ca849d128d1c"
title: "Office Application Startup - Office Test"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_office_test_regadd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_office_test_regadd.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / registry_event"
aliases:
  - "3d27f6dd-1c74-4687-b4fa-ca849d128d1c"
  - "Office Application Startup - Office Test"
attack_technique_ids:
  - "T1137.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Office Application Startup - Office Test

Detects the addition of office test registry that allows a user to specify an arbitrary DLL that will be executed every time an Office application is started

## Metadata

- Rule ID: 3d27f6dd-1c74-4687-b4fa-ca849d128d1c
- Status: test
- Level: medium
- Author: omkar72
- Date: 2020-10-25
- Modified: 2023-11-08
- Source Path: rules/windows/registry/registry_event/registry_event_office_test_regadd.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137.002]]

## Detection

```yaml
selection:
  TargetObject|contains: \Software\Microsoft\Office test\Special\Perf
condition: selection
```

## False Positives

- Unlikely

## References

- https://unit42.paloaltonetworks.com/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_office_test_regadd.yml)
