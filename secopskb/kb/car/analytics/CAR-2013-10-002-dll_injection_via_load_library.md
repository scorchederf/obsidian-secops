---
car_id: "CAR-2013-10-002"
title: "DLL Injection via Load Library"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-10-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-10-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-10-002"
  - "DLL Injection via Load Library"
attack_technique_ids:
  - "T1055"
  - "T1055.001"
  - "T1548"
  - "T1548.002"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2013-10-002: DLL Injection via Load Library

## Metadata

- CAR ID: CAR-2013-10-002
- Submission Date: 2013/10/07
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process DLL
- Contributors: MITRE

## Description

Microsoft Windows allows for processes to remotely create threads within other processes of the same privilege level. This functionality is provided via the Windows API [CreateRemoteThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682437.aspx). Both Windows and third-party software use this ability for legitimate purposes. For example, the Windows process [csrss.exe](https://en.wikipedia.org/wiki/Client/Server_Runtime_Subsystem) creates threads in programs to send signals to registered callback routines. Both adversaries and host-based security software use this functionality to [inject DLLs](https://attack.mitre.org/techniques/T1055), but for very different purposes. An adversary is likely to inject into a program to [evade defenses](https://attack.mitre.org/tactics/TA0005) or [bypass User Account Control](https://attack.mitre.org/techniques/T1548/002), but a security program might do this to gain increased monitoring of API calls. One of the most common methods of [DLL Injection](https://attack.mitre.org/techniques/T1055) is through the Windows API [LoadLibrary](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684175.aspx).

-   Allocate memory in the target program with [VirtualAllocEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366890.aspx)
-   Write the name of the DLL to inject into this program with [WriteProcessMemory](https://msdn.microsoft.com/en-us/library/windows/desktop/ms681674.aspx)
-   Create a new thread and set its entry point to [LoadLibrary](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684175.aspx) using the API [CreateRemoteThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682437.aspx).

This behavior can be detected by looking for thread creations across processes, and resolving the entry point to determine the function name. If the function is `LoadLibraryA` or `LoadLibraryW`, then the intent of the remote thread is clearly to inject a DLL. When this is the case, the source process must be examined so that it can be ignored when it is both expected and a trusted process.

## ATT&CK Coverage

- [[kb/attack/techniques/T1055-process_injection|T1055]] (coverage: Moderate; tactics: TA0005)
  - [[kb/attack/techniques/T1055-process_injection|T1055.001]]
- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]] (coverage: Moderate; tactics: TA0004)
  - [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Implementations

### pseudocode

Search for remote thread creations that start at LoadLibraryA or LoadLibraryW. Depending on the tool, it may provide additional information about the DLL string that is an argument to the function. If there is any security software that legitimately injects DLLs, it must be carefully whitelisted.

```pseudocode
remote_thread = search Thread:RemoteCreate
remote_thread = filter (start_function == "LoadLibraryA" or start_function == "LoadLibraryW")
remote_thread = filter (src_image_path != "C:\Path\To\TrustedProgram.exe")

output remote_thread
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=8 start_function IN ["LoadLibraryA", "LoadLibraryW"] -source_image="C:\Path\To\TrustedProgram.exe"
```

## Data Model References

- thread/remote_create/src_pid
- thread/remote_create/start_function

## D3FEND Mappings

- [[kb/defend/techniques/D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-10-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-10-002.yaml)
