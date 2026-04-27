---
car_id: "CAR-2013-10-001"
title: "User Login Activity Monitoring"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2013-10-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-10-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2013-10-001"
  - "User Login Activity Monitoring"
attack_technique_ids:
  - "T1021"
  - "T1021.001"
  - "T1078"
  - "T1078.002"
  - "T1078.003"
platforms:
  - "Windows"
  - "Linux"
  - "macOS"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "DNIF"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR-2013-10-001: User Login Activity Monitoring

## Metadata

- CAR ID: CAR-2013-10-001
- Submission Date: 2013/10/03
- Information Domain: Host, Network
- Analytic Type: Situational Awareness
- Platforms: Windows, Linux, macOS
- Data Subtypes: Login, Netflow
- Contributors: MITRE

## Description

Monitoring logon and logoff events for hosts on the network is very important for situational awareness. This information can be used as an indicator of unusual activity as well as to corroborate activity seen elsewhere.

Could be applied to a number of different types of monitoring depending on what information is desired. Some use cases include monitoring for all remote connections and building login timelines for users.
Logon events are Windows Event Code 4624 for Windows Vista and above, 518 for pre-Vista. Logoff events are 4634 for Windows Vista and above, 538 for pre-Vista.

### Output Description

The time of login events for distinct users on individual systems

## ATT&CK Coverage

- [[kb/attack/techniques/T1021-remote_services|T1021]] (coverage: Moderate; tactics: TA0008)
  - [[kb/attack/techniques/T1021-remote_services|T1021.001]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078]] (coverage: Moderate; tactics: TA0005)
  - [[kb/attack/techniques/T1078-valid_accounts|T1078.002]]
  - [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Implementations

### Pseudocode

This base pseudocode looks for user logon events and filters out the top 30 account names to reduce the occurrence of noisy service accounts and the like. It is meant as a starting point for situational awareness around such events.

```pseudocode
logon_events = search User_Session:Login
filtered_logons = filter logon_events where (
  user NOT IN TOP30(user))
output filtered_logons
```

### Splunk

Splunk version of the above pseudocode. NOTE - this is liable to be quite noisy and will need tweaking, especially in terms of the number of top users filtered out.

```splunk
index=__your_win_event_log_index__ EventCode=4624|search NOT [search index=__your_win_event_log_index__ EventCode=4624|top 30 Account_Name|table Account_Name]
```

### DNIF

DNIF version of the above pseudocode.

- Data Model: Sysmon native

```dnif
_fetch * from event where $LogName=WINDOWS-NXLOG-AUDIT AND $SubSystem=AUTHENTICATION AND $Action=LOGIN group count_unique $ScopeID, $User limit 30
>>_store in_disk david_test win_top_30 stack_replace
>>_fetch * from event where $LogName=WINDOWS-NXLOG-AUDIT AND $SubSystem=AUTHENTICATION AND $Action=LOGIN limit 10000
>>_checkif lookup david_test win_top_30 join $ScopeID = $ScopeID str_compare $User eq $User exclude
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-ANET-authentication_event_thresholding|D3-ANET: Authentication Event Thresholding]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2013-10-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2013-10-001.yaml)
