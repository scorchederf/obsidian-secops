---
car_id: "CAR-2014-07-001"
title: "Service Search Path Interception"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-07-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-07-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2014-07-001"
  - "Service Search Path Interception"
attack_technique_ids:
  - "T1574"
  - "T1574.009"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2014-07-001: Service Search Path Interception

## Metadata

- CAR ID: CAR-2014-07-001
- Submission Date: 2014/07/17
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: MITRE

## Description

According to [ATT&CK](https://attack.mitre.org/), an adversary may [escalate privileges](https://attack.mitre.org/tactics/TA0004) by [intercepting the search path](https://attack.mitre.org/techniques/T1579/009) for legitimately installed services. As a result, Windows will launch the target executable instead of the desired binary and command line. This can be done when there are spaces in the binary path and the path is unquoted. Search path interception should never happen legitimately and will likely be the result of an adversary abusing a system misconfiguration. With a few regular expressions, it is possible to identify the execution of services with intercepted search paths.

## ATT&CK Coverage

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574]] (coverage: High; tactics: TA0004, TA0003)
  - [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.009]]

## Implementations

### pseudocode

Look over all service creations that have a quoted path for the first argument. Assuming these still have an absolute path, look for cases in which the command line has a space, but the exe field is not part of the command line. This would indicate that a different process was intended, but the path was intercepted at an earlier space.

```pseudocode
process = search Process:Create
services = filter processes where (parent_exe == "services.exe")
unquoted_services = filter services where (command_line != "\"*" and command_line == "* *")
intercepted_service = filter unquoted_service where (image_path != "* *" and exe not in command_line)
output intercepted_service
```

## Data Model References

- process/create/command_line
- process/create/image_path
- process/create/parent_exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-07-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-07-001.yaml)
