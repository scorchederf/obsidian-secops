---
sigma_id: "817f252c-5143-4dae-b418-48c3e9f63728"
title: "Windows Recall Feature Enabled Via Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_enable_windows_recall.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_enable_windows_recall.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "817f252c-5143-4dae-b418-48c3e9f63728"
  - "Windows Recall Feature Enabled Via Reg.EXE"
attack_technique_ids:
  - "T1113"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Recall Feature Enabled Via Reg.EXE

Detects the enabling of the Windows Recall feature via registry manipulation.
Windows Recall can be enabled by deleting the existing "DisableAIDataAnalysis" value, or setting it to 0.
Adversaries may enable Windows Recall as part of post-exploitation discovery and collection activities.
This rule assumes that Recall is already explicitly disabled on the host, and subsequently enabled by the adversary.

## Metadata

- Rule ID: 817f252c-5143-4dae-b418-48c3e9f63728
- Status: test
- Level: medium
- Author: Sajid Nawaz Khan
- Date: 2024-06-02
- Source Path: rules/windows/process_creation/proc_creation_win_reg_enable_windows_recall.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Detection

```yaml
selection_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_value:
  CommandLine|contains|all:
  - Microsoft\Windows\WindowsAI
  - DisableAIDataAnalysis
selection_action_add:
  CommandLine|contains:
  - add
  - '0'
selection_action_delete:
  CommandLine|contains: delete
condition: selection_img and selection_value and 1 of selection_action_*
```

## False Positives

- Legitimate use/activation of Windows Recall

## References

- https://learn.microsoft.com/en-us/windows/client-management/manage-recall
- https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowsai#disableaidataanalysis

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_enable_windows_recall.yml)
