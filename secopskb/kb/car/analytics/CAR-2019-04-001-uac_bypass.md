---
car_id: "CAR-2019-04-001"
title: "UAC Bypass"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2019-04-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-04-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2019-04-001"
  - "UAC Bypass"
attack_technique_ids:
  - "T1548"
  - "T1548.002"
platforms:
  - "Windows"
implementation_types:
  - "splunk"
  - "pseudocode"
  - "Sigma"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2019-04-001: UAC Bypass

## Metadata

- CAR ID: CAR-2019-04-001
- Submission Date: 2019/04/19
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

Bypassing user account control (UAC Bypass) is generally done by piggybacking on a system process that has auto-escalate privileges. This analytic looks to detect those cases as described by the open-source [UACME](https://github.com/hfiref0x/UACME) tool.

## ATT&CK Coverage

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]] (coverage: Low; tactics: TA0005)
  - [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Implementations

### splunk

This Splunk query looks for specific invocations of UACME, representing different ways to bypass user account control.

- Data Model: Sysmon native

```splunk
index=_your_sysmon_index_ EventCode=1 IntegrityLevel=High|search (ParentCommandLine="\"c:\\windows\\system32\\dism.exe\"*""*.xml" AND Image!="c:\\users\\*\\appdata\\local\\temp\\*\\dismhost.exe") OR ParentImage=c:\\windows\\system32\\fodhelper.exe OR (CommandLine="\"c:\\windows\\system32\\wusa.exe\"*/quiet*" AND User!=NOT_TRANSLATED AND CurrentDirectory=c:\\windows\\system32\\ AND ParentImage!=c:\\windows\\explorer.exe) OR CommandLine="*.exe\"*cleanmgr.exe /autoclean*" OR (ParentImage="c:\\windows\\*dccw.exe" AND Image!="c:\\windows\\system32\\cttune.exe") OR Image="c:\\program files\\windows media player\\osk.exe" OR ParentImage="c:\\windows\\system32\\slui.exe"|eval PossibleTechniques=case(like(lower(ParentCommandLine),"%c:\\windows\\system32\\dism.exe%"), "UACME #23", like(lower(Image),"c:\\program files\\windows media player\\osk.exe"), "UACME #32", like(lower(ParentImage),"c:\\windows\\system32\\fodhelper.exe"),  "UACME #33", like(lower(CommandLine),"%.exe\"%cleanmgr.exe /autoclean%"), "UACME #34", like(lower(Image),"c:\\windows\\system32\\wusa.exe"), "UACME #36", like(lower(ParentImage),"c:\\windows\\%dccw.exe"), "UACME #37", like(lower(ParentImage),"c:\\windows\\system32\\slui.exe"), "UACME #45")
```

### pseudocode

This is a pseudocode version of the above Splunk query.

- Data Model: CAR

```pseudocode
processes = search Process:Create
possible_uac_bypass = filter processes where (
  integrity_level == "High" and
  (parent_image_path == "c:\windows\system32\fodhelper.exe") or
  (command_line == "*.exe\"*cleanmgr.exe /autoclean*") or
  (image_path == "c:\program files\windows media player\osk.exe") or
  (parent_image_path == "c:\windows\system32\slui.exe") or
  (parent_command_line == '"c:\windows\system32\dism.exe"*""*.xml"' and image_path != "c:\users\*\appdata\local\temp\*\dismhost.exe") or
  (command_line == '"c:\windows\system32\wusa.exe"*/quiet*' and user != "NOT_TRANSLATED" and current_working_directory == "c:\windows\system32\" and parent_image_path != "c:\windows\explorer.exe") or
  (parent_image_path == "c:\windows\*dccw.exe" and image_path != "c:\windows\system32\cttune.exe")
)
output possible_uac_bypass
```

### Sigma

[Sigma](https://github.com/Neo23x0/sigma/blob/master/rules/windows/sysmon/sysmon_uac_bypass_eventvwr.yml) rule for detecting eventvwr-based UAC bypass.

### Sigma

[Sigma](https://github.com/Neo23x0/sigma/blob/master/rules/windows/sysmon/sysmon_uac_bypass_sdclt.yml) rule for detecting sdclt-based UAC bypass.

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 integrity_level="High" ((parent_image="c:\windows\system32\fodhelper.exe" OR command='*.exe"*cleanmgr.exe /autoclean*' OR image="c:\program files\windows media player\osk.exe" OR parent_image="c:\windows\system32\slui.exe") OR (parent_command='"c:\windows\system32\dism.exe"*""*.xml"' -image="c:\users\*\appdata\local\temp\*\dismhost.exe") OR (parent_image="c:\windows\*dccw.exe" -image="c:\windows\system32\cttune.exe") OR (command='"c:\windows\system32\wusa.exe"*/quiet*' -user="NOT_TRANSLATED" path="c:\windows\system32\" -parent_image="c:\windows\explorer.exe"))
```

## Data Model References

- process/create/image_path
- process/create/parent_image_path
- process/create/integrity_level
- process/create/user
- process/create/parent_command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2019-04-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-04-001.yaml)
