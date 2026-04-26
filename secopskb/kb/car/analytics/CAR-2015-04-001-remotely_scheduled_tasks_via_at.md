---
car_id: "CAR-2015-04-001"
title: "Remotely Scheduled Tasks via AT"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2015-04-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2015-04-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2015-04-001"
  - "Remotely Scheduled Tasks via AT"
attack_technique_ids:
  - "T1053"
  - "T1053.002"
platforms:
  - "Windows"
implementation_types:
  - "pseudocode"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2015-04-001: Remotely Scheduled Tasks via AT

## Metadata

- CAR ID: CAR-2015-04-001
- Submission Date: 2015/04/29
- Information Domain: Host, Network
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: File API, PCAP
- Contributors: MITRE

## Description

When AT.exe is used to remotely [schedule tasks](https://attack.mitre.org/techniques/T1053), Windows uses named pipes over [SMB](https://en.wikipedia.org/wiki/Server_Message_Block) to communicate with the API on the remote machine. After authentication over SMB, the Named Pipe "ATSVC" is opened, over which the JobAdd function is called. On the remote host, the job files are created by the Task Scheduler and follow the convention `C:\Windows\System32\AT<job\_id>`. Unlike [[kb/car/analytics/CAR-2013-05-004-execution_with_at|CAR-2013-05-004]], this analytic specifically focuses on uses of AT that can be detected between hosts, indicating remotely gained [execution](https://attack.mitre.org/tactics/TA0002).

This pipe activity could be discovered with a network decoder, such as that in wireshark, that can inspect SMB traffic to identify the use of pipes. It could also be detected by looking for raw packet capture streams or from a custom sensor on the host that hooks the appropriate API functions. If no network or API level of visibility is possible, this traffic may inferred by looking at SMB connections over 445/tcp followed by the creation of files matching the pattern `C:\Windows\System32\AT\<job_id\>`.

## ATT&CK Coverage

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053]] (coverage: Moderate; tactics: TA0002)
  - [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]

## Implementations

### pseudocode

To detect AT via network traffic, a sensor is needed that has the ability to extract and decode PCAP information. Specifically, it needs to properly decode SMB and the functions that are implemented over it via NamedPipes. If a sensor meets these criteria, then the PCAP data needs to search for instances of the command `JobAdd` over the pipe `ATSVC`, which is all implemented over Windows SMB 445/tcp.

```pseudocode
flows = search Flow:Message
at_proto = filter flows where (dest_port == 445 and proto_info.pipe == "ATSVC")
at_create = filter flows where (proto_info.function == "JobAdd")

output at_create
```

## Data Model References

- flow/message/proto_info

## D3FEND Mappings

- [[kb/defend/techniques/D3-IPCTA-ipc_traffic_analysis|D3-IPCTA: IPC Traffic Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2015-04-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2015-04-001.yaml)
