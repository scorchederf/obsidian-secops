---
sigma_id: "5a5152f1-463f-436b-b2f5-8eceb3964b42"
title: "Displaying Hidden Files Feature Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_hide_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hide_file.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "5a5152f1-463f-436b-b2f5-8eceb3964b42"
  - "Displaying Hidden Files Feature Disabled"
attack_technique_ids:
  - "T1564.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Displaying Hidden Files Feature Disabled

Detects modifications to the "Hidden" and "ShowSuperHidden" explorer registry values in order to disable showing of hidden files and system files.
This technique is abused by several malware families to hide their files from normal users.

## Metadata

- Rule ID: 5a5152f1-463f-436b-b2f5-8eceb3964b42
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-04-02
- Modified: 2024-03-26
- Source Path: rules/windows/registry/registry_set/registry_set_hide_file.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.001]]

## Detection

```yaml
selection:
  TargetObject|endswith:
  - \Microsoft\Windows\CurrentVersion\Explorer\Advanced\ShowSuperHidden
  - \Microsoft\Windows\CurrentVersion\Explorer\Advanced\Hidden
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.001/T1564.001.md#atomic-test-8---hide-files-through-registry

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hide_file.yml)
