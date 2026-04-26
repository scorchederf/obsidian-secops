---
sigma_id: "d4f4e0be-cf12-439f-9e25-4e2cdcf7df5a"
title: "Potential Persistence Via Disk Cleanup Handler - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_add/registry_add_persistence_disk_cleanup_handler_entry.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_add/registry_add_persistence_disk_cleanup_handler_entry.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_add"
aliases:
  - "d4f4e0be-cf12-439f-9e25-4e2cdcf7df5a"
  - "Potential Persistence Via Disk Cleanup Handler - Registry"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Disk Cleanup Handler - Registry

Detects when an attacker modifies values of the Disk Cleanup Handler in the registry to achieve persistence.
The disk cleanup manager is part of the operating system. It displays the dialog box […]
The user has the option of enabling or disabling individual handlers by selecting or clearing their check box in the disk cleanup manager's UI.
Although Windows comes with a number of disk cleanup handlers, they aren't designed to handle files produced by other applications.
Instead, the disk cleanup manager is designed to be flexible and extensible by enabling any developer to implement and register their own disk cleanup handler.
Any developer can extend the available disk cleanup services by implementing and registering a disk cleanup handler.

## Metadata

- Rule ID: d4f4e0be-cf12-439f-9e25-4e2cdcf7df5a
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-21
- Modified: 2023-02-07
- Source Path: rules/windows/registry/registry_add/registry_add_persistence_disk_cleanup_handler_entry.yml

## Logsource

- category: registry_add
- product: windows

## Detection

```yaml
selection:
  EventType: CreateKey
  TargetObject|contains: \SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\
filter_main_default_keys:
  TargetObject|endswith:
  - \Active Setup Temp Folders
  - \BranchCache
  - \Content Indexer Cleaner
  - \D3D Shader Cache
  - \Delivery Optimization Files
  - \Device Driver Packages
  - \Diagnostic Data Viewer database files
  - \Downloaded Program Files
  - \DownloadsFolder
  - \Feedback Hub Archive log files
  - \Internet Cache Files
  - \Language Pack
  - \Microsoft Office Temp Files
  - \Offline Pages Files
  - \Old ChkDsk Files
  - \Previous Installations
  - \Recycle Bin
  - \RetailDemo Offline Content
  - \Setup Log Files
  - \System error memory dump files
  - \System error minidump files
  - \Temporary Files
  - \Temporary Setup Files
  - \Temporary Sync Files
  - \Thumbnail Cache
  - \Update Cleanup
  - \Upgrade Discarded Files
  - \User file versions
  - \Windows Defender
  - \Windows Error Reporting Files
  - \Windows ESD installation files
  - \Windows Upgrade Log Files
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate new entry added by windows

## References

- https://persistence-info.github.io/Data/diskcleanuphandler.html
- https://www.hexacorn.com/blog/2018/09/02/beyond-good-ol-run-key-part-86/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_add/registry_add_persistence_disk_cleanup_handler_entry.yml)
