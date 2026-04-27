---
car_id: "CAR-2014-03-001"
title: "SMB Write Request - NamedPipes"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2014-03-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-03-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2014-03-001"
  - "SMB Write Request - NamedPipes"
attack_technique_ids:
  - "T1570"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2014-03-001: SMB Write Request - NamedPipes

## Metadata

- CAR ID: CAR-2014-03-001
- Submission Date: 2014/03/03
- Information Domain: Host, Network
- Analytic Type: Situational Awareness
- Platforms: Windows, Linux, macOS
- Data Subtypes: Process, Netflow
- Contributors: MITRE

## Description

An SMB write can be an indicator of lateral movement, especially when combined with other information such as execution of that written file. Named pipes are a subset of SMB write requests. Named pipes such as msftewds may not be alarming; however others, such as lsarpc, may.

Monitoring SMB write requests still creates some noise, particulary with named pipes. As a result, SMB is now split between writing named pipes and writing other files.

## ATT&CK Coverage

- [[kb/attack/techniques/T1570-lateral_tool_transfer|T1570]] (coverage: Low; tactics: TA0008)

## Implementations

### pseudocode

Look for SMB network connections over port 445. Using a sensor that can decode protocol information, extract out the name of the pipe and potentially other information. This happens legitimately so certain pipes, such as `spoolss` should be appropriately white-listed. Certain pipes do correspond to adversary activity, including:

* `WINREG` - Windows Remote Registry ([[kb/car/analytics/CAR-2014-11-005-remote_registry|CAR-2014-11-005]])
* `ATSVC` - Windows AT command ([[kb/car/analytics/CAR-2015-04-001-remotely_scheduled_tasks_via_at|CAR-2015-04-001]])

```pseudocode
flow = search Flow:Message
smb_write = filter flow where (dest_port == "445" and protocol == "smb.write_pipe")
smb_write.pipe_name = smb_write.proto_info.pipe_name
output smb_write
```

## Data Model References

- flow/message/proto_info
- flow/start/dest_port

## D3FEND Mappings

- [[kb/defend/techniques/D3-IPCTA-ipc_traffic_analysis|D3-IPCTA: IPC Traffic Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2014-03-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2014-03-001.yaml)
