---
atomic_guid: "5a496325-0115-4274-8eb9-755b649ad0fb"
title: "Windows Recall Feature Enabled - DisableAIDataAnalysis Value Deleted"
framework: "atomic"
generated: "true"
attack_technique_id: "T1113"
attack_technique_name: "Screen Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "5a496325-0115-4274-8eb9-755b649ad0fb"
  - "Windows Recall Feature Enabled - DisableAIDataAnalysis Value Deleted"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Recall Feature Enabled - DisableAIDataAnalysis Value Deleted

Detects the enabling of the Windows Recall feature via registry manipulation. Windows Recall can be enabled by deleting the existing "DisableAIDataAnalysis" registry value. Adversaries may enable Windows Recall as part of post-exploitation discovery and collection activities. This rule assumes that Recall is already explicitly disabled on the host, and subsequently enabled by the adversary. 
- https://learn.microsoft.com/en-us/windows/client-management/manage-recall
- https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-windowsai#disableaidataanalysis

## Metadata

- Atomic GUID: 5a496325-0115-4274-8eb9-755b649ad0fb
- Technique: T1113: Screen Capture
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1113/T1113.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
reg add "HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsAI" /v DisableAIDataAnalysis /t REG_DWORD /d 0 /f
reg delete "HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsAI" /v DisableAIDataAnalysis /f
```

### Cleanup

```powershell
reg add "HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\WindowsAI" /v DisableAIDataAnalysis /t REG_DWORD /d 1 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml)
