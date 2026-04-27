---
car_id: "CAR-2013-04-002"
title: "Quick execution of a series of suspicious commands"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-04-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-04-002.yaml"
build_date: "2026-04-27 19:03:49"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

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

- [[kb/attack/techniques/T1087-account_discovery|T1087: Account Discovery]] (coverage: Low; tactics: TA0007)
  - [[kb/attack/techniques/T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]
  - [[kb/attack/techniques/T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]] (coverage: Low; tactics: TA0006)
  - [[kb/attack/techniques/T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069: Permission Groups Discovery]] (coverage: Low; tactics: TA0007)
  - [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]
  - [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
- [[kb/attack/techniques/T1057-process_discovery|T1057: Process Discovery]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1021-remote_services|T1021: Remote Services]] (coverage: Low; tactics: TA0008)
  - [[kb/attack/techniques/T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543: Create or Modify System Process]] (coverage: Low; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]] (coverage: Low; tactics: TA0005)
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574: Hijack Execution Flow]] (coverage: Low; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574011-services-registry-permissions-weakness|T1574.011: Services Registry Permissions Weakness]]
- [[kb/attack/techniques/T1018-remote_system_discovery|T1018: Remote System Discovery]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1569-system_services|T1569: System Services]] (coverage: Low; tactics: TA0002)
  - [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]
- [[kb/attack/techniques/T1053-scheduled_task_job|T1053: Scheduled Task/Job]] (coverage: Low; tactics: TA0003, TA0004, TA0002)
  - [[kb/attack/techniques/T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
  - [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[kb/attack/techniques/T1029-scheduled_transfer|T1029: Scheduled Transfer]] (coverage: Low; tactics: TA0010)
- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1007-system_service_discovery|T1007: System Service Discovery]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1082-system_information_discovery|T1082: System Information Discovery]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1010-application_window_discovery|T1010: Application Window Discovery]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1518-software_discovery|T1518: Software Discovery]] (coverage: Low; tactics: TA0007)
  - [[kb/attack/techniques/T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]
- [[kb/attack/techniques/T1046-network_service_discovery|T1046: Network Service Discovery]] (coverage: Low; tactics: TA0007)
- [[kb/attack/techniques/T1562-impair_defenses|T1562: Impair Defenses]] (coverage: Low; tactics: TA0005)
  - [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]
  - [[kb/attack/techniques/T1562-impair_defenses#^t1562006-indicator-blocking|T1562.006: Indicator Blocking]]
- [[kb/attack/techniques/T1098-account_manipulation|T1098: Account Manipulation]] (coverage: Low; tactics: TA0006)
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]] (coverage: Moderate; tactics: TA0002)
  - [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]
- [[kb/attack/techniques/T1012-query_registry|T1012: Query Registry]] (coverage: Low; tactics: TA0007)

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
