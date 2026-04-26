---
sigma_id: "15434e33-5027-4914-88d5-3d4145ec25a9"
title: "Potential Product Reconnaissance Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_recon_product.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_product.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "15434e33-5027-4914-88d5-3d4145ec25a9"
  - "Potential Product Reconnaissance Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Product Reconnaissance Via Wmic.EXE

Detects the execution of WMIC in order to get a list of firewall and antivirus products

## Metadata

- Rule ID: 15434e33-5027-4914-88d5-3d4145ec25a9
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali
- Date: 2023-02-14
- Modified: 2025-10-22
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_recon_product.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_img:
- Image|endswith: \wmic.exe
- OriginalFileName: wmic.exe
selection_cli:
  CommandLine|contains: Product
filter_main_call_operations:
  CommandLine|contains:
  - ' uninstall'
  - ' install'
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2023/03/06/2022-year-in-review/
- https://www.yeahhub.com/list-installed-programs-version-path-windows/
- https://learn.microsoft.com/en-us/answers/questions/253555/software-list-inventory-wmic-product

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_product.yml)
