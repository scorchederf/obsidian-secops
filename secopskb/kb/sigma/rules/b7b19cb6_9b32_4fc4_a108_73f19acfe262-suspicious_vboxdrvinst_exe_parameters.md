---
sigma_id: "b7b19cb6-9b32-4fc4-a108-73f19acfe262"
title: "Suspicious VBoxDrvInst.exe Parameters"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_virtualbox_vboxdrvinst_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_virtualbox_vboxdrvinst_execution.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b7b19cb6-9b32-4fc4-a108-73f19acfe262"
  - "Suspicious VBoxDrvInst.exe Parameters"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious VBoxDrvInst.exe Parameters

Detect VBoxDrvInst.exe run with parameters allowing processing INF file.
This allows to create values in the registry and install drivers.
For example one could use this technique to obtain persistence via modifying one of Run or RunOnce registry keys

## Metadata

- Rule ID: b7b19cb6-9b32-4fc4-a108-73f19acfe262
- Status: test
- Level: medium
- Author: Konstantin Grishchenko, oscd.community
- Date: 2020-10-06
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_virtualbox_vboxdrvinst_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  Image|endswith: \VBoxDrvInst.exe
  CommandLine|contains|all:
  - driver
  - executeinf
condition: selection
```

## False Positives

- Legitimate use of VBoxDrvInst.exe utility by VirtualBox Guest Additions installation process

## References

- https://github.com/LOLBAS-Project/LOLBAS/blob/4db780e0f0b2e2bb8cb1fa13e09196da9b9f1834/yml/LOLUtilz/OtherBinaries/VBoxDrvInst.yml
- https://twitter.com/pabraeken/status/993497996179492864

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_virtualbox_vboxdrvinst_execution.yml)
