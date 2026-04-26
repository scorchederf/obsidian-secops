---
car_id: "CAR-2021-02-001"
title: "Webshell-Indicative Process Tree"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-02-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-02-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-02-001"
  - "Webshell-Indicative Process Tree"
attack_technique_ids:
  - "T1505"
  - "T1505.003"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2021-02-001: Webshell-Indicative Process Tree

## Metadata

- CAR ID: CAR-2021-02-001
- Submission Date: 2020/11/29
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Nichols Jasper

## Description

A web shell is a web script placed on an openly accessible web server to allow an adversary to use the server as a gatway in a network. As the shell operates, commands will be issued from within the web application into the broader server operating system. This analytic looks for host enumeration executables initiated by any web service that would not normally be executed within that environment.

## ATT&CK Coverage

- [[kb/attack/techniques/T1505-server_software_component|T1505]] (coverage: Moderate; tactics: TA0003)
  - [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
suspicious_processes = filter processes where (
  (parent_exe == "w3wp.exe" OR
   parent_exe == "httpd.exe" OR
   parent_exe == "tomcat*.exe" OR
   parent_exe == "nginx.exe" ) AND
  (exe == "cmd.exe" OR
   exe == "powershell.exe" OR
   exe == "net.exe" OR
   exe == "whoami.exe" OR
   exe == "hostname.exe" OR
   exe == "systeminfo.exe" OR
   exe == "ipconfig.exe) )
output suspicious_processes
```

### Splunk

Look for host enumeration commands spawned by web services.

- Data Model: Sysmon native

```splunk
(index=__your_sysmon_index__ EventCode=1)
(ParentImage="C:\\Windows\\System32\\*w3wp.exe" OR ParentImage="*httpd.exe" OR ParentImage="*tomcat*.exe" OR ParentImage="*nginx.exe")
(Image="C:\\Windows\\System32\\cmd.exe OR Image="C:\\Windows\\SysWOW64\\cmd.exe" OR Image="C:\\Windows\\System32\\*\\powershell.exe OR Image="C:\\Windows\SysWOW64\\*\powershell.exe OR Image="C:\\Windows\\System32\\net.exe" OR Image="C:\\Windows\\System32\\hostname.exe" OR Image="C:\\Windows\\System32\\whoami.exe" OR Image="*systeminfo.exe OR Image="C:\\Windows\\System32\\ipconfig.exe")
```

## Data Model References

- process/create/exe
- process/create/parent_exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-02-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-02-001.yaml)
