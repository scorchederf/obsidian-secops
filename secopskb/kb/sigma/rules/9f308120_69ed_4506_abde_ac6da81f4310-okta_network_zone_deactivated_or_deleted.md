---
sigma_id: "9f308120-69ed-4506-abde-ac6da81f4310"
title: "Okta Network Zone Deactivated or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_network_zone_deactivated_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_network_zone_deactivated_or_deleted.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "9f308120-69ed-4506-abde-ac6da81f4310"
  - "Okta Network Zone Deactivated or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta Network Zone Deactivated or Deleted

Detects when an Network Zone is Deactivated or Deleted.

## Metadata

- Rule ID: 9f308120-69ed-4506-abde-ac6da81f4310
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-12
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_network_zone_deactivated_or_deleted.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  eventtype:
  - zone.deactivate
  - zone.delete
condition: selection
```

## False Positives

- Unknown

## References

- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_network_zone_deactivated_or_deleted.yml)
