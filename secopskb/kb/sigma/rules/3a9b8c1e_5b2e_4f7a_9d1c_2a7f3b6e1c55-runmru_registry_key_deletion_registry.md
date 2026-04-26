---
sigma_id: "3a9b8c1e-5b2e-4f7a-9d1c-2a7f3b6e1c55"
title: "RunMRU Registry Key Deletion - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_delete/registry_delete_runmru.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_runmru.yml"
build_date: "2026-04-26 17:03:22"
status: "experimental"
level: "high"
logsource: "windows / registry_delete"
aliases:
  - "3a9b8c1e-5b2e-4f7a-9d1c-2a7f3b6e1c55"
  - "RunMRU Registry Key Deletion - Registry"
attack_technique_ids:
  - "T1070.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# RunMRU Registry Key Deletion - Registry

Detects attempts to delete the RunMRU registry key, which stores the history of commands executed via the run dialog.
In the clickfix techniques, the phishing lures instruct users to open a run dialog through (Win + R) and execute malicious commands.
Adversaries may delete this key to cover their tracks after executing commands.

## Metadata

- Rule ID: 3a9b8c1e-5b2e-4f7a-9d1c-2a7f3b6e1c55
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-09-25
- Source Path: rules/windows/registry/registry_delete/registry_delete_runmru.yml

## Logsource

- category: registry_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
condition: selection
```

## False Positives

- Unknown

## References

- https://www.zscaler.com/blogs/security-research/coldriver-updates-arsenal-baitswitch-and-simplefix

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_runmru.yml)
