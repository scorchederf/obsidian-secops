---
sigma_id: "3ec9a16d-0b4f-4967-9542-ebf38ceac7dd"
title: "OpenCanary - MSSQL Login Attempt Via SQLAuth"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_mssql_login_sqlauth.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_mssql_login_sqlauth.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "3ec9a16d-0b4f-4967-9542-ebf38ceac7dd"
  - "OpenCanary - MSSQL Login Attempt Via SQLAuth"
attack_technique_ids:
  - "T1003"
  - "T1213"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# OpenCanary - MSSQL Login Attempt Via SQLAuth

Detects instances where an MSSQL service on an OpenCanary node has had a login attempt using SQLAuth.

## Metadata

- Rule ID: 3ec9a16d-0b4f-4967-9542-ebf38ceac7dd
- Status: test
- Level: high
- Author: Security Onion Solutions
- Date: 2024-03-08
- Source Path: rules/application/opencanary/opencanary_mssql_login_sqlauth.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]
- [[kb/attack/techniques/T1213-data_from_information_repositories|T1213]]

## Detection

```yaml
selection:
  logtype: 9001
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_mssql_login_sqlauth.yml)
