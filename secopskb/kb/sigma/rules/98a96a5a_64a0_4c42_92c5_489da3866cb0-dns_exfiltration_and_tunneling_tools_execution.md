---
sigma_id: "98a96a5a-64a0-4c42-92c5-489da3866cb0"
title: "DNS Exfiltration and Tunneling Tools Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dns_exfiltration_tools_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dns_exfiltration_tools_execution.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "98a96a5a-64a0-4c42-92c5-489da3866cb0"
  - "DNS Exfiltration and Tunneling Tools Execution"
attack_technique_ids:
  - "T1048.001"
  - "T1071.004"
  - "T1132.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DNS Exfiltration and Tunneling Tools Execution

Well-known DNS Exfiltration tools execution

## Metadata

- Rule ID: 98a96a5a-64a0-4c42-92c5-489da3866cb0
- Status: test
- Level: high
- Author: Daniil Yugoslavskiy, oscd.community
- Date: 2019-10-24
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_dns_exfiltration_tools_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.001]]
- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.004]]
- [[kb/attack/techniques/T1132-data_encoding|T1132.001]]

## Detection

```yaml
selection:
- Image|endswith: \iodine.exe
- Image|contains: \dnscat2
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/iagox86/dnscat2
- https://github.com/yarrick/iodine

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dns_exfiltration_tools_execution.yml)
