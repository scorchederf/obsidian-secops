---
car_id: "CAR-2013-02-008"
title: "Simultaneous Logins on a Host"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-02-008/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-02-008.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-02-008"
  - "Simultaneous Logins on a Host"
attack_technique_ids:
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

# CAR-2013-02-008: Simultaneous Logins on a Host

## Metadata

- CAR ID: CAR-2013-02-008
- Submission Date: 2013/02/18
- Information Domain: Host
- Analytic Type: Situational Awareness
- Platforms: Windows, Linux, macOS
- Data Subtypes: Login
- Contributors: MITRE

## Description

Multiple users logged into a single machine at the same time, or even within the same hour, do not typically occur in networks we have observed.

Logon events are Windows Event Code 4624 for Windows Vista and above, 518 for pre-Vista. Logoff events are 4634 for Windows Vista and above, 538 for pre-Vista.
Logon types 2, 3, 9 and 10 are of interest. For more details see the Logon Types table on Microsoft's [Audit Logon Events](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc787567(v=ws.10)) page.

## ATT&CK Coverage

- [[kb/attack/techniques/T1078-valid_accounts|T1078]] (coverage: Low; tactics: TA0001)
  - [[kb/attack/techniques/T1078-valid_accounts|T1078.002]]
  - [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Implementations

### pseudocode

```pseudocode
users_list = search UserSession:Login
users_grouped = group users_list by hostname
users_grouped = from users_grouped select min(time) as earliest_time, max(time) as latest_time count(user) as user_count
multiple_logins = filter users_grouped where (latest_time - earliest_time <= 1 hour and user_count > 1)
output multiple_logins
```

## Data Model References

- user_session/login/user
- user_session/login/hostname

## D3FEND Mappings

- [[kb/defend/techniques/D3-ANET-authentication_event_thresholding|D3-ANET: Authentication Event Thresholding]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-02-008/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-02-008.yaml)
