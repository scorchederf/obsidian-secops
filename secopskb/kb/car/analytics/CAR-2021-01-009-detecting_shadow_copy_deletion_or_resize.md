---
car_id: "CAR-2021-01-009"
title: "Detecting Shadow Copy Deletion or Resize"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-01-009/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-009.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2021-01-009"
  - "Detecting Shadow Copy Deletion or Resize"
attack_technique_ids:
  - "T1490"
platforms:
  - "Windows"
implementation_types:
  - "Splunk"
  - "Elastic"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2021-01-009: Detecting Shadow Copy Deletion or Resize

## Metadata

- CAR ID: CAR-2021-01-009
- Submission Date: 2020/12/11
- Update Date: 2022/02/03
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: Process
- Contributors: Cyware Labs, Lucas Heiligenstein

## Description

After compromising a network of systems, threat actors often try to delete/resize Shadow Copy in an attempt to prevent administrators from restoring the systems to versions present before the attack. This is often done via vssadmin, a legitimate Windows tool to interact with shadow copies. This action is often employed by ransomware, may lead to a failure in recovering systems after an attack. The pseudo code detection focus on Windows Security and Sysmon process creation (4688 and 1). The use of wmic to delete shadow copy generates WMI-Activity Operationnal 5857 event and could generate 5858 (if the operation fails). These 2 EventIDs could be interesting when attackers use wmic without process creation and/or for forensics.

## ATT&CK Coverage

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]] (coverage: Low; tactics: TA0040)

## Implementations

### Splunk

This query looks for the deletion or resizing of shadow copy volumes, which may possibly indicate malicious activity.

```splunk
((EventCode="4688" OR EventCode="1") (CommandLine="*vssadmin* *delete* *shadows*" OR CommandLine="*wmic* *shadowcopy* *delete*" OR CommandLine="*vssadmin* *resize* *shadowstorage*")) OR (EventCode="5857" ProviderName="MSVSS__PROVIDER") OR (EventCode="5858" Operation="*Win32_ShadowCopy*")
```

### Elastic

This query looks for the deletion or resizing of shadow copy volumes, which may possibly indicate malicious activity.

```elastic
(EventCode:("4688" OR "1") AND process.command_line:(*vssadmin*\ *delete*\ *shadows* OR *wmic*\ *shadowcopy*\ *delete* OR *vssadmin*\ *resize*\ *shadowstorage*)) OR (EventCode:"5857" AND ProviderName:"MSVSS__PROVIDER") OR (EventCode:"5858" AND Operation:*Win32_ShadowCopy*)
```

### LogPoint

This query looks for the deletion or resizing of shadow copy volumes, which may possibly indicate malicious activity.

```logpoint
(EventCode IN ["4688", "1"] CommandLine IN ["*vssadmin* *delete* *shadows*", "*wmic* *shadowcopy* *delete*", "*vssadmin* *resize* *shadowstorage*"]) OR (EventCode IN "5857" ProviderName IN "MSVSS__PROVIDER") OR (EventCode IN "5858" Operation IN "*Win32_ShadowCopy*")
```

## Data Model References

- process/create/command_line

## Unit Tests

Shadow copy deletion with vssadmin

```text
vssadmin.exe delete shadows /all /quiet
```

Shadow copy deletion with wmic

```text
wmic shadowcopy delete
```

Shadow copy resize with vssadmin

```text
vssadmin resize shadowstorage /for=c: /on=c: /maxsize=401MB
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-01-009/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-009.yaml)
