---
sigma_id: "674202d0-b22a-4af4-ae5f-2eda1f3da1af"
title: "Bypass UAC Using Event Viewer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_bypass_uac_using_eventviewer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_bypass_uac_using_eventviewer.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "674202d0-b22a-4af4-ae5f-2eda1f3da1af"
  - "Bypass UAC Using Event Viewer"
attack_technique_ids:
  - "T1547.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bypass UAC Using Event Viewer

Bypasses User Account Control using Event Viewer and a relevant Windows Registry modification

## Metadata

- Rule ID: 674202d0-b22a-4af4-ae5f-2eda1f3da1af
- Status: test
- Level: high
- Author: frack113
- Date: 2022-01-05
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_bypass_uac_using_eventviewer.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.010]]

## Detection

```yaml
selection:
  TargetObject|endswith: _Classes\mscfile\shell\open\command\(Default)
filter:
  Details|startswith: '%SystemRoot%\system32\mmc.exe "%1" %'
condition: selection and not filter
```

## False Positives

- Unknown

## Simulation

### Bypass UAC using Event Viewer (cmd)

- Atomic Test: [[kb/atomic/tests/5073adf8_9a50_4bd9_b298_a9bd2ead8af9-bypass_uac_using_event_viewer_cmd|5073adf8-9a50-4bd9-b298-a9bd2ead8af9]]
- atomic_guid: 5073adf8-9a50-4bd9-b298-a9bd2ead8af9
- name: Bypass UAC using Event Viewer (cmd)
- technique: T1548.002
- type: atomic-red-team

## References

- https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1548.002/T1548.002.md#atomic-test-1---bypass-uac-using-event-viewer-cmd

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_bypass_uac_using_eventviewer.yml)
