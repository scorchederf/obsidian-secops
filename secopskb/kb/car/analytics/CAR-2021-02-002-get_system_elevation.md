---
car_id: "CAR-2021-02-002"
title: "Get System Elevation"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-02-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-02-002.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2021-02-002"
  - "Get System Elevation"
attack_technique_ids:
  - "T1548"
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

Cyber actors frequently escalate to the SYSTEM account after gaining entry to a Windows host, to enable them to carry out various attacks more effectively. Tools such as Meterpreter, Cobalt Strike, and Empire carry out automated steps to "Get System", which is the same as switching over to the System user account. Most of these tools utilize multiple techniques to try and attain SYSTEM: in the first technique, they create a named pipe and connects an instance of cmd.exe to it, which allows them to impersonate the security context of cmd.exe, which is SYSTEM. In the second technique, a malicious DLL is injected into a process that is running as SYSTEM; the injected DLL steals the SYSTEM token and applies it where necessary to escalate privileges. This analytic looks for both of these techniques.

## ATT&CK Coverage

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]] (coverage: Moderate; tactics: TA0004, TA0005)

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process
suspicious_processes = filter processes where (
  (parent_image_path == C:\Windows\System32\services.exe" AND
   image_path == "C:\Windows\System32\cmd.exe" AND
   command_line == "*echo*" AND
   command_line == "*\pipe\*") OR
  (image_path == "C:\Windows\System32\rundll32.exe" AND
   command_line == "*,a /p:*"))
output suspicious_processes
```

### Splunk

Look for instances GetSystem elevation performed by Meterpreter or Cobalt Strike

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ (ParentImage="C:\\Windows\\System32\\services.exe" Image="C:\\Windows\\System32\\cmd.exe" (CommandLine="*echo*" AND CommandLine="*\\pipe\\*"))
OR (Image="C:\\Windows\\System32\\rundll32.exe" CommandLine="*,a /p:*")
```

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process
suspicious_processes = filter processes where (
  (image_path == "C:\Windows\System32\cmd.exe" OR
   command_line == "*%COMSPEC%*") AND
   command_line == "*echo*" AND
   command_line == "*\pipe\*"))
output suspicious_processes
```

### Splunk

Look for instances GetSystem elevation performed by Empire or PoshC2

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ (Image="C:\\Windows\\System32\\cmd.exe" OR CommandLine="*%COMSPEC%*") (CommandLine="*echo*" AND CommandLine="*\pipe\*")
```

## Data Model References

- process/create/exe
- process/create/parent_exe
- process/create/command_line
- service/create/command_line

## Unit Tests

GetSystem in Meterpreter & Cobalt Strike’s Beacon

```text
cmd.exe /c echo ba80ae80df9 > \\.\pipe\66bee3
cmd.exe /c echo fvxens > \\.\pipe\fvxens
rundll32.exe C:\Users\user\AppData\Local\Temp\fvxens.dll,a /p:fvxens
```

GetSystem in Empire & PoshC2

```text
cmd.exe /C start %COMSPEC% /C `"timeout /t 3 >nul&&echo TestSVC > \\.\pipe\TestSVC
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-02-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-02-002.yaml)
