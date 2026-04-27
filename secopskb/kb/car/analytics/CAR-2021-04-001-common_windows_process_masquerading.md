---
car_id: "CAR-2021-04-001"
title: "Common Windows Process Masquerading"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-04-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-04-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-04-001"
  - "Common Windows Process Masquerading"
attack_technique_ids:
  - "T1036"
  - "T1036.005"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2021-04-001: Common Windows Process Masquerading

## Metadata

- CAR ID: CAR-2021-04-001
- Submission Date: 2021/02/12
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Sebastien Damaye

## Description

[Masquerading (T1036)](https://attack.mitre.org/techniques/T1036/) is defined by ATT&CK as follows:

"Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names."

Malware authors often use this technique to hide malicious executables behind legitimate Windows executable names (e.g. `lsass.exe`, `svchost.exe`, etc).

There are several sub-techniques, but this analytic focuses on [Match Legitimate Name or Location](https://attack.mitre.org/techniques/T1036/005/) only.

**Analytic Methodology**

With process monitoring, hunt for processes matching these criteria:

* process name is `svchost.exe`, `smss.exe`, `wininit.exe`, `taskhost.exe`, etc.
* process path is not `C:\Windows\System32\` or `C:\Windows\SysWow64\`

Examples (true positive):

`C:\Users\administrator\svchost.exe`

To make sure the rule doesn't miss cases where the executable would be started from a sub-folder of these locations, the entire path is checked for the process path. The below example should be considered as suspicious:

`C:\Windows\System32\srv\svchost.exe`

## ATT&CK Coverage

- [[kb/attack/techniques/T1036-masquerading|T1036]] (coverage: Moderate; tactics: TA0005)
  - [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Implementations

### Pseudocode

Looks for mismatches between process names and their image paths.

- Data Model: CAR native

```pseudocode
processes = search Process:*
suspicious_processes = filter processes where (
  (exe=svchost.exe AND (image_path!="C:\\Windows\\System32\\svchost.exe" OR process_path!="C:\\Windows\\SysWow64\\svchost.exe"))
  OR (exe=smss.exe AND image_path!="C:\\Windows\\System32\\smss.exe")
  OR (exe=wininit.exe AND image_path!="C:\\Windows\\System32\\wininit.exe")
  OR (exe=taskhost.exe AND image_path!="C:\\Windows\\System32\\taskhost.exe")
  OR (exe=lasass.exe AND image_path!="C:\\Windows\\System32\\lsass.exe")
  OR (exe=winlogon.exe AND image_path!="C:\\Windows\\System32\\winlogon.exe")
  OR (exe=csrss.exe AND image_path!="C:\\Windows\\System32\\csrss.exe")
  OR (exe=services.exe AND image_path!="C:\\Windows\\System32\\services.exe")
  OR (exe=lsm.exe AND image_path!="C:\\Windows\\System32\\lsm.exe")
  OR (exe=explorer.exe AND image_path!="C:\\Windows\\explorer.exe")
  )
output suspicious_processes
```

### Splunk

Splunk search version of the above pseudocode.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" AND (
(process_name=svchost.exe AND NOT (process_path="C:\\Windows\\System32\\svchost.exe" OR process_path="C:\\Windows\\SysWow64\\svchost.exe"))
OR (process_name=smss.exe AND NOT process_path="C:\\Windows\\System32\\smss.exe")
OR (process_name=wininit.exe AND NOT process_path="C:\\Windows\\System32\\wininit.exe")
OR (process_name=taskhost.exe AND NOT process_path="C:\\Windows\\System32\\taskhost.exe")
OR (process_name=lasass.exe AND NOT process_path="C:\\Windows\\System32\\lsass.exe")
OR (process_name=winlogon.exe AND NOT process_path="C:\\Windows\\System32\\winlogon.exe")
OR (process_name=csrss.exe AND NOT process_path="C:\\Windows\\System32\\csrss.exe")
OR (process_name=services.exe AND NOT process_path="C:\\Windows\\System32\\services.exe")
OR (process_name=lsm.exe AND NOT process_path="C:\\Windows\\System32\\lsm.exe")
OR (process_name=explorer.exe AND NOT process_path="C:\\Windows\\explorer.exe")
)
```

## Data Model References

- process/create/exe
- process/create/image_path
- process/access/exe
- process/access/image_path
- process/terminate/exe
- process/terminate/image_path

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-04-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-04-001.yaml)
