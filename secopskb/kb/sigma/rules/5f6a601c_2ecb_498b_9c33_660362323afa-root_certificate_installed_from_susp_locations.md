---
sigma_id: "5f6a601c-2ecb-498b-9c33-660362323afa"
title: "Root Certificate Installed From Susp Locations"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_import_cert_susp_locations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_import_cert_susp_locations.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5f6a601c-2ecb-498b-9c33-660362323afa"
  - "Root Certificate Installed From Susp Locations"
attack_technique_ids:
  - "T1553.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Root Certificate Installed From Susp Locations

Adversaries may install a root certificate on a compromised system to avoid warnings when connecting to adversary controlled web servers.

## Metadata

- Rule ID: 5f6a601c-2ecb-498b-9c33-660362323afa
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-09
- Modified: 2023-01-16
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_import_cert_susp_locations.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - Import-Certificate
  - ' -FilePath '
  - Cert:\LocalMachine\Root
  CommandLine|contains:
  - \AppData\Local\Temp\
  - :\Windows\TEMP\
  - \Desktop\
  - \Downloads\
  - \Perflogs\
  - :\Users\Public\
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.microsoft.com/security/blog/2022/09/07/profiling-dev-0270-phosphorus-ransomware-operations/
- https://learn.microsoft.com/en-us/powershell/module/pki/import-certificate?view=windowsserver2022-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_import_cert_susp_locations.yml)
