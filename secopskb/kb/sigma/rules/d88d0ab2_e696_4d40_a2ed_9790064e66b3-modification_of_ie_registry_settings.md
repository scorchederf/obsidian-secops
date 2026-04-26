---
sigma_id: "d88d0ab2-e696-4d40-a2ed-9790064e66b3"
title: "Modification of IE Registry Settings"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_ie.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_ie.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "windows / registry_set"
aliases:
  - "d88d0ab2-e696-4d40-a2ed-9790064e66b3"
  - "Modification of IE Registry Settings"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Modification of IE Registry Settings

Detects modification of the registry settings used for Internet Explorer and other Windows components that use these settings. An attacker can abuse this registry key to add a domain to the trusted sites Zone or insert JavaScript for persistence

## Metadata

- Rule ID: d88d0ab2-e696-4d40-a2ed-9790064e66b3
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-22
- Modified: 2025-10-22
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_ie.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_domains:
  TargetObject|contains: \Software\Microsoft\Windows\CurrentVersion\Internet Settings
filter_main_dword:
  Details|startswith: DWORD
filter_main_null:
  Details: null
filter_main_office:
  Details:
  - 'Cookie:'
  - 'Visited:'
  - (Empty)
filter_main_path:
  TargetObject|contains:
  - \Cache
  - \ZoneMap
  - \WpadDecision
filter_main_binary:
  Details: Binary Data
filter_optional_accepted_documents:
  TargetObject|contains: \Software\Microsoft\Windows\CurrentVersion\Internet Settings\Accepted
    Documents
condition: selection_domains and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1112/T1112.md#atomic-test-4---add-domain-to-trusted-sites-zone
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1112/T1112.md#atomic-test-5---javascript-in-registry

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_ie.yml)
