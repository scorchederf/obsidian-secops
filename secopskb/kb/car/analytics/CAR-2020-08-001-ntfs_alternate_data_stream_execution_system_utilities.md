---
car_id: "CAR-2020-08-001"
title: "NTFS Alternate Data Stream Execution - System Utilities"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-08-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-08-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-08-001"
  - "NTFS Alternate Data Stream Execution - System Utilities"
attack_technique_ids:
  - "T1564"
  - "T1564.004"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "splunk"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2020-08-001: NTFS Alternate Data Stream Execution - System Utilities

## Metadata

- CAR ID: CAR-2020-08-001
- Submission Date: 2020/08/03
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

NTFS Alternate Data Streams (ADSs) may be used by adversaries as a means of evading security tools by storing malicious data or binaries in file attribute metadata. ADSs are also powerful because they can be directly executed by various Windows tools; accordingly, this analytic looks at common ways of executing ADSs using system utilities such as powershell.

## ATT&CK Coverage

- [[kb/attack/techniques/T1564-hide_artifacts|T1564]] (coverage: Low; tactics: TA0005)
  - [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Implementations

### pseudocode

This is generic pseudocode that lines up with the below Splunk queries.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
ads_processes = filter processes where (
exe == "powershell.exe OR rundll32.exe OR wmic.exe OR wscript.exe OR cscript.exe" and command_line.matches("__some_regex__")
)
output ads_processes
```

### splunk

This Splunk query looks for invocations of powershell used to execute NTFS alternate data streams.

- Data Model: Sysmon native

```splunk
index=__sysmon_index__ EventCode=1 Image=C:\\Windows\\*\\powershell.exe|regex CommandLine="Invoke-CimMethod\s+-ClassName\s+Win32_Process\s+-MethodName\s+Create.*\b(\w+(\.\w+)?):(\w+(\.\w+)?)|-ep bypass\s+-\s+<.*\b(\w+(\.\w+)?):(\w+(\.\w+)?)|-command.*Get-Content.*-Stream.*Set-Content.*start-process .*(\w+(\.\w+)?)"
```

### splunk

This Splunk query looks for invocations of WMIC used to execute NTFS alternate data streams.

- Data Model: Sysmon native

```splunk
index=__sysmon_index__ EventCode=1 Image=C:\\Windows\\*\\wmic.exe | regex CommandLine="process call create.*\"(\w+(\.\w+)?):(\w+(\.\w+)?)"
```

### splunk

This Splunk query looks for invocations of rundll32 used to execute NTFS alternate data streams.

- Data Model: Sysmon native

```splunk
index=__sysmon_index__  EventCode=1 Image=C:\\Windows\\*\\rundll32.exe | regex CommandLine="\"?(\w+(\.\w+)?):(\w+(\.\w+)?)?\"?,\w+\|(advpack\.dll\|ieadvpack\.dll),RegisterOCX\s+(\w+\.\w+):(\w+(\.\w+)?)\|(shdocvw\.dll\|ieframe\.dll),OpenURL.*(\w+\.\w+):(\w+(\.\w+)?)"
```

### splunk

This Splunk query looks for invocations of the windows scripting host used to execute NTFS alternate data streams.

- Data Model: Sysmon native

```splunk
index=__sysmon_index__ EventCode=1 (Image=C:\\Windows\\*\\wscript.exe OR Image=C:\\Windows\\*\\cscript.exe) | regex CommandLine="(?<!\/)\b\w+(\.\w+)?:\w+(\.\w+)?$"
```

## Data Model References

- process/create/exe
- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-08-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-08-001.yaml)
