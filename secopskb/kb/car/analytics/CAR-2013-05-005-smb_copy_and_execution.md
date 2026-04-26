---
car_id: "CAR-2013-05-005"
title: "SMB Copy and Execution"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-05-005/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-05-005.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-05-005"
  - "SMB Copy and Execution"
attack_technique_ids:
  - "T1021"
  - "T1021.002"
  - "T1078"
  - "T1078.002"
  - "T1078.003"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2013-05-005: SMB Copy and Execution

## Metadata

- CAR ID: CAR-2013-05-005
- Submission Date: 2013/05/13
- Information Domain: Host, Network
- Analytic Type: TTP
- Platforms: Windows, Linux, macOS
- Data Subtypes: Network Process File, PCAP
- Contributors: MITRE

## Description

An adversary needs to gain access to other hosts to move throughout an environment. In many cases, this is a twofold process. First, a file is remotely written to a host via an SMB share (detected by [[kb/car/analytics/CAR-2013-05-003-smb_write_request|CAR-2013-05-003]]). Then, a variety of [Execution](https://attack.mitre.org/tactics/TA0002) techniques can be used to remotely establish execution of the file or script. To detect this behavior, look for files that are written to a host over SMB and then later run directly as a process or in the command line arguments. SMB File Writes and Remote Execution may happen normally in an environment, but the combination of the two behaviors is less frequent and more likely to indicate adversarial activity.

This can possibly extend to more copy protocols in order to widen its reach, or it could be tuned more finely to focus on specific program run locations (e.g. `%SYSTEMROOT%\system32`) to gain a higher detection rate.

## ATT&CK Coverage

- [[kb/attack/techniques/T1021-remote_services|T1021]] (coverage: Moderate; tactics: TA0008)
  - [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078]] (coverage: Moderate; tactics: TA0005)
  - [[kb/attack/techniques/T1078-valid_accounts|T1078.002]]
  - [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]
- [[kb/attack/techniques/T1570-lateral_tool_transfer|T1570]] (coverage: Moderate; tactics: TA0008)

## Implementations

### pseudocode

```pseudocode
process = search Process:Create
smb_write = run Analytic:CAR-2013-05-003
remote_start = join (smb_write, process) where (
 smb_write.hostname == process.hostname and
 smb_write.file_path == process.image_path
 (smb_write.time < process.time)
)
output remote_start
```

## Data Model References

- process/create/image_path
- process/create/proto_info
- process/create/hostname

## D3FEND Mappings

- [[kb/defend/techniques/D3-IPCTA-ipc_traffic_analysis|D3-IPCTA: IPC Traffic Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-05-005/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-05-005.yaml)
