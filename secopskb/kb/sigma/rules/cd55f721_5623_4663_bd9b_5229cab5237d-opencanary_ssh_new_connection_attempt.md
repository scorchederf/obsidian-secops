---
sigma_id: "cd55f721-5623-4663-bd9b-5229cab5237d"
title: "OpenCanary - SSH New Connection Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_ssh_new_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_ssh_new_connection.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "cd55f721-5623-4663-bd9b-5229cab5237d"
  - "OpenCanary - SSH New Connection Attempt"
attack_technique_ids:
  - "T1133"
  - "T1021"
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects instances where an SSH service on an OpenCanary node has had a connection attempt.

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133: External Remote Services]]
- [[kb/attack/techniques/T1021-remote_services|T1021: Remote Services]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078: Valid Accounts]]

## Detection

```yaml
selection:
  logtype: 4000
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_ssh_new_connection.yml)
