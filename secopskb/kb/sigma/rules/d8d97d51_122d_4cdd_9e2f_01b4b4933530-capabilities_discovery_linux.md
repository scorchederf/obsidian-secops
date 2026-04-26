---
sigma_id: "d8d97d51-122d-4cdd-9e2f-01b4b4933530"
title: "Capabilities Discovery - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_capa_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_capa_discovery.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "d8d97d51-122d-4cdd-9e2f-01b4b4933530"
  - "Capabilities Discovery - Linux"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Capabilities Discovery - Linux

Detects usage of "getcap" binary. This is often used during recon activity to determine potential binaries that can be abused as GTFOBins or other.

## Metadata

- Rule ID: d8d97d51-122d-4cdd-9e2f-01b4b4933530
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-28
- Modified: 2026-01-24
- Source Path: rules/linux/process_creation/proc_creation_lnx_capa_discovery.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
selection:
  Image|endswith: /getcap
  CommandLine|contains: ' -r '
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SaiSathvik1/Linux-Privilege-Escalation-Notes
- https://github.com/carlospolop/PEASS-ng
- https://github.com/diego-treitos/linux-smart-enumeration

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_capa_discovery.yml)
