---
car_id: "CAR-2022-03-001"
title: "Disable Windows Event Logging"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2022-03-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2022-03-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2022-03-001"
  - "Disable Windows Event Logging"
attack_technique_ids:
  - "T1562"
  - "T1562.002"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2022-03-001: Disable Windows Event Logging

## Metadata

- CAR ID: CAR-2022-03-001
- Submission Date: 2022/03/14
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Lucas Heiligenstein

## Description

Adversaries may disable Windows event logging to limit data that can be leveraged for detections and audits. Windows event logs record user and system activity such as login attempts, process creation, and much more. This data is used by security tools and analysts to generate detections. There are different ways to perform this attack.
1. The first one is to create the Registry Key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\MiniNt`. This action will not generate Security EventLog 4657 or Sysmon EventLog 13 because the value of the key remains empty. However, if an attacker uses powershell to perform this attack (and not cmd), a Security EventLog 4663 will be generated (but 4663 generates a lot of noise).
2. The second way is to disable the service EventLog (display name Windows Event Log). After disabed, attacker must reboot the system. The action of disabling or put in manual the service will modify the Registry Key value `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\start`, therefore Security EventLog 4657 or Sysmon EventLog 13 will be generated on the system.
3. The third way is linked with the second. By default, the EventLog service cannot be stopped. If an attacker tries to stop the service, this one will restart immediately. Why ? Because to stop completely, this service must stop others, one in particular called netprofm (display name Network List Service). This service remains running until it is disabled. So Attacker must either disable EventLog and after to stop it or disable netprofm and after stop EventLog. Only stopping the service (even as admin) will not have an effect on the EventLog service because of the link with netprofm. Security EventLog 1100 will log the stop of the EventLog service (but also generates a lot of noise because it will generate a log everytime the system shutdown).
4. The fourth way is to use auditpol.exe to modify the audit configuration and disable/modify important parameters that will lead to disable the creation of EventLog.
5. The last one is to modify the Registry Key value `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Security\file` (or other kind of log) to modify the path where the EventLog are stocked. Importantly, with this technique, the EventViewer will use the value of the Registry Key "file" to know where to find the Log. Thus, using the EventViewer will always show the current event logs, but the old one will be stocked in another evtx. Also, the path must be in a folder that the Eventlog process has access (like it doesn’t work if attacker set up the new path in the Desktop). Attacker can also decrease the maxsize value of the Log to force the system to rewrite on the older EventLog (but the minimum cannot be less than 1028 KB). As the Registry key is modified, Security EventLog 4657 or Sysmon EventLog 13 will be generated on the system. All of these attacks required administrative right. Attacks number three, four and five do not require a system reboot to be effective immediately.

## ATT&CK Coverage

- [[kb/attack/techniques/T1562-impair_defenses|T1562]] (coverage: Moderate; tactics: TA0005)
  - [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Implementations

### Pseudocode

This detects the disabling of Windows Event Logging, via process command line or registry key value manipulation.

```pseudocode
processes = search Process:create
susp_processes = filter processes where ((command_line CONTAINS("*New-Item*") OR command_line CONTAINS("*reg add*")) OR command_line CONTAINS("*MiniNt*")) OR (command_line CONTAINS("*Stop-Service*")AND command_line CONTAINS("*EventLog*")) OR (command_line CONTAINS("*EventLog*") AND (command_line CONTAINS("*Set-Service*") OR command_line CONTAINS("*reg add*") OR command_line CONTAINS("*Set-ItemProperty*") OR command_line CONTAINS("*New-ItemProperty*") OR command_line CONTAINS("*sc config*"))) OR (command_line CONTAINS("*auditpol*") AND (command_line CONTAINS("*/set*") OR command_line CONTAINS("*/clear*") OR command_line CONTAINS("*/revove*"))) OR ((command_line CONTAINS("*wevtutil*") AND (command_line CONTAINS("*sl*") OR command_line CONTAINS("*set-log*"))))
reg_keys = search Registry:value_edit
event_log_reg_keys = filter reg_keys where Key="*EventLog*" AND (value="Start" OR value="File" OR value="MaxSize")
output susp_processes, event_log_reg_keys
```

### Splunk

Splunk version of the CAR pseudocode.

```splunk
((EventCode="4688" OR EventCode="1") ((CommandLine="*New-Item*" OR CommandLine="*reg add*") CommandLine="*MiniNt*")OR (CommandLine="*Stop-Service*" CommandLine="*EventLog*")OR (CommandLine="*EventLog*" (CommandLine="*Set-Service*" OR CommandLine="*reg add*" OR CommandLine="*Set-ItemProperty*" OR CommandLine="*New-ItemProperty*" OR CommandLine="*sc config*")) OR (CommandLine="*auditpol*" (CommandLine="*/set*" OR CommandLine="*/clear*" OR CommandLine="*/revove*")) OR ((CommandLine="*wevtutil*" (CommandLine="*sl*" OR CommandLine="*set-log*")))) OR (EventCode="4719") OR ((EventCode="4657" OR EventCode="13") (ObjectName="*EventLog*") (ObjectValueName="Start" OR ObjectValueName="File" OR ObjectValueName="MaxSize"))
```

### LogPoint

LogPoint version of the CAR pseudocode.

```logpoint
((((((EventCode IN ["4688", "1"] CommandLine="*New-Item*" CommandLine="*reg add*" CommandLine IN "*MiniNt*") OR (CommandLine="*Stop-Service*" CommandLine="*EventLog*")) OR (CommandLine IN ["*Set-Service*", "*reg add*", "*Set-ItemProperty*", "*New-ItemProperty*", "*sc config*"] CommandLine IN "*EventLog*")) OR (CommandLine IN "*auditpol*" CommandLine IN ["*/set*", "*/clear*", "*/revove*"])) OR (CommandLine IN "*wevtutil*" CommandLine IN ["*sl*", "*set-log*"]) OR EventCode IN "4719") OR (EventCode IN ["4657", "13"] ObjectName IN "*EventLog*" ObjectValueName IN ["Start", "File", "MaxSize"]))
```

## Data Model References

- registry/value_edit/value
- process/create/command_line

## Unit Tests

MiniNt Registry Key creation with cmd.

```text
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\MiniNt"
```

MiniNt Registry Key creation with powershell.

```text
New-Item -Path "HKLM:\SYSTEM\CurrentControlSet\Control\MiniNt"
```

Disable EvenLog Service with Set-Service.

```text
Set-Service -Name EventLog -StartupType Disabled
```

Registry Key modification to disable EventLog Service.

```text
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog" /v start /t REG_DWORD /d 0x00000004 /f
```

Stop EventLog Service with Stop-Service.

```text
Stop-Service -Name EventLog -Force
```

Audit configuration modification to disable EventLog with auditpol.

```text
auditpol.exe /set /subcategory:"Process Creation" /success:Disable /failure:Disable
```

Modification of Security EventLog path with wevtutil.

```text
wevtutil.exe sl Security /logfilename:"C:\Windows\System32\winevt\Not-Important-Log.evtx"
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2022-03-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2022-03-001.yaml)
