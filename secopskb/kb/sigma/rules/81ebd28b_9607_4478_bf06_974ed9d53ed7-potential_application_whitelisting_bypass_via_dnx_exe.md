---
sigma_id: "81ebd28b-9607-4478-bf06-974ed9d53ed7"
title: "Potential Application Whitelisting Bypass via Dnx.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dnx_execute_csharp_code.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dnx_execute_csharp_code.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "81ebd28b-9607-4478-bf06-974ed9d53ed7"
  - "Potential Application Whitelisting Bypass via Dnx.EXE"
attack_technique_ids:
  - "T1218"
  - "T1027.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Application Whitelisting Bypass via Dnx.EXE

Detects the execution of Dnx.EXE. The Dnx utility allows for the execution of C# code.
Attackers might abuse this in order to bypass application whitelisting.

## Metadata

- Rule ID: 81ebd28b-9607-4478-bf06-974ed9d53ed7
- Status: test
- Level: medium
- Author: Beyu Denis, oscd.community
- Date: 2019-10-26
- Modified: 2024-04-24
- Source Path: rules/windows/process_creation/proc_creation_win_dnx_execute_csharp_code.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.004]]

## Detection

```yaml
selection:
  Image|endswith: \dnx.exe
condition: selection
```

## False Positives

- Legitimate use of dnx.exe by legitimate user

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Csi/
- https://enigma0x3.net/2016/11/17/bypassing-application-whitelisting-by-using-dnx-exe/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dnx_execute_csharp_code.yml)
