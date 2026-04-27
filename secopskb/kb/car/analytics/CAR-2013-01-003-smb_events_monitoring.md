---
car_id: "CAR-2013-01-003"
title: "SMB Events Monitoring"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-01-003/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-01-003.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-01-003"
  - "SMB Events Monitoring"
attack_technique_ids:
  - "T1039"
  - "T1021"
  - "T1021.002"
platforms:
  - "N/A"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2013-01-003: SMB Events Monitoring

## Metadata

- CAR ID: CAR-2013-01-003
- Submission Date: 2013/01/25
- Information Domain: Network
- Analytic Type: Situational Awareness
- Platforms: N/A
- Data Subtypes: PCAP
- Contributors: MITRE

## Description

[Server Message Block](https://en.wikipedia.org/wiki/Server_Message Block) (SMB) is used by Windows to allow for file, pipe, and printer sharing over port 445/tcp. It allows for enumerating, and reading from and writing to file shares for a remote computer. Although it is heavily used by Windows servers for legitimate purposes and by users for file and printer sharing, many adversaries also use SMB to achieve [Lateral Movement](https://attack.mitre.org/tactics/TA0008). Looking at this activity more closely to obtain an adequate sense of situational awareness may make it possible to detect adversaries moving between hosts in a way that deviates from normal activity. Because SMB traffic is heavy in many environments, this analytic may be difficult to turn into something that can be used to quickly detect an APT. In some cases, it may make more sense to run this analytic in a forensic fashion. Looking through and filtering its output after an intrusion has been discovered may be helpful in identifying the scope of compromise.

### Output Description

The source, destination, content, and time of each event.

## ATT&CK Coverage

- [[kb/attack/techniques/T1039-data_from_network_shared_drive|T1039]] (coverage: Moderate; tactics: TA0009)
- [[kb/attack/techniques/T1021-remote_services|T1021]] (coverage: Moderate; tactics: TA0008)
  - [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Implementations

### pseudocode

Although there may be more native ways to detect detailed SMB events on the host, they can be extracted out of network traffic. With the right protocol decoders, port 445 traffic can be filtered and even the file path (relative to the share) can be retrieved.

```pseudocode
flow = search Flow:Message
smb_events = filter flow where (dest_port == "445" and protocol == "smb")
smb_events.file_name = smb_events.proto_info.file_name
output smb_write
```

## Data Model References

- flow/message/dest_port
- flow/message/proto_info

## D3FEND Mappings

- [[kb/defend/techniques/D3-IPCTA-ipc_traffic_analysis|D3-IPCTA: IPC Traffic Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-01-003/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-01-003.yaml)
