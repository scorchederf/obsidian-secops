---
car_id: "CAR-2014-02-001"
title: "Service Binary Modifications"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-02-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-02-001.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2014-02-001"
  - "Service Binary Modifications"
attack_technique_ids:
  - "T1543"
  - "T1543.003"
  - "T1574"
  - "T1574.010"
  - "T1569"
  - "T1569.002"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Adversaries may modify the binary file for an existing service to achieve [Persistence](https://attack.mitre.org/tactics/TA0003) while potentially [evading defenses](https://attack.mitre.org/tactics/TA0005). If a newly created or modified runs as a service, it may indicate APT activity. However, services are frequently installed by legitimate software. A well-tuned baseline is essential to differentiating between benign and malicious service modifications.

### Output Description

The Service Name and approximate time in which changes occurred on each host

## ATT&CK Coverage

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543: Create or Modify System Process]] (coverage: Moderate; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574: Hijack Execution Flow]] (coverage: Moderate; tactics: TA0003, TA0004)
  - [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574010-services-file-permissions-weakness|T1574.010: Services File Permissions Weakness]]
- [[kb/attack/techniques/T1569-system_services|T1569: System Services]] (coverage: Moderate; tactics: TA0002)
  - [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

## Implementations

### pseudocode

Look for events where a file was created and then later run as a service. In these cases, a new service has been created or the binary has been modified. Many programs, such as `msiexec.exe`, do these behaviors legitimately and can be used to help validate legitimate service creations/modifications.

```pseudocode
legitimate_installers = ["C:\windows\system32\msiexec.exe", "C:\windows\syswow64\msiexec.exe", ...]

file_change = search File:Create,Modify
process = search Process:Create
service_process = filter processes where (parent_exe == "services.exe")
modified_service = join (search, filter) where (
 file_change.time < service_process.time and
 file_change.file_path == service_process.image_path
)

modified_service = filter modified_service where (modified_service.file_change.image_path not in legitimate_installers)
output modified_service
```

## Data Model References

- file/create/file_path
- file/create/image_path
- process/create/image_path
- process/create/parent_exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-SBV-service_binary_verification|D3-SBV: Service Binary Verification]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-02-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-02-001.yaml)
