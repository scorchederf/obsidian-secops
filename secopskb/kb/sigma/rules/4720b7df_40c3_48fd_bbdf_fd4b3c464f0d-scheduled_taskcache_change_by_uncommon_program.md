---
sigma_id: "4720b7df-40c3-48fd-bbdf-fd4b3c464f0d"
title: "Scheduled TaskCache Change by Uncommon Program"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_taskcache_entry.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_taskcache_entry.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "4720b7df-40c3-48fd-bbdf-fd4b3c464f0d"
  - "Scheduled TaskCache Change by Uncommon Program"
attack_technique_ids:
  - "T1053"
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Scheduled TaskCache Change by Uncommon Program

Monitor the creation of a new key under 'TaskCache' when a new scheduled task is registered by a process that is not svchost.exe, which is suspicious

## Metadata

- Rule ID: 4720b7df-40c3-48fd-bbdf-fd4b3c464f0d
- Status: test
- Level: high
- Author: Syed Hasan (@syedhasan009)
- Date: 2021-06-18
- Modified: 2025-10-22
- Source Path: rules/windows/registry/registry_set/registry_set_taskcache_entry.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053]]
- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection:
  TargetObject|contains: SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\
filter_main_empty:
  Details: (Empty)
filter_main_null:
  Details: null
filter_main_other:
  TargetObject|contains:
  - Microsoft\Windows\UpdateOrchestrator
  - Microsoft\Windows\SoftwareProtectionPlatform\SvcRestartTask\Index
  - Microsoft\Windows\Flighting\OneSettings\RefreshCache\Index
filter_main_mousocoreworker:
  Image|endswith: C:\Windows\System32\MoUsoCoreWorker.exe
filter_main_services:
  Image|endswith: C:\Windows\System32\services.exe
filter_main_tiworker:
  Image|startswith: C:\Windows\
  Image|endswith: \TiWorker.exe
filter_main_svchost:
  Image: C:\WINDOWS\system32\svchost.exe
filter_main_ngen:
  Image|startswith: C:\Windows\Microsoft.NET\Framework
  Image|endswith: \ngen.exe
  TargetObject|contains:
  - \Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks\{B66B135D-DA06-4FC4-95F8-7458E1D10129}
  - \Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\Microsoft\Windows\.NET
    Framework\.NET Framework NGEN
filter_main_office:
  Image:
  - C:\Program Files\Microsoft Office\root\Integration\Integrator.exe
  - C:\Program Files (x86)\Microsoft Office\root\Integration\Integrator.exe
  - C:\Program Files\Common Files\microsoft shared\ClickToRun\OfficeC2RClient.exe
  - C:\Program Files (x86)\Common Files\microsoft shared\ClickToRun\OfficeC2RClient.exe
filter_main_msiexec:
  Image: C:\Windows\System32\msiexec.exe
filter_main_explorer:
  Image: C:\Windows\explorer.exe
  TargetObject|contains: \Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\Microsoft\Windows\PLA\Server
    Manager Performance Monitor\
filter_main_system:
  Image: System
filter_main_runtimebroker:
  Image: C:\Windows\System32\RuntimeBroker.exe
filter_optional_dropbox_updater:
  Image:
  - C:\Program Files (x86)\Dropbox\Update\DropboxUpdate.exe
  - C:\Program Files\Dropbox\Update\DropboxUpdate.exe
filter_optional_edge:
  Image|endswith:
  - C:\Program Files (x86)\Microsoft\EdgeUpdate\MicrosoftEdgeUpdate.exe
  - C:\Program Files\Microsoft\EdgeUpdate\MicrosoftEdgeUpdate.exe
filter_optional_onedrive:
  Image|endswith:
  - C:\Program Files (x86)\Microsoft OneDrive\OneDrive.exe
  - C:\Program Files\Microsoft OneDrive\OneDrive.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/
- https://labs.f-secure.com/blog/scheduled-task-tampering/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_taskcache_entry.yml)
