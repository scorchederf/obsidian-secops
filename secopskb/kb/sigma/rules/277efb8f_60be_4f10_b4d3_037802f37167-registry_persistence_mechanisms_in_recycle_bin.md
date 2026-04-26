---
sigma_id: "277efb8f-60be-4f10-b4d3-037802f37167"
title: "Registry Persistence Mechanisms in Recycle Bin"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_persistence_recycle_bin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_persistence_recycle_bin.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "277efb8f-60be-4f10-b4d3-037802f37167"
  - "Registry Persistence Mechanisms in Recycle Bin"
attack_technique_ids:
  - "T1547"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Registry Persistence Mechanisms in Recycle Bin

Detects persistence registry keys for Recycle Bin

## Metadata

- Rule ID: 277efb8f-60be-4f10-b4d3-037802f37167
- Status: test
- Level: high
- Author: frack113
- Date: 2021-11-18
- Modified: 2022-12-06
- Source Path: rules/windows/registry/registry_event/registry_event_persistence_recycle_bin.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]]

## Detection

```yaml
selection_create:
  EventType: RenameKey
  NewName|contains: \CLSID\{645FF040-5081-101B-9F08-00AA002F954E}\shell\open
selection_set:
  EventType: SetValue
  TargetObject|contains: \CLSID\{645FF040-5081-101B-9F08-00AA002F954E}\shell\open\command\(Default)
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/vxunderground/VXUG-Papers/blob/751edb8d50f95bd7baa730adf2c6c3bb1b034276/The%20Persistence%20Series/Persistence%20via%20Recycle%20Bin/Persistence_via_Recycle_Bin.pdf
- https://persistence-info.github.io/Data/recyclebin.html
- https://www.hexacorn.com/blog/2018/05/28/beyond-good-ol-run-key-part-78-2/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_persistence_recycle_bin.yml)
