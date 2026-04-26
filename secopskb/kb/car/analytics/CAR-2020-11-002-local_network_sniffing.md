---
car_id: "CAR-2020-11-002"
title: "Local Network Sniffing"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2020-11-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2020-11-002"
  - "Local Network Sniffing"
attack_technique_ids:
  - "T1040"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CAR-2020-11-002: Local Network Sniffing

## Metadata

- CAR ID: CAR-2020-11-002
- Submission Date: 2020/11/30
- Information Domain: Host
- Analytic Type: Situational Awareness
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Olaf Hartong

## Description

Adversaries may use a variety of tools to gain visibility on the current status of things on the network: which processes are listening on which ports, which services are running on other hosts, etc. This analytic looks for the names of the most common network sniffing tools. While this may be noisy on networks where sysadmins are using any of these tools on a regular basis, in most networks their use is noteworthy.

## ATT&CK Coverage

- [[kb/attack/techniques/T1040-network_sniffing|T1040]] (coverage: Moderate; tactics: TA0006, TA0007)

## Implementations

### Pseudocode

This is a pseudocode representation of the below splunk search.

- Data Model: CAR native

```pseudocode
processes = search Process:Create
sniffer_processes = filter processes where (
  exe = "tshark.exe" OR
  exe = "windump.exe" OR
  (exe = "logman.exe" AND parent_exe exists AND parent_exe!="C:\Program Files\Windows Event Reporting\Core\EventReporting.AgentService.exe") OR
  exe = "tcpdump.exe" OR
  exe = "wprui.exe" OR
  exe = "wpr.exe" )
output sniffer_processes
```

### Splunk

look for common network traffic sniffing apps being run

- Data Model: Sysmon native

```splunk
(index=__your_sysmon_index__ EventCode=1) (Image="*tshark.exe" OR Image="*windump.exe" OR (Image="*logman.exe" AND ParentImage!="?" AND ParentImage!="C:\\Program Files\\Windows Event Reporting\\Core\\EventReporting.AgentService.exe") OR Image="*tcpdump.exe" OR Image="*wprui.exe" OR Image="*wpr.exe")
```

### LogPoint

look for common network traffic sniffing apps being run

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=1 (image="*\tshark.exe" OR image="*\windump.exe" OR (image="*\logman.exe" -parent_image="?" -parent_image="C:\Program Files\Windows Event Reporting\Core\EventReporting.AgentService.exe") OR image="*\tcpdump.exe" OR image="*\wprui.exe" OR image="*\wpr.exe")
```

## Data Model References

- process/create/exe
- process/create/parent_exe

## D3FEND Mappings

- [[kb/defend/techniques/D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2020-11-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2020-11-002.yaml)
