---
sigma_id: "adf876b3-f1f8-4aa9-a4e4-a64106feec06"
title: "Testing Usage of Uncommonly Used Port"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_test_netconnection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_test_netconnection.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "adf876b3-f1f8-4aa9-a4e4-a64106feec06"
  - "Testing Usage of Uncommonly Used Port"
attack_technique_ids:
  - "T1571"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Testing Usage of Uncommonly Used Port

Adversaries may communicate using a protocol and port paring that are typically not associated.
For example, HTTPS over port 8088(Citation: Symantec Elfin Mar 2019) or port 587(Citation: Fortinet Agent Tesla April 2018) as opposed to the traditional port 443.

## Metadata

- Rule ID: adf876b3-f1f8-4aa9-a4e4-a64106feec06
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-23
- Source Path: rules/windows/powershell/powershell_script/posh_ps_test_netconnection.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1571-non-standard_port|T1571]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Test-NetConnection
  - '-ComputerName '
  - '-port '
filter:
  ScriptBlockText|contains:
  - ' 443 '
  - ' 80 '
condition: selection and not filter
```

## False Positives

- Legitimate administrative script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1571/T1571.md#atomic-test-1---testing-usage-of-uncommonly-used-port-with-powershell
- https://learn.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection?view=windowsserver2022-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_test_netconnection.yml)
