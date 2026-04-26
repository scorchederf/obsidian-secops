---
car_id: "CAR-2014-03-006"
title: "RunDLL32.exe monitoring"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-03-006/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-03-006.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2014-03-006"
  - "RunDLL32.exe monitoring"
attack_technique_ids:
  - "T1218"
  - "T1218.011"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "DNIF"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2014-03-006: RunDLL32.exe monitoring

## Metadata

- CAR ID: CAR-2014-03-006
- Submission Date: 2014/03/28
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

Adversaries may find it necessary to use [Dyanamic-link Libraries](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682589.aspx) (DLLs) to [evade defenses](https://attack.mitre.org/tactics/TA0005). One way these DLLs can be "executed" is through the use of the built-in Windows utility [RunDLL32](https://attack.mitre.org/techniques/T1218.011), which allows a user to execute code in a DLL, providing the name and optional arguments to an exported entry point. Windows uses RunDll32 legitimately in its normal operation, but with a proper baseline and understanding of the environment, monitoring its usage could be fruitful.

## ATT&CK Coverage

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]] (coverage: Moderate; tactics: TA0005)
  - [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Implementations

### pseudocode

When looking for all instances of RunDLL32, it is imperative to also have the `command_line` information, which contains the DLL information, including the name, entry point, and optional arguments.

```pseudocode
process = search Process:Create
rundll32 = filter process where (exe == "rundll32.exe")
output rundll32
```

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-SYSMON AND $EventID=1 AND $App=rundll32.exe limit 100
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 image="*\rundll32.exe"
```

## Data Model References

- process/create/exe
- process/create/command_line

## Unit Tests

Execute rundll32.exe from a command window

- Configurations: Windows 7

```text
c:\windows\syswow64\rundll32.exe
RUNDLL32.EXE SHELL32.DLL,Control_RunDLL desk.cpl,,0
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-03-006/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-03-006.yaml)
