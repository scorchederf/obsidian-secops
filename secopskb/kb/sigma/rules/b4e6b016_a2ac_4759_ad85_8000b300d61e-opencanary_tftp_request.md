---
sigma_id: "b4e6b016-a2ac-4759-ad85-8000b300d61e"
title: "OpenCanary - TFTP Request"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_tftp_request.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_tftp_request.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "b4e6b016-a2ac-4759-ad85-8000b300d61e"
  - "OpenCanary - TFTP Request"
attack_technique_ids:
  - "T1041"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# OpenCanary - TFTP Request

Detects instances where a TFTP service on an OpenCanary node has had a request.

## Metadata

- Rule ID: b4e6b016-a2ac-4759-ad85-8000b300d61e
- Status: test
- Level: high
- Author: Security Onion Solutions
- Date: 2024-03-08
- Source Path: rules/application/opencanary/opencanary_tftp_request.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1041-exfiltration_over_c2_channel|T1041]]

## Detection

```yaml
selection:
  logtype: 10001
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_tftp_request.yml)
