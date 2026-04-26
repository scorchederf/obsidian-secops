---
sigma_id: "3390fbef-c98d-4bdd-a863-d65ed7c610dd"
title: "New ODBC Driver Registered"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_odbc_driver_registered.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_odbc_driver_registered.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / registry_set"
aliases:
  - "3390fbef-c98d-4bdd-a863-d65ed7c610dd"
  - "New ODBC Driver Registered"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New ODBC Driver Registered

Detects the registration of a new ODBC driver.

## Metadata

- Rule ID: 3390fbef-c98d-4bdd-a863-d65ed7c610dd
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-23
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_odbc_driver_registered.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\ODBC\ODBCINST.INI\
  TargetObject|endswith: \Driver
filter_main_sqlserver:
  TargetObject|contains: \SQL Server\
  Details: '%WINDIR%\System32\SQLSRV32.dll'
filter_optional_office_access:
  TargetObject|contains: '\Microsoft Access '
  Details|startswith: C:\Progra
  Details|endswith: \ACEODBC.DLL
filter_optional_office_excel:
  TargetObject|contains: \Microsoft Excel Driver
  Details|startswith: C:\Progra
  Details|endswith: \ACEODBC.DLL
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Likely

## References

- https://www.hexacorn.com/blog/2020/08/23/odbcconf-lolbin-trifecta/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_odbc_driver_registered.yml)
