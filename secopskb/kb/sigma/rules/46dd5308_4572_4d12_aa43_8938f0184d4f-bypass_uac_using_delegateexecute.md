---
sigma_id: "46dd5308-4572-4d12-aa43-8938f0184d4f"
title: "Bypass UAC Using DelegateExecute"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_bypass_uac_using_delegateexecute.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_bypass_uac_using_delegateexecute.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "46dd5308-4572-4d12-aa43-8938f0184d4f"
  - "Bypass UAC Using DelegateExecute"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bypass UAC Using DelegateExecute

Bypasses User Account Control using a fileless method

## Metadata

- Rule ID: 46dd5308-4572-4d12-aa43-8938f0184d4f
- Status: test
- Level: high
- Author: frack113
- Date: 2022-01-05
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_bypass_uac_using_delegateexecute.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  TargetObject|endswith: \open\command\DelegateExecute
  Details: (Empty)
condition: selection
```

## False Positives

- Unknown

## Simulation

### Bypass UAC using sdclt DelegateExecute

- Atomic Test: [[kb/atomic/tests/3be891eb_4608_4173_87e8_78b494c029b7-bypass_uac_using_sdclt_delegateexecute|3be891eb-4608-4173-87e8-78b494c029b7]]
- atomic_guid: 3be891eb-4608-4173-87e8-78b494c029b7
- name: Bypass UAC using sdclt DelegateExecute
- technique: T1548.002
- type: atomic-red-team

## References

- https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nn-shobjidl_core-iexecutecommand
- https://devblogs.microsoft.com/oldnewthing/20100312-01/?p=14623
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1548.002/T1548.002.md#atomic-test-7---bypass-uac-using-sdclt-delegateexecute

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_bypass_uac_using_delegateexecute.yml)
