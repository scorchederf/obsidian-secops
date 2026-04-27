---
car_id: "CAR-2020-11-008"
title: "MSBuild and msxsl"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-11-008/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-008.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-11-008"
  - "MSBuild and msxsl"
attack_technique_ids:
  - "T1127"
  - "T1127.001"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2020-11-008: MSBuild and msxsl

## Metadata

- CAR ID: CAR-2020-11-008
- Submission Date: 2020/11/30
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Olaf Hartong

## Description

Trusted developer utilities such as MSBuild may be leveraged to run malicious code with elevated privileges. This analytic looks for any instances of msbuild.exe, which will execute any C# code placed within a given XML document; and msxsl.exe, which processes xsl transformation specifications for XML files and will execute a variaty of scripting languages contained within the XSL file. Both of these executables are rarely used outside of Visual Studio.

## ATT&CK Coverage

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]] (coverage: High; tactics: TA0005)
  - [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127.001]]

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
target_processes = filter processes where (
  (exe="C:\Program Files (x86)\Microsoft Visual Studio\*\bin\MSBuild.exe" OR exe="C:\Windows\Microsoft.NET\Framework*\msbuild.exe" OR exe="C:\users\*\appdata\roaming\microsoft\msxsl.exe") AND
  image_path!="*Microsoft Visual Studio*")
output target_processes
```

### Splunk

Looks for all instances of msbuild.exe or msxsl.exe

- Data Model: Sysmon native

```splunk
(index=__your_sysmon_index__ EventCode=1) (Image="C:\\Program Files (x86)\\Microsoft Visual Studio\\*\\bin\\MSBuild.exe" OR Image="C:\\Windows\\Microsoft.NET\\Framework*\\msbuild.exe" OR Image="C:\\users\\*\\appdata\\roaming\\microsoft\\msxsl.exe") ParentImage!="*\\Microsoft Visual Studio*")
```

### LogPoint

Looks for all instances of msbuild.exe or msxsl.exe

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 (image IN ["C:\Program Files (x86)\Microsoft Visual Studio\*\bin\MSBuild.exe", "C:\Windows\Microsoft.NET\Framework*\msbuild.exe", "C:\Users\*\appdata\roaming\microsoft\msxsl.exe") -parent_image="*\Microsoft Visual Studio*")
```

## Data Model References

- process/create/exe
- process/create/image_path

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-11-008/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-008.yaml)
