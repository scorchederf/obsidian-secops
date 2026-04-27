---
sigma_id: "4fe17521-aef3-4e6a-9d6b-4a7c8de155a8"
title: "OpenCanary - GIT Clone Request"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_git_clone_request.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_git_clone_request.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "4fe17521-aef3-4e6a-9d6b-4a7c8de155a8"
  - "OpenCanary - GIT Clone Request"
attack_technique_ids:
  - "T1213"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects instances where a GIT service on an OpenCanary node has had Git Clone request.

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1213-data_from_information_repositories|T1213: Data from Information Repositories]]

## Detection

```yaml
selection:
  logtype: 16001
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_git_clone_request.yml)
