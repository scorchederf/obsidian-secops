---
car_id: "CAR-2014-03-005"
title: "Remotely Launched Executables via Services"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-03-005/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-03-005.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2014-03-005"
  - "Remotely Launched Executables via Services"
attack_technique_ids:
  - "T1543"
  - "T1543.003"
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

There are several ways to cause code to [execute](https://attack.mitre.org/tactics/TA0002) on a remote host. One of the most common methods is via the Windows [Service Control Manager](https://en.wikipedia.org/wiki/Service_Control_Manager) (SCM), which allows authorized users to remotely create and modify services. Several tools, such as [PsExec](https://attack.mitre.org/software/S0029), use this functionality.

When a client remotely communicates with the Service Control Manager, there are two observable behaviors. First, the client connects to the [[kb/car/analytics/CAR-2014-05-001-rpc_activity|RPC Endpoint Mapper]] over 135/tcp. This handles authentication, and tells the client what port the endpoint—in this case the SCM—is listening on. Then, the client connects directly to the listening port on `services.exe`. If the request is to start an existing service with a known command line, the the SCM process will run the corresponding command.

This compound behavior can be detected by looking for `services.exe` receiving a network connection and immediately spawning a child process.

## ATT&CK Coverage

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543: Create or Modify System Process]] (coverage: Moderate; tactics: TA0003)
  - [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[kb/attack/techniques/T1569-system_services|T1569: System Services]] (coverage: Moderate; tactics: TA0002)
  - [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

## Implementations

### pseudocode

Look for processes launched from `services.exe` within 1 second of services.exe receiving a network connection.

```pseudocode
process = search Process:Create
flow = search Flow:Start
service = filter process where (parent_exe == "services.exe")
remote_start = join (flow, service ) where (
 flow.hostname == service.hostname and
 flow.pid == service.pid and
 (flow.time < service.time < flow.time + 1 second)
)
output remote_start
```

## Data Model References

- flow/start/pid
- process/create/parent_exe
- process/create/pid

## D3FEND Mappings

- [[kb/defend/techniques/D3-RTA-rpc_traffic_analysis|D3-RTA: RPC Traffic Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-03-005/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-03-005.yaml)
