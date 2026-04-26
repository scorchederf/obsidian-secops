---
sigma_id: "cc36992a-4671-4f21-a91d-6c2b72a2edf5"
title: "Suspicious Eventlog Clearing or Configuration Change Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_eventlog_clear.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_eventlog_clear.yml"
build_date: "2026-04-26 17:03:22"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cc36992a-4671-4f21-a91d-6c2b72a2edf5"
  - "Suspicious Eventlog Clearing or Configuration Change Activity"
attack_technique_ids:
  - "T1070.001"
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Eventlog Clearing or Configuration Change Activity

Detects the clearing or configuration tampering of EventLog using utilities such as "wevtutil", "powershell" and "wmic".
This technique were seen used by threat actors and ransomware strains in order to evade defenses.

## Metadata

- Rule ID: cc36992a-4671-4f21-a91d-6c2b72a2edf5
- Status: stable
- Level: high
- Author: Ecco, Daniil Yugoslavskiy, oscd.community, D3F7A5105, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2019-09-26
- Modified: 2025-03-12
- Source Path: rules/windows/process_creation/proc_creation_win_susp_eventlog_clear.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.001]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Detection

```yaml
selection_wevtutil_img:
- Image|endswith: \wevtutil.exe
- OriginalFileName: wevtutil.exe
selection_wevtutil_cmd:
  CommandLine|contains:
  - 'clear-log '
  - ' cl '
  - 'set-log '
  - ' sl '
  - 'lfn:'
selection_other_ps_img:
  Image|endswith:
  - \powershell.exe
  - \powershell_ise.exe
  - \pwsh.exe
selection_other_ps_cmd:
- CommandLine|contains:
  - 'Clear-EventLog '
  - 'Remove-EventLog '
  - 'Limit-EventLog '
  - 'Clear-WinEvent '
- CommandLine|contains|all:
  - Eventing.Reader.EventLogSession
  - ClearLog
- CommandLine|contains|all:
  - Diagnostics.EventLog
  - Clear
selection_other_wmi:
  Image|endswith:
  - \powershell.exe
  - \powershell_ise.exe
  - \pwsh.exe
  - \wmic.exe
  CommandLine|contains: ClearEventLog
filter_main_msiexec:
  ParentImage:
  - C:\Windows\SysWOW64\msiexec.exe
  - C:\Windows\System32\msiexec.exe
  CommandLine|contains: ' sl '
condition: (all of selection_wevtutil_*) or (all of selection_other_ps_*) or (selection_other_wmi)
  and not 1 of filter_main_*
```

## False Positives

- Admin activity
- Scripts and administrative tools used in the monitored environment
- Maintenance activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.001/T1070.001.md
- https://eqllib.readthedocs.io/en/latest/analytics/5b223758-07d6-4100-9e11-238cfdd0fe97.html
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil
- https://gist.github.com/fovtran/ac0624983c7722e80a8f5a4babb170ee
- https://jdhnet.wordpress.com/2017/12/19/changing-the-location-of-the-windows-event-logs/
- https://www.linkedin.com/posts/huntress-labs_when-a-sketchy-incident-hits-your-network-activity-7304940371078238208-Th_l/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAJTlRcB28IaUtg03HUU-IdliwzoAL1flGc
- https://stackoverflow.com/questions/66011412/how-to-clear-a-event-log-in-powershell-7
- https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.eventing.reader.eventlogsession.clearlog?view=windowsdesktop-9.0&viewFallbackFrom=dotnet-plat-ext-5.0#System_Diagnostics_Eventing_Reader_EventLogSession_ClearLog_System_String_
- https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.eventlog.clear

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_eventlog_clear.yml)
