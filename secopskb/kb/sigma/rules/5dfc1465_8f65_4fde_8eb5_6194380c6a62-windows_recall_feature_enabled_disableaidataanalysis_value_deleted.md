---
sigma_id: "5dfc1465-8f65-4fde-8eb5-6194380c6a62"
title: "Windows Recall Feature Enabled - DisableAIDataAnalysis Value Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_delete/registry_delete_enable_windows_recall.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_enable_windows_recall.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / registry_delete"
aliases:
  - "5dfc1465-8f65-4fde-8eb5-6194380c6a62"
  - "Windows Recall Feature Enabled - DisableAIDataAnalysis Value Deleted"
attack_technique_ids:
  - "T1113"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Recall Feature Enabled - DisableAIDataAnalysis Value Deleted

Detects the enabling of the Windows Recall feature via registry manipulation. Windows Recall can be enabled by deleting the existing "DisableAIDataAnalysis" registry value.
Adversaries may enable Windows Recall as part of post-exploitation discovery and collection activities.
This rule assumes that Recall is already explicitly disabled on the host, and subsequently enabled by the adversary.

## Metadata

- Rule ID: 5dfc1465-8f65-4fde-8eb5-6194380c6a62
- Status: test
- Level: medium
- Author: Sajid Nawaz Khan
- Date: 2024-06-02
- Source Path: rules/windows/registry/registry_delete/registry_delete_enable_windows_recall.yml

## Logsource

- category: registry_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Detection

```yaml
selection:
  EventType: DeleteValue
  TargetObject|endswith: \Microsoft\Windows\WindowsAI\DisableAIDataAnalysis
condition: selection
```

## False Positives

- Legitimate use/activation of Windows Recall

## References

- https://learn.microsoft.com/en-us/windows/client-management/manage-recall
- https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowsai#disableaidataanalysis

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_enable_windows_recall.yml)
