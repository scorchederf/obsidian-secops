---
sigma_id: "b8b1b304-a60f-4999-9a6e-c547bde03ffd"
title: "DeviceCredentialDeployment Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_device_credential_deployment.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_device_credential_deployment.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b8b1b304-a60f-4999-9a6e-c547bde03ffd"
  - "DeviceCredentialDeployment Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DeviceCredentialDeployment Execution

Detects the execution of DeviceCredentialDeployment to hide a process from view.

## Metadata

- Rule ID: b8b1b304-a60f-4999-9a6e-c547bde03ffd
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-19
- Source Path: rules/windows/process_creation/proc_creation_win_device_credential_deployment.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|endswith: \DeviceCredentialDeployment.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/LOLBAS-Project/LOLBAS/pull/147

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_device_credential_deployment.yml)
