---
sigma_id: "6e78f90f-0043-4a01-ac41-f97681613a66"
title: "OpenCanary - MSSQL Login Attempt Via Windows Authentication"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_mssql_login_winauth.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_mssql_login_winauth.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "6e78f90f-0043-4a01-ac41-f97681613a66"
  - "OpenCanary - MSSQL Login Attempt Via Windows Authentication"
attack_technique_ids:
  - "T1003"
  - "T1213"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# OpenCanary - MSSQL Login Attempt Via Windows Authentication

Detects instances where an MSSQL service on an OpenCanary node has had a login attempt using Windows Authentication.

## Metadata

- Rule ID: 6e78f90f-0043-4a01-ac41-f97681613a66
- Status: test
- Level: high
- Author: Security Onion Solutions
- Date: 2024-03-08
- Source Path: rules/application/opencanary/opencanary_mssql_login_winauth.yml

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
  logtype: 9002
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_mssql_login_winauth.yml)
