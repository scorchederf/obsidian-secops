---
car_id: "CAR-2014-11-008"
title: "Command Launched from WinLogon"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-11-008/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-008.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2014-11-008"
  - "Command Launched from WinLogon"
attack_technique_ids:
  - "T1546"
  - "T1546.008"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "Splunk"
  - "EQL"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2014-11-008: Command Launched from WinLogon

## Metadata

- CAR ID: CAR-2014-11-008
- Submission Date: 2014/11/19
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

An adversary can use [accessibility features](https://attack.mitre.org/techniques/T1546/008) (Ease of Access), such as StickyKeys or Utilman, to launch a command shell from the logon screen and gain SYSTEM access. Since an adversary does not have physical access to the machine, this technique must be run within [Remote Desktop](https://attack.mitre.org/techniques/T1021/001). To prevent an adversary from getting to the login screen without first authenticating, Network-Level Authentication (NLA) must be enabled. If a debugger is set up for one of the accessibility features, then it will intercept the process launch of the feature and instead execute a new command line. This analytic looks for instances of `cmd.exe` or `powershell.exe` launched directly from the logon process, `winlogon.exe`. It should be used in tandem with [[kb/car/analytics/CAR-2014-11-003-debuggers_for_accessibility_applications|CAR-2014-11-003]], which detects the accessibility programs in the command line.

Several accessibility programs can be run using the Ease of Access center

-   `sethc.exe` handles StickyKeys
-   `utilman.exe` is the Ease of Access menu
-   `osk.exe` runs the On-Screen Keyboard
-   `narrator.exe` reads screen text over audio
-   `magnify.exe` magnifies the view of the screen near the cursor

## ATT&CK Coverage

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]] (coverage: Moderate; tactics: TA0004, TA0003)
  - [[kb/attack/techniques/T1546-event_triggered_execution|T1546.008]]

## Implementations

### pseudocode

Look for instances of processes where the parent executable is winlogon.exe and the child is an instance of a command prompt.

```pseudocode
processes = search Process:Create
winlogon_cmd = filter processes where (parent_exe == "winlogon.exe" and exe == "cmd.exe")
output winlogon_cmd
```

### Splunk

Splunk version of the above pseudocode.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=1 ParentImage="C:\\Windows\\*\\winlogon.exe" Image="C:\\Windows\\*\\cmd.exe"
```

### EQL

EQL version of the above pseudocode.

- Data Model: EQL native

```eql
process where subtype.create and
  (process_name == "cmd.exe" and parent_process_name == "winlogon.exe")
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 parent_image="C:\Windows\System32\winlogon.exe" parent_image="C:\Windows\System32\cmd.exe"
```

## Data Model References

- process/create/exe
- process/create/parent_exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-11-008/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-11-008.yaml)
