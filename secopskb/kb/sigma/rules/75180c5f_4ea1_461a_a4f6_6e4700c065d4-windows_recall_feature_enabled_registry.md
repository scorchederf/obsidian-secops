---
sigma_id: "75180c5f-4ea1-461a-a4f6-6e4700c065d4"
title: "Windows Recall Feature Enabled - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_enable_windows_recall.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_enable_windows_recall.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "75180c5f-4ea1-461a-a4f6-6e4700c065d4"
  - "Windows Recall Feature Enabled - Registry"
attack_technique_ids:
  - "T1113"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Recall Feature Enabled - Registry

Detects the enabling of the Windows Recall feature via registry manipulation. Windows Recall can be enabled by setting the value of "DisableAIDataAnalysis" to "0".
Adversaries may enable Windows Recall as part of post-exploitation discovery and collection activities.
This rule assumes that Recall is already explicitly disabled on the host, and subsequently enabled by the adversary.

## Metadata

- Rule ID: 75180c5f-4ea1-461a-a4f6-6e4700c065d4
- Status: test
- Level: medium
- Author: Sajid Nawaz Khan
- Date: 2024-06-02
- Source Path: rules/windows/registry/registry_set/registry_set_enable_windows_recall.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Software\Policies\Microsoft\Windows\WindowsAI\DisableAIDataAnalysis
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Legitimate use/activation of Windows Recall

## References

- https://learn.microsoft.com/en-us/windows/client-management/manage-recall
- https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowsai#disableaidataanalysis

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_enable_windows_recall.yml)
