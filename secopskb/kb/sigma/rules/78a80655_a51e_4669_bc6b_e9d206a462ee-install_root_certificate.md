---
sigma_id: "78a80655-a51e-4669-bc6b-e9d206a462ee"
title: "Install Root Certificate"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_install_root_certificate.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_install_root_certificate.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "78a80655-a51e-4669-bc6b-e9d206a462ee"
  - "Install Root Certificate"
attack_technique_ids:
  - "T1553.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Install Root Certificate

Detects installation of new certificate on the system which attackers may use to avoid warnings when connecting to controlled web servers or C2s

## Metadata

- Rule ID: 78a80655-a51e-4669-bc6b-e9d206a462ee
- Status: test
- Level: low
- Author: Ömer Günal, oscd.community
- Date: 2020-10-05
- Modified: 2022-07-07
- Source Path: rules/linux/process_creation/proc_creation_lnx_install_root_certificate.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Detection

```yaml
selection:
  Image|endswith:
  - /update-ca-certificates
  - /update-ca-trust
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.004/T1553.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_install_root_certificate.yml)
