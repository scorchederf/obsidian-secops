---
sigma_id: "d4e2745c-f0c6-4bde-a3ab-b553b3f693cc"
title: "Persistence Via Disk Cleanup Handler - Autorun"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disk_cleanup_handler_autorun_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disk_cleanup_handler_autorun_persistence.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "d4e2745c-f0c6-4bde-a3ab-b553b3f693cc"
  - "Persistence Via Disk Cleanup Handler - Autorun"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Persistence Via Disk Cleanup Handler - Autorun

Detects when an attacker modifies values of the Disk Cleanup Handler in the registry to achieve persistence via autorun.
The disk cleanup manager is part of the operating system.
It displays the dialog box […] The user has the option of enabling or disabling individual handlers by selecting or clearing their check box in the disk cleanup manager's UI.
Although Windows comes with a number of disk cleanup handlers, they aren't designed to handle files produced by other applications.
Instead, the disk cleanup manager is designed to be flexible and extensible by enabling any developer to implement and register their own disk cleanup handler.
Any developer can extend the available disk cleanup services by implementing and registering a disk cleanup handler.

## Metadata

- Rule ID: d4e2745c-f0c6-4bde-a3ab-b553b3f693cc
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-21
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_disk_cleanup_handler_autorun_persistence.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
root:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\
selection_autorun:
  TargetObject|contains: \Autorun
  Details: DWORD (0x00000001)
selection_pre_after:
  TargetObject|contains:
  - \CleanupString
  - \PreCleanupString
  Details|contains:
  - cmd
  - powershell
  - rundll32
  - mshta
  - cscript
  - wscript
  - wsl
  - \Users\Public\
  - \Windows\TEMP\
  - \Microsoft\Windows\Start Menu\Programs\Startup\
condition: root and 1 of selection_*
```

## False Positives

- Unknown

## References

- https://persistence-info.github.io/Data/diskcleanuphandler.html
- https://www.hexacorn.com/blog/2018/09/02/beyond-good-ol-run-key-part-86/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disk_cleanup_handler_autorun_persistence.yml)
