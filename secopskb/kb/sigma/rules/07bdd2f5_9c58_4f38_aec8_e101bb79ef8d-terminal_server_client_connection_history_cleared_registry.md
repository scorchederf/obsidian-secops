---
sigma_id: "07bdd2f5-9c58-4f38-aec8-e101bb79ef8d"
title: "Terminal Server Client Connection History Cleared - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_delete/registry_delete_mstsc_history_cleared.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_mstsc_history_cleared.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / registry_delete"
aliases:
  - "07bdd2f5-9c58-4f38-aec8-e101bb79ef8d"
  - "Terminal Server Client Connection History Cleared - Registry"
attack_technique_ids:
  - "T1070"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Terminal Server Client Connection History Cleared - Registry

Detects the deletion of registry keys containing the MSTSC connection history

## Metadata

- Rule ID: 07bdd2f5-9c58-4f38-aec8-e101bb79ef8d
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-10-19
- Modified: 2023-02-08
- Source Path: rules/windows/registry/registry_delete/registry_delete_mstsc_history_cleared.yml

## Logsource

- category: registry_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection1:
  EventType: DeleteValue
  TargetObject|contains: \Microsoft\Terminal Server Client\Default\MRU
selection2:
  EventType: DeleteKey
  TargetObject|contains: \Microsoft\Terminal Server Client\Servers\
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/remove-entries-from-remote-desktop-connection-computer
- http://woshub.com/how-to-clear-rdp-connections-history/
- https://www.trendmicro.com/en_us/research/23/a/vice-society-ransomware-group-targets-manufacturing-companies.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_mstsc_history_cleared.yml)
