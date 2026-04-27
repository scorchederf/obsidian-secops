---
car_id: "CAR-2015-04-002"
title: "Remotely Scheduled Tasks via Schtasks"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2015-04-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2015-04-002.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2015-04-002"
  - "Remotely Scheduled Tasks via Schtasks"
attack_technique_ids:
  - "T1053"
  - "T1053.005"
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

An adversary can [move laterally](https://attack.mitre.org/tactics/TA0008) using the `schtasks` command to remotely [schedule tasks/jobs](https://attack.mitre.org/techniques/T1053). Although these events can be detected with command line analytics [[kb/car/analytics/CAR-2013-08-001-execution_with_schtasks|CAR-2013-08-001]], it is possible for an adversary to use the API directly, via the Task Scheduler GUI or with a scripting language such as [PowerShell](https://attack.mitre.org/techniques/T1059/001). In this cases, an additional source of data becomes necessary to detect adversarial behavior. When scheduled tasks are created remotely, Windows uses RPC (135/tcp) to communicate with the Task Scheduler on the remote machine. Once an RPC connection is established ([[kb/car/analytics/CAR-2014-05-001-rpc_activity|CAR-2014-05-001]]), the client communicates with the Scheduled Tasks endpoint, which runs within the service group netsvcs. With packet capture and the right packet decoders or byte-stream based signatures, remote invocations of these functions can be identified.

Certain strings can be identifiers of the schtasks, by looking up the interface UUID of ITaskSchedulerService in different formats

-   UUID `86d35949-83c9-4044-b424-db363231fd0c` (decoded)
-   Hex `49 59 d3 86 c9 83 44 40 b4 24 db 36 32 31 fd 0c` (raw)
-   ASCII `IYD@$621` (printable bytes only)

This identifier is present three times during the RPC request phase. Any sensor that has access to the byte code as raw, decoded, or ASCII could implement this analytic.

## ATT&CK Coverage

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053: Scheduled Task/Job]] (coverage: Moderate; tactics: TA0002)
  - [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]

## Implementations

### pseudocode

Look for RPC traffic after being mapped, which implies a destination port of at least 49152. If network inspection is available via packet captures or a NIDS, then traffic through the `ITaskSchedulerService` interface can be detected. Microsoft has a list of the possible methods that are implemented for the `ITaskSchedulerService` interface, which may be useful in differentiating read and query operations from creations and modifications.

```pseudocode
flows = search Flow:Message
schtasks_rpc = filter flows where (
 src_port >= 49152 and dest_port >= 49152 and
 proto_info.rpc_interface == "ITaskSchedulerService"
)

output schtasks_rpc
```

## Data Model References

- flow/message/dest_port
- flow/message/src_port
- flow/message/proto_info

## D3FEND Mappings

- [[kb/defend/techniques/D3-RTA-rpc_traffic_analysis|D3-RTA: RPC Traffic Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2015-04-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2015-04-002.yaml)
