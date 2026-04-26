---
sigma_id: "ebea773c-a8f1-42ad-a856-00cb221966e8"
title: "DLL Sideloading by VMware Xfer Utility"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dll_sideload_vmware_xfer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dll_sideload_vmware_xfer.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ebea773c-a8f1-42ad-a856-00cb221966e8"
  - "DLL Sideloading by VMware Xfer Utility"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DLL Sideloading by VMware Xfer Utility

Detects execution of VMware Xfer utility (VMwareXferlogs.exe) from the non-default directory which may be an attempt to sideload arbitrary DLL

## Metadata

- Rule ID: ebea773c-a8f1-42ad-a856-00cb221966e8
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-02
- Source Path: rules/windows/process_creation/proc_creation_win_dll_sideload_vmware_xfer.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  Image|endswith: \VMwareXferlogs.exe
filter:
  Image|startswith: C:\Program Files\VMware\
condition: selection and not filter
```

## False Positives

- Unlikely

## References

- https://www.sentinelone.com/labs/lockbit-ransomware-side-loads-cobalt-strike-beacon-with-legitimate-vmware-utility/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dll_sideload_vmware_xfer.yml)
