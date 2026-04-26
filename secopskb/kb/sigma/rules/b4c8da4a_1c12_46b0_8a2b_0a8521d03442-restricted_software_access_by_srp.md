---
sigma_id: "b4c8da4a-1c12-46b0-8a2b-0a8521d03442"
title: "Restricted Software Access By SRP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/microsoft_windows_software_restriction_policies/win_software_restriction_policies_block.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/microsoft_windows_software_restriction_policies/win_software_restriction_policies_block.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / application"
aliases:
  - "b4c8da4a-1c12-46b0-8a2b-0a8521d03442"
  - "Restricted Software Access By SRP"
attack_technique_ids:
  - "T1072"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Restricted Software Access By SRP

Detects restricted access to applications by the Software Restriction Policies (SRP) policy

## Metadata

- Rule ID: b4c8da4a-1c12-46b0-8a2b-0a8521d03442
- Status: test
- Level: high
- Author: frack113
- Date: 2023-01-12
- Source Path: rules/windows/builtin/application/microsoft_windows_software_restriction_policies/win_software_restriction_policies_block.yml

## Logsource

- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1072-software_deployment_tools|T1072]]

## Detection

```yaml
selection:
  Provider_Name: Microsoft-Windows-SoftwareRestrictionPolicies
  EventID:
  - 865
  - 866
  - 867
  - 868
  - 882
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows-server/identity/software-restriction-policies/software-restriction-policies
- https://github.com/nasbench/EVTX-ETW-Resources/blob/7a806a148b3d9d381193d4a80356016e6e8b1ee8/ETWEventsList/CSV/Windows11/22H2/W11_22H2_Pro_20220920_22621.382/Providers/Microsoft-Windows-AppXDeployment-Server.csv

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/microsoft_windows_software_restriction_policies/win_software_restriction_policies_block.yml)
