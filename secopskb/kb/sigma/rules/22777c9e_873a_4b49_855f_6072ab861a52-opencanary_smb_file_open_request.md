---
sigma_id: "22777c9e-873a-4b49-855f-6072ab861a52"
title: "OpenCanary - SMB File Open Request"
framework: "sigma"
generated: "true"
source_path: "rules/application/opencanary/opencanary_smb_file_open.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_smb_file_open.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "opencanary / application"
aliases:
  - "22777c9e-873a-4b49-855f-6072ab861a52"
  - "OpenCanary - SMB File Open Request"
attack_technique_ids:
  - "T1021"
  - "T1005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# OpenCanary - SMB File Open Request

Detects instances where an SMB service on an OpenCanary node has had a file open request.

## Metadata

- Rule ID: 22777c9e-873a-4b49-855f-6072ab861a52
- Status: test
- Level: high
- Author: Security Onion Solutions
- Date: 2024-03-08
- Source Path: rules/application/opencanary/opencanary_smb_file_open.yml

## Logsource

- category: application
- product: opencanary

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021]]
- [[kb/attack/techniques/T1005-data_from_local_system|T1005]]

## Detection

```yaml
selection:
  logtype: 5000
condition: selection
```

## False Positives

- Unlikely

## References

- https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
- https://github.com/thinkst/opencanary/blob/a0896adfcaf0328cfd5829fe10d2878c7445138e/opencanary/logger.py#L52

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/opencanary/opencanary_smb_file_open.yml)
