---
car_id: "CAR-2013-05-003"
title: "SMB Write Request"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-05-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-05-003.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-05-003"
  - "SMB Write Request"
attack_technique_ids:
  - "T1570"
  - "T1021"
  - "T1021.002"
  - "T1078"
  - "T1078.002"
  - "T1078.003"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2013-05-003: SMB Write Request

## Metadata

- CAR ID: CAR-2013-05-003
- Submission Date: 2013/05/13
- Information Domain: Host, Network
- Analytic Type: Situational Awareness, TTP
- Platforms: Windows, Linux, macOS
- Data Subtypes: Network, Netflow, PCAP
- Contributors: MITRE

## Description

As described in [[kb/car/analytics/CAR-2013-01-003-smb_events_monitoring|CAR-2013-01-003]], SMB provides a means of remotely managing a file system. Adversaries often use SMB to move laterally to a host. SMB is commonly used to upload files. It may be used for staging in [Exfiltration](https://attack.mitre.org/tactics/TA0010) or as a [Lateral Movement](https://attack.mitre.org/tactics/TA0008) technique. Unlike SMB Reads, SMB Write requests typically require an additional level of access, resulting in less activity. Focusing on SMB Write activity narrows the field to find techniques that actively change remote hosts, instead of passively reading files.

## ATT&CK Coverage

- [[kb/attack/techniques/T1570-lateral_tool_transfer|T1570]] (coverage: Moderate; tactics: TA0008)
- [[kb/attack/techniques/T1021-remote_services|T1021]] (coverage: Moderate; tactics: TA0008)
  - [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078]] (coverage: Moderate; tactics: TA0005)
  - [[kb/attack/techniques/T1078-valid_accounts|T1078.002]]
  - [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Implementations

### pseudocode

```pseudocode
flow = search Flow:Message
smb_write = filter flow where (dest_port == "445" and protocol == "smb.write")
smb_write.file_name = smb_write.proto_info.file_name
output smb_write
```

## Data Model References

- flow/message/proto_info
- flow/message/dest_port

## D3FEND Mappings

- [[kb/defend/techniques/D3-IPCTA-ipc_traffic_analysis|D3-IPCTA: IPC Traffic Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-05-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-05-003.yaml)
