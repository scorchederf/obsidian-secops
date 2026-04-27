---
car_id: "CAR-2013-09-003"
title: "SMB Session Setups"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-09-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-09-003.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-09-003"
  - "SMB Session Setups"
attack_technique_ids:
  - "T1187"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2013-09-003: SMB Session Setups

## Metadata

- CAR ID: CAR-2013-09-003
- Submission Date: 2013/09/12
- Information Domain: Network
- Analytic Type: Situational Awareness
- Platforms: 
- Data Subtypes: PCAP
- Contributors: MITRE

## Description

Account usage within SMB can be used to identify compromised credentials, and the hosts accessed with them.

This analytic monitors SMB activity that deals with user activity rather than file activity.

## ATT&CK Coverage

- [[kb/attack/techniques/T1187-forced_authentication|T1187]] (coverage: Low; tactics: TA0006)

## Implementations

### pseudocode

```pseudocode
flow = search Flow:Message
smb_setup = filter flow where (dest_port == 445 and protocol == smb.setup)
smb_setup.user = smb_write.proto_info.user_name
smb_setup.target_host = smb_write.proto_info.hostname
output smb_write
```

## Data Model References

- flow/message/dest_port
- flow/message/proto_info
- flow/message/protocol

## D3FEND Mappings

- [[kb/defend/techniques/D3-IPCTA-ipc_traffic_analysis|D3-IPCTA: IPC Traffic Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-09-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-09-003.yaml)
