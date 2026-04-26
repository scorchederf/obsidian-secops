---
sigma_id: "1c8e96cd-2bed-487d-9de0-b46c90cade56"
title: "Potential Qakbot Registry Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_malware_qakbot_registry.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_malware_qakbot_registry.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "1c8e96cd-2bed-487d-9de0-b46c90cade56"
  - "Potential Qakbot Registry Activity"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Qakbot Registry Activity

Detects a registry key used by IceID in a campaign that distributes malicious OneNote files

## Metadata

- Rule ID: 1c8e96cd-2bed-487d-9de0-b46c90cade56
- Status: test
- Level: high
- Author: Hieu Tran
- Date: 2023-03-13
- Source Path: rules/windows/registry/registry_event/registry_event_malware_qakbot_registry.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Software\firm\soft\Name
condition: selection
```

## False Positives

- Unknown

## References

- https://www.zscaler.com/blogs/security-research/onenote-growing-threat-malware-distribution

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_malware_qakbot_registry.yml)
