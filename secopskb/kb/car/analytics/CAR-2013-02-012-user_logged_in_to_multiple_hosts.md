---
car_id: "CAR-2013-02-012"
title: "User Logged in to Multiple Hosts"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-02-012/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-02-012.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-02-012"
  - "User Logged in to Multiple Hosts"
attack_technique_ids:
  - "T1078"
  - "T1078.002"
  - "T1078.003"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2013-02-012: User Logged in to Multiple Hosts

## Metadata

- CAR ID: CAR-2013-02-012
- Submission Date: 2013/02/27
- Information Domain: Host
- Analytic Type: Situational Awareness
- Platforms: Windows, Linux, macOS
- Data Subtypes: Login
- Contributors: MITRE

## Description

Most users use only one or two machines during the normal course of business. User accounts that log in to multiple machines, especially over a short period of time, may be compromised. Remote logins among multiple machines may be an indicator of [Lateral Movement](https://attack.mitre.org/tactics/TA0008).

Certain users will likely appear as being logged into several machines and may need to be "whitelisted." Such users would include network admins or user names that are common to many hosts.

### Output Description

User Name, Machines logged into, the earliest and latest times in which users were logged into the host, the type of logon, and logon ID.

## ATT&CK Coverage

- [[kb/attack/techniques/T1078-valid_accounts|T1078]] (coverage: Moderate; tactics: TA0008)
  - [[kb/attack/techniques/T1078-valid_accounts|T1078.002]]
  - [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## D3FEND Mappings

- [[kb/defend/techniques/D3-ANET-authentication_event_thresholding|D3-ANET: Authentication Event Thresholding]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-02-012/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-02-012.yaml)
