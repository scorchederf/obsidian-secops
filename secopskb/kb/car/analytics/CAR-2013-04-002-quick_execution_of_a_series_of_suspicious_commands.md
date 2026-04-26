---
car_id: "CAR-2013-04-002"
title: "Quick execution of a series of suspicious commands"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-04-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-04-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-04-002"
  - "Quick execution of a series of suspicious commands"
attack_technique_ids:
  - "T1087"
  - "T1087.001"
  - "T1087.002"
  - "T1003"
  - "T1003.002"
  - "T1069"
  - "T1069.001"
  - "T1069.002"
  - "T1057"
  - "T1021"
  - "T1021.002"
  - "T1543"
  - "T1543.003"
  - "T1112"
  - "T1574"
  - "T1574.011"
  - "T1018"
  - "T1569"
  - "T1569.002"
  - "T1053"
  - "T1053.002"
  - "T1053.005"
  - "T1029"
  - "T1033"
  - "T1007"
  - "T1082"
  - "T1049"
  - "T1016"
  - "T1010"
  - "T1518"
  - "T1518.001"
  - "T1046"
  - "T1562"
  - "T1562.001"
  - "T1562.006"
  - "T1098"
  - "T1059"
  - "T1059.005"
  - "T1012"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
implementation_types:
  - "pseudocode"
  - "Sigma"
  - "DNIF"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2013-04-002: Quick execution of a series of suspicious commands

## Metadata

- CAR ID: CAR-2013-04-002
- Submission Date: 2013/04/11
- Information Domain: Analytic, Host
- Analytic Type: TTP
- Platforms: Windows, Linux, macOS
- Data Subtypes: Process
- Contributors: MITRE

## Description

Certain commands are frequently used by malicious actors and infrequently used by normal users. By looking for execution of these commands in short periods of time, we can not only see when a malicious user was on the system but also get an idea of what they were doing.

  Commands of interest:

-   arp.exe
-   at.exe
-   attrib.exe
-   cscript.exe
-   dsquery.exe
-   hostname.exe
-   ipconfig.exe
-   mimikatz.exe
-   nbstat.exe
-   net.exe
-   netsh.exe
-   nslookup.exe
-   ping.exe
-   quser.exe
-   qwinsta.exe
-   reg.exe
-   runas.exe
-   sc.exe
-   schtasks.exe
-   ssh.exe
-   systeminfo.exe
-   taskkill.exe
-   telnet.exe
-   tracert.exe
-   wscript.exe
-   xcopy.exe

### Output Description

The host on which the commands were executed, the time of execution, and what commands were executed

## ATT&CK Coverage

- [[kb/attack/techniques/T1087-account_discovery|T1087]] (coverage: Low; tactics: TA0007)
  - [[kb/attack/techniques/T1087-account_discovery|T1087.001]]
  - [[kb/attack/techniques/T1087-account_discovery|T1087.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]] (coverage: Low; tactics: TA0006)
  - [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069]] (coverage: Low; tactics: TA0007)
  - [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.001]]
  - [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]
- [[kb/attack/techniques/T1057-process_discovery|T1057]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1021-remote_services|T1021]] (coverage: Low; tactics: TA0008)
  - [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543]] (coverage: Low; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]] (coverage: Low; tactics: TA0005)
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574]] (coverage: Low; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]
- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1569-system_services|T1569]] (coverage: Low; tactics: TA0002)
  - [[kb/attack/techniques/T1569-system_services|T1569.002]]
- [[kb/attack/techniques/T1053-scheduled_task_job|T1053]] (coverage: Low; tactics: TA0003, TA0004, TA0002)
  - [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]
  - [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]
- [[kb/attack/techniques/T1029-scheduled_transfer|T1029]] (coverage: Low; tactics: TA0010)
- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1007-system_service_discovery|T1007]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1082-system_information_discovery|T1082]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1010-application_window_discovery|T1010]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1518-software_discovery|T1518]] (coverage: Low; tactics: TA0007)
  - [[kb/attack/techniques/T1518-software_discovery|T1518.001]]
- [[kb/attack/techniques/T1046-network_service_discovery|T1046]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1562-impair_defenses|T1562]] (coverage: Low; tactics: TA0005)
  - [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]
  - [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]
- [[kb/attack/techniques/T1098-account_manipulation|T1098]] (coverage: Low; tactics: TA0006)
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]] (coverage: Moderate; tactics: TA0002)
  - [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1012-query_registry|T1012]] (coverage: Low; tactics: TA0007)

## Implementations

### pseudocode

```pseudocode
processes = search Process:Create
reg_processes = filter processes where (exe == "arp.exe" or exe == "at.exe" or exe == "attrib.exe"
 or exe == "cscript.exe" or exe == "dsquery.exe" or exe == "hostname.exe"
 or exe == "ipconfig.exe" or exe == "mimikatz.exe" or exe == "nbstat.exe"
 or exe == "net.exe" or exe == "netsh.exe" or exe == "nslookup.exe"
 or exe == "ping.exe" or exe == "quser.exe" or exe == "qwinsta.exe"
 or exe == "reg.exe" or exe == "runas.exe" or exe == "sc.exe"
 or exe == "schtasks.exe" or exe == "ssh.exe" or exe == "systeminfo.exe"
 or exe == "taskkill.exe" or exe == "telnet.exe" or exe == "tracert.exe"
 or exe == "wscript.exe" or exe == "xcopy.exe")
reg_grouped = group reg by hostname, ppid where(max time between two events is 30 minutes)
output reg_grouped
```

### Sigma

[Sigma version](https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_multiple_suspicious_cli.yml) of the above pseudocode, with some modifications.

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=regex(arp\.exe|at\.exe|attrib\.exe|cscript\.exe|dsquery\.exe|hostname\.exe|ipconfig\.exe|mimikatz.exe|nbstat\.exe|net\.exe|netsh\.exe|nslookup\.exe|ping\.exe|quser\.exe|qwinsta\.exe|reg\.exe|runas\.exe|sc\.exe|schtasks\.exe|ssh\.exe|systeminfo\.exe|taskkill\.exe|telnet\.exe|tracert\.exe|wscript\.exe|xcopy\.exe)i group count_unique $App limit 100
>>_agg count
>>_checkif int_compare Count > 1 include
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image IN ["*\arp.exe", "*\at.exe", "*\attrib.exe", "*\cscript.exe", "*\dsquery.exe", "*\hostname.exe", "*\ipconfig.exe", "*\mimikatz.exe", "*\nbstat.exe", "*\net.exe", "*\netsh.exe", "*\nslookup.exe", "*\ping.exe", "*\quser.exe", "*\qwinsta.exe", "*\reg.exe", "*\runas.exe", "*\sc.exe", "*\schtasks.exe", "*\ssh.exe", "*\systeminfo.exe", "*\taskkill.exe", "*\telnet.exe", "*\tracert.exe", "*\wscript.exe", "*\xcopy.exe"]
| chart count() as cnt by host
| search cnt > 1
```

## Data Model References

- process/create/hostname
- process/create/ppid
- process/create/exe

## Unit Tests

Within a command window, execute several of the commands in quick succession.

- Configurations: Windows 7

```text
ipconfig /all
hostname
systeminfo
reg.exe Query HKLM\Software\Microsoft
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-04-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-04-002.yaml)
