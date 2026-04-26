---
sigma_id: "e0813366-0407-449a-9869-a2db1119dc41"
title: "Suspicious Printer Driver Empty Manufacturer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_susp_printer_driver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_printer_driver.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "e0813366-0407-449a-9869-a2db1119dc41"
  - "Suspicious Printer Driver Empty Manufacturer"
attack_technique_ids:
  - "T1574"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Printer Driver Empty Manufacturer

Detects a suspicious printer driver installation with an empty Manufacturer value

## Metadata

- Rule ID: e0813366-0407-449a-9869-a2db1119dc41
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2020-07-01
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_susp_printer_driver.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574]]

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - \Control\Print\Environments\Windows x64\Drivers
  - \Manufacturer
  Details: (Empty)
filter_cutepdf:
  TargetObject|contains: \CutePDF Writer v4.0\
filter_vnc:
  TargetObject|contains:
  - \VNC Printer (PS)\
  - \VNC Printer (UD)\
filter_pdf24:
  TargetObject|contains: \Version-3\PDF24\
condition: selection and not 1 of filter_*
```

## False Positives

- Alerts on legitimate printer drivers that do not set any more details in the Manufacturer value

## References

- https://twitter.com/SBousseaden/status/1410545674773467140

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_printer_driver.yml)
