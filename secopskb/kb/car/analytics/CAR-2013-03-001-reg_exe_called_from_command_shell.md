---
car_id: "CAR-2013-03-001"
title: "Reg.exe called from Command Shell"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-03-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-03-001.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2013-03-001"
  - "Reg.exe called from Command Shell"
attack_technique_ids:
  - "T1012"
  - "T1112"
  - "T1547"
  - "T1547.001"
  - "T1574"
  - "T1574.011"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "DNIF"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Registry modifications are often essential in establishing persistence via known Windows mechanisms. Many legitimate modifications are done graphically via `regedit.exe` or by using the corresponding channels, or even calling the Registry APIs directly. The built-in utility `reg.exe` provides a [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) to the registry, so that queries and modifications can be performed from a shell, such as `cmd.exe`. When a user is responsible for these actions, the parent of `cmd.exe` will likely be `explorer.exe`. Occasionally, power users and administrators write scripts that do this behavior as well, but likely from a different process tree. These background scripts must be learned so they can be tuned out accordingly.

### Output Description

The sequence of processes that resulted in `reg.exe` being started from a shell. That is, a hierarchy that looks like

-   `great-grand_parent.exe`
-   `grand_parent.exe`
-   `parent.exe`
-   `reg.exe`

## ATT&CK Coverage

- [[kb/attack/techniques/T1012-query_registry|T1012: Query Registry]] (coverage: Moderate; tactics: TA0007)
- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]] (coverage: Moderate; tactics: TA0005)
- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]] (coverage: Moderate; tactics: TA0003)
  - [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574: Hijack Execution Flow]] (coverage: Moderate; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574011-services-registry-permissions-weakness|T1574.011: Services Registry Permissions Weakness]]

## Implementations

### pseudocode

To gain better context, it may be useful to also get information about the cmd process to know its parent. This may be helpful when tuning the analytic to an environment, if this behavior happens frequently. This may also help to rule out instances of users running

```pseudocode
processes = search Process:Create
reg = filter processes where (exe == "reg.exe" and parent_exe == "cmd.exe")
cmd = filter processes where (exe == "cmd.exe" and parent_exe != "explorer.exe"")
reg_and_cmd = join (reg, cmd) where (reg.ppid == cmd.pid and reg.hostname == cmd.hostname)
output reg_and_cmd
```

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $Process=regex(.*reg\.exe.*)i AND $ParentProcess=regex(.*cmd\.exe.*)i as #A limit 100
>>_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $Process=regex(.*cmd\.exe.*)i NOT $ParentProcess=regex(.*explorer\.exe.*)i as #B limit 100
>>_checkif sjoin #B.$PPID = #A.$CPID str_compare #B.$SystemName eq #A.$SystemName include
```

## Data Model References

- process/create/command_line
- process/create/hostname
- process/create/exe
- process/create/parent_exe
- process/create/pid
- process/create/ppid

## Unit Tests

Execute reg.exe from cmd.exe. Note that the analytic joins back to the grandparent process, which in this case is explorer.exe. The query time window must include the user log on. For example, if you logged in at 8am and tested the analytic at 10am, the query needs to search from 8am to 10am, not just at 10am. Within a command window, run the command.

- Configurations: Windows 7

```text
reg.exe QUERY HKLM\Software\Microsoft
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-03-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-03-001.yaml)
