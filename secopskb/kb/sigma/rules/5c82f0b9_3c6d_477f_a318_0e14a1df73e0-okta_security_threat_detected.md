---
sigma_id: "5c82f0b9-3c6d-477f-a318-0e14a1df73e0"
title: "Okta Security Threat Detected"
framework: "sigma"
generated: "true"
source_path: "rules/identity/okta/okta_security_threat_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_security_threat_detected.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "okta / okta"
aliases:
  - "5c82f0b9-3c6d-477f-a318-0e14a1df73e0"
  - "Okta Security Threat Detected"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Okta Security Threat Detected

Detects when an security threat is detected in Okta.

## Metadata

- Rule ID: 5c82f0b9-3c6d-477f-a318-0e14a1df73e0
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-09-12
- Modified: 2022-10-09
- Source Path: rules/identity/okta/okta_security_threat_detected.yml

## Logsource

- product: okta
- service: okta

## Detection

```yaml
selection:
  eventtype: security.threat.detected
condition: selection
```

## False Positives

- Unknown

## References

- https://okta.github.io/okta-help/en/prod/Content/Topics/Security/threat-insight/configure-threatinsight-system-log.htm
- https://developer.okta.com/docs/reference/api/system-log/
- https://developer.okta.com/docs/reference/api/event-types/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/okta/okta_security_threat_detected.yml)
